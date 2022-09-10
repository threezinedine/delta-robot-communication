import socket
from ..utils import create_a_socket_client
from ..models import Command


class Controller:
    def __init__(self, command=None):
        self.client = create_a_socket_client()
        self.command = command

    def connect(self, ip_address, port):
        self.client.connect((ip_address, port))

    def send(self, msg):
        self.client.send(msg)
        return self.client.recv(100)

    def set_function(self, function):
        self.command.set_function(function)
