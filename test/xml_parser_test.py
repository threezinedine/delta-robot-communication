import unittest
from src.controllers import XMLParser
from dict2xml import dict2xml
from src.models import Command
from src.models.properties import Property


class XMLParserTest(unittest.TestCase):
    filename="test.xml"
    header = "<?xml version=\"1.0\"?>"

    address_property = Property()
    stop_command = Command(address_property)

    def create_the_xml_file(self, commands=[]):
        with open(self.filename, 'w') as file:
            file.write(dict2xml(commands, wrap="commands"))

    def test_parse_no_commands_xml_file(self):
        self.create_the_xml_file(commands=[]) # create an empty command file
        parser = XMLParser(filename=self.filename)

        assert parser.get_commands_list() == []

        
    def test_parse_default_command_from_xml_file(self):
        self.create_the_xml_file(commands={"command": {}})
        parser = XMLParser(filename=self.filename)

        assert parser.get_commands_list()[0].get_function() == self.stop_command.get_function()


    def test_parse_stop_command_from_xml_file(self):
        function = 4
        self.create_the_xml_file(commands={"command": {"name": "reset", "address": function, "parameters": {"parameter": {"index": 4, "value": 4}}}})
        parser = XMLParser(filename=self.filename)

        address_property = Property() 
        reset_command = Command(address_property=address_property)
        reset_command.set_function(function)

        assert parser.get_commands_list()[0].get_function() == reset_command.get_function()
