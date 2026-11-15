"""Short-lived authenticated clients; never retry a game effect automatically."""

import json
import os
from pathlib import Path
import re
import socket
import stat
import uuid

from .service import MAX_REQUEST, MAX_RESPONSE, MUTATIONS, PROTOCOL, encoded, receive_line


class ClientError(ValueError):
    pass


def private_file(path, *, limit=4096):
    path = Path(path)
    fd = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
    with os.fdopen(fd, "rb") as source:
        info = os.fstat(source.fileno())
        if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or info.st_mode & 0o077 or info.st_size > limit:
            raise ClientError("Expected a small private file owned by this user.")
        return source.read(limit + 1)


class Client:
    def __init__(self, descriptor, *, timeout=10):
        self.descriptor = json.loads(private_file(descriptor))
        d = self.descriptor
        if (not isinstance(d, dict) or d.get("protocol") != PROTOCOL or d.get("host") != "127.0.0.1"
                or type(d.get("port")) is not int or not 1 <= d["port"] <= 65535
                or not isinstance(d.get("instance_id"), str)
                or not re.fullmatch(r"[0-9a-f]{32}", d["instance_id"])):
            raise ClientError("Invalid local session descriptor.")
        self.token = private_file(d["password_file"]).decode("ascii").strip()
        if not re.fullmatch(r"[0-9a-f]{64}", self.token):
            raise ClientError("Invalid session credential.")
        self.timeout = timeout

    def request(self, op, params=None, *, lease=None):
        request = {"protocol": PROTOCOL, "id": uuid.uuid4().hex, "token": self.token,
                   "op": op, "params": params or {}}
        if op in MUTATIONS:
            if lease is None:
                raise ClientError("Mutating requests require a previously observed session lease.")
            request.update(instance_id=lease["instance_id"], expected_generation=lease["generation"])
        payload = encoded(request)
        if len(payload) > MAX_REQUEST:
            raise ClientError("Request exceeds byte limit.")
        with socket.create_connection(("127.0.0.1", self.descriptor["port"]), timeout=self.timeout) as connection:
            connection.settimeout(self.timeout)
            connection.sendall(payload)
            response = receive_line(connection, MAX_RESPONSE)
        if (not isinstance(response, dict) or response.get("protocol") != PROTOCOL
                or response.get("id") != request["id"] or type(response.get("ok")) is not bool):
            raise ClientError("Invalid response; request outcome is unknown. Do not replay automatically.")
        return response
