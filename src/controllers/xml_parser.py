import xml.etree.ElementTree as ET
from ..models import Command
from ..models.properties import Property


class XMLParser:
    def __init__(self, filename=""):
        self.filename = filename

        tree = ET.parse(filename)
        self.root = tree.getroot()

    def _get_command_from_element(self, element):
        address_property = Property()
        command = Command(address_property=address_property)

        if element.find("address") is not None:
            command.set_function(element.find("address").text)

            params = element.find("parameters")

            for param in params:
                param_index = int(param.find("index").text)
                param_value = int(param.find("value").text)

                command.set_param(param_index, Property(num_bytes=4))
                command.set_param_value(param_index, param_value)
            
        return command

    def get_commands_list(self):
        commands = []
        for element in self.root.findall("command"):
            commands.append(self._get_command_from_element(element))

        return commands
