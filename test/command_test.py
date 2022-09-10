import unittest
from src.models import Command


class CommandTest(unittest.TestCase):
    def test_command_with_command_address_to_hex_function(self):
        function_address = 6
        expected_func = b'\x30\x30\x00\x00\x00\x22\x01\x06\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        command = Command()
        command.set_function(function_address)

        result = command.to_hex()

        assert result == expected_func

    def test_command_with_command_address_4_to_hex_function(self):
        function_address = 7
        expected_func = b'\x30\x30\x00\x00\x00\x22\x01\x06\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        command = Command()
        command.set_function(function_address)

        result = command.to_hex()

        assert result == expected_func


