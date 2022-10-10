from behave import given, when, then
from src.controllers import Controller
from src.models import Command
from src.models.properties import Property, DefaultParam

@when("the command is set to default")
def when_the_default_is_set(context):
    context.command = Command()
    context.controller = Controller(command=context.command)

@when("the command is set to address {function}")
def when_the_command_is_set_to_address(context, function):
    address_property = Property()
    context.command = Command(address_property=address_property, params=[DefaultParam() for _ in range(Command.NUM_PARAMS)]) 
    context.command.set_function(int(function))
    context.controller = Controller(command=context.command)

@when("the command's {param_index}th param is changable, and is modified to {param_value}, reverse mode is {is_reverse}")
def the_param_of_the_command_is_changed(context, param_index, param_value, is_reverse):
    reverse = True if is_reverse == 'set' else False
    context.command.set_param(int(param_index), Property(num_bytes=4, reverse=reverse))
    context.command.set_param_value(int(param_index), int(param_value))

@when("the app sends that command")
def when_set_the_function_for_the_command_and_send(context):
    print(context.controller.command.to_hex())
    context.controller.connect(context.ip_address, context.port)
    context.response = context.controller.send(context.controller.command.to_hex())

@then("the app should receive the response")
def then_the_app_receive_the_response_of_the_stop_command(context):
    assert context.response != b'fail'
