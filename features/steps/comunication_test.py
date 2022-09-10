from behave import given, when, then
from src.controllers import Controller
from src.models import Command



@when("the app sends the stop command (address {function})")
def when_the_stop_function_is_sent(context, function):
    context.command = Command()
    context.controller = Controller(command=context.command)
    context.controller.connect(context.ip_address, context.port)
    print(context.command.to_hex())
    context.response = context.controller.send(context.controller.command.to_hex())

@then("the app should receive the response")
def then_the_app_receive_the_response_of_the_stop_command(context):
    assert context.response == b'\x30\x30\x00\x00\x00\x08\x01\x03\x00\x06\x00\x00\x00\x00'

@then("the command should have the param {index} is None")
def and_check_the_command_param(context):
    assert context.controller.command.get_param(int(index)) == None
