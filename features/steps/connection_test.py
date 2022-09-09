from behave import when, given, then
import socket
from threading import Thread


@given("the server is binded as {ip_address}:{port}")
def given_the_server(context, ip_address, port):
    context.ip_address = ip_address
    context.port = int(port)
    context.connected = False
    server_thread = Thread(target=binding_server, 
            args=(ip_address, port, context.connected))
    server_thread.start()
    server_thread.join()

@when("the app is connected to the server")
def when_the_app_is_connected_to_the_server(context):
    controller = Controller(context.ip_address, context.port)
    controller.connect()

@then("we should see the app is connected")
def then_check_the_connection(context):
    assert context.connected
