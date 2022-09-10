import unittest
from unittest.mock import Mock
from src.controllers import Controller
from src.models import ISetFunctionable


class ControllerTest(unittest.TestCase):
    def test_the_command_function_is_set_when_the_controller_set_the_function(self):
        command_address = 6
        command = Mock(spec=ISetFunctionable)
        controller = Controller(command=command)
        controller.set_function(command_address)

        command.set_function.assert_called_once_with(command_address)
