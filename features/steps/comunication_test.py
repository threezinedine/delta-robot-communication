from behave import given, when, then
from src.controllers import Controller



@when("the app sends the stop command (address {function})")
def when_the_stop_function_is_sent(context, function):
    context.controller = Controller()
    context.controller.set_function(int(function))
    context.response = contex.tcontroller.send(controller.command.to_bytearray())

@then("the app should receive the response")
def then_the_app_receive_the_response_of_the_stop_command(context):
    assert context.response == b'\x30\x30\x00\x00\x00\x08\x01\x03\x00\x06\x00\x00\x00\x00'

@then("the command should have the param {index} is None")
def and_check_the_command_param(context):
    assert context.controller.command.get_param(int(index)) == None
