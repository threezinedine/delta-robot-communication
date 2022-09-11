from behave import given, when, then
from src.controllers import Controller
from src.models import Command
from src.models.properties import Property

@when("the app sends the default command")
def when_the_stop_function_is_sent(context):
    context.command = Command()
    context.controller = Controller(command=context.command)
    context.controller.connect(context.ip_address, context.port)
    context.response = context.controller.send(context.controller.command.to_hex())

@when("thap app sends the command with address {function}")
def when_set_the_function_for_the_command_and_send(context, function):
    address_property = Property()
    context.command = Command(address_property=address_property) 
    context.command.set_function(int(function))
    context.controller = Controller(command=context.command)
    context.controller.connect(context.ip_address, context.port)
    context.response = context.controller.send(context.controller.command.to_hex())

@then("the app should receive the response")
def then_the_app_receive_the_response_of_the_stop_command(context):
    assert context.response != b'fail'
