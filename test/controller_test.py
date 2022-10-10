import unittest
from unittest.mock import Mock
from src.controllers import Controller
from src.models import ISetFunctionable, ICommandDelayable, IDelayable
from src.utils import binding_server
from threading import Thread


class ControllerTest(unittest.TestCase):
    def test_the_command_function_is_set_when_the_controller_set_the_function(self):
        command_address = 6
        command = Mock(spec=ISetFunctionable)
        controller = Controller(command=command)
        controller.set_function(command_address)

        command.set_function.assert_called_once_with(command_address)

    def test_command_run_delay_each_time_the_command_is_sent(self):
        host = "127.0.0.1"
        port = 8090

        command = Mock(spec=IDelayable)
        controller = Controller(command=command)
        thread = Thread(target=binding_server, args=(host, port))
        thread.start()

        controller.connect(host, port)

        controller.send(b'test')

        command.delay.assert_called_once()
