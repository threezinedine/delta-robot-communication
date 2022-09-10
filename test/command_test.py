import unittest
from src.models import Command
from unittest.mock import Mock
from src.models.properties import IProperty, ISetValuable, ISetValuableProperty, DefaultParam
from src.utils.exceptions import ChangeNonChangaleProperty


class CommandTest(unittest.TestCase):
    def test_command_with_command_address_6_to_hex_function(self):
        expected_func = b'\x30\x30\x00\x00\x00\x22\x01\x06\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        command = Command()

        result = command.to_hex()

        assert result == expected_func


    def test_command_with_command_address_4_to_hex_function(self):
        function_address = 4
        expected_func = b'\x30\x30\x00\x00\x00\x22\x01\x06\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        address_property = Mock(spec=ISetValuableProperty)
        address_property.to_hex.return_value = b'\x00\x04'
        command = Command(address_property=address_property)
        command.set_function(function_address)

        result = command.to_hex()

        assert result == expected_func


    def test_set_function_changes_the_value_of_the_property(self):
        function_address = 6
        address_property = Mock(spec=ISetValuable)
        command = Command(address_property=address_property)
        command.set_function(function_address)

        address_property.set_value.assert_called_once_with(function_address)


    def test_command_with_command_address_4_to_hex_function_and_change_the_param_4th(self):
        function_address = 4
        param_index = 4
        param_value = 3
        expected_func = b'\x30\x30\x00\x00\x00\x22\x01\x06\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00'
        address_property = Mock(spec=ISetValuableProperty)
        address_property.to_hex.return_value = b'\x00\x04'
        param_property = Mock(spec=ISetValuableProperty)
        param_property.to_hex.return_value = b'\x00\x00\x00\x03'

        params = [DefaultParam()] * 6
        params[param_index] = param_property

        command = Command(address_property=address_property, params=params)
        command.set_function(function_address)
        command.set_param_value(param_index, param_value)

        result = command.to_hex()

        assert result == expected_func
        param_property.set_value.assert_called_once_with(param_value)


    def test_command_set_value_to_the_none_setable_param_with_address_6_raises_an_error(self):
        changed_param_index = 3
        new_value = 4
        command = Command()
        with self.assertRaises(ChangeNonChangaleProperty) as error:
            command.set_param_value(changed_param_index, new_value)


    def test_command_set_value_to_the_none_setable_param_with_address_5_raises_an_error(self):
        function_address = 5
        changed_param_index = 3
        new_value = 4

        address_property = Mock(spec=ISetValuableProperty)
        address_property.to_hex.return_value = b'\x00\x05'
        
        params = [DefaultParam() for _ in range(6)]
        params[4] = Mock(spec=ISetValuableProperty)
        params[4].to_hex.return_value = b'\x00\x00\x00\x05'

        command = Command(address_property=address_property, params=params)
        command.set_function(function_address)

        with self.assertRaises(ChangeNonChangaleProperty) as error:
            command.set_param_value(changed_param_index, new_value)
