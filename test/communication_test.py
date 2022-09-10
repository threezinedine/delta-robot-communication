import unittest
from unittest.mock import Mock
from src.controllers import Controller
from src.models import ICommand


class ControllerTest(unittest.TestCase):
    def test_the_command_function_is_set_when_the_controller_set_the_function(self):
        command = Mock(spec=ICommand)
        controller = Controller(command=command)
        controller.set_function(6)

        command.set_function.assert_called_once_with(6)
