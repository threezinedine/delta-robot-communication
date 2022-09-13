import xml.etree.ElementTree as ET
from ..models import Command
from ..models.properties import Property


class XMLParser:
    def __init__(self, filename=""):
        self.filename = filename

        tree = ET.parse(filename)
        self.root = tree.getroot()

    def _get_command_from_element(self, element):
        return Command()

    def get_commands_list(self):
        commands = []
        for element in self.root.findall("command"):
            commands.append(self._get_command_from_element(element))

        return commands
