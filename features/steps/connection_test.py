from behave import when, given, then
import socket
from threading import Thread
from src.utils import binding_server
from src.controllers import Controller


@given("the server is binded as {ip_address}:{port}, the server should response {response} when the app sends {request}")
def given_the_server(context, ip_address, port, response, request):
    context.ip_address = ip_address
    context.port = int(port)
    context.connected = False
    server_thread = Thread(target=binding_server,
            args=(context.ip_address, 
                context.port, {request: response}))
    server_thread.start()

@when("the app is connected to the server")
def when_the_app_is_connected_to_the_server(context):
    controller = Controller()
    controller.connect(context.ip_address, context.port)
    context.msg = controller.send(b'test')

@then("we should see the app is connected")
def then_check_the_connection(context):
    assert context.msg == b'ok'
