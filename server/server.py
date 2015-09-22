#!/usr/bin/env python3

class User:
    ONLINE, OFFLINE = 1, 2

    def __init__(self):
        self.name = 'anonymous'
        self.status = User.OFFLINE

    def get_status(self):
        "Return user's current status (currently either ONLINE or OFFLINE)"
        return self.status


class Server:
    def __init__(self):
        # should probs start a thread here?
        pass


if __name__ != '__main__':
    server = Server()  # only one server may exist
