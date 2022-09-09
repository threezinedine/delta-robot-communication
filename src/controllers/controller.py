import socket
from ..utils import create_a_socket_client


class Controller:
    def __init__(self):
        self.client = create_a_socket_client()

    def connect(self, ip_address, port):
        self.client.connect((ip_address, port))

    def send(self, msg):
        self.client.send(msg)
        return self.client.recv(100)
