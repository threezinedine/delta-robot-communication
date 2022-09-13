from src.controllers import Controller, XMLParser
from src.models import Command, Response
from src.models.properties import Property
from src.utils import binding_server_for
from threading import Thread


if __name__ == "__main__":
    file = "process.xml"
    host = "127.0.0.1"
    port = 8090
    thread = Thread(target=binding_server_for, args=(host, port))
    thread.start()

    parser = XMLParser(filename=file)
    controller = Controller(Command())
    controller.connect(host, port)
    response = Response()

    for index, command in enumerate(parser.get_commands_list()):
        controller.command = command
        print(f"""
            --------------
            Command: {command.to_hex()}
            --------------
        """)
        response_hex = controller.send(controller.command.to_hex())
        Response.from_bytes(response, response_hex)

        print(f"""
            --------------
                Address: {response.get_function()}
                Value: {response.get_value()}
            --------------
        """)

    controller.send(b'quit')
