import unittest
from src.models import Command


class CommandTest(unittest.TestCase):
    def test_command_with_command_address_to_hex_function(self):
        command = Command()
        command.set_function(6)

        result = command.to_hex()

        assert result == b'\x30\x30\x00\x00\x00\x22\x01\x06\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
