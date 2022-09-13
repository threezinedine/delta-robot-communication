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
            if commands != []:
                file.write(dict2xml(commands))
            else:
                file.write('')

    def test_parse_default_command_from_xml_file(self):
        self.create_the_xml_file(commands={"commands": {"command": [{}]}})
        parser = XMLParser(filename=self.filename)

        assert parser.get_commands_list()[0].get_function() == self.stop_command.get_function()


    def test_parse_reset_command_from_xml_file_with_no_params(self):
        function = 4
        self.create_the_xml_file(commands={"commands": {"command": [{"name": "reset", "address": function, "parameters": []}]}})
        parser = XMLParser(filename=self.filename)

        address_property = Property() 
        reset_command = Command(address_property=address_property)
        reset_command.set_function(function)

        assert parser.get_commands_list()[0].get_function() == reset_command.get_function()


    def test_parse_reset_command_from_xml_file_with_no_params_without_name_should_have_empty_name(self):
        function = 4
        self.create_the_xml_file(commands={"commands": {"command": [{"address": function, "parameters": []}]}})
        parser = XMLParser(filename=self.filename)

        address_property = Property() 
        reset_command = Command(address_property=address_property)
        reset_command.set_function(function)

        assert parser.get_commands_list()[0].get_name() == ''

    def test_parse_reset_command_from_xml_file_with_no_params_with_name_should_have_name(self):
        function = 4
        self.create_the_xml_file(commands={"commands": {"command": [{"name": "reset", "address": function, "parameters": []}]}})
        parser = XMLParser(filename=self.filename)

        address_property = Property() 
        reset_command = Command(address_property=address_property)
        reset_command.set_function(function)

        assert parser.get_commands_list()[0].get_name() == 'reset'


    def test_parse_reset_command_from_xml_file_with_no_params_should_has_the_name(self):
        function = 4
        self.create_the_xml_file(commands={"commands": {"command": [{"name": "reset", "address": function, "parameters": []}]}})
        parser = XMLParser(filename=self.filename)

        address_property = Property() 
        reset_command = Command(address_property=address_property)
        reset_command.set_function(function)

        assert parser.get_commands_list()[0].get_function() == reset_command.get_function()


    def test_parse_stop_command_from_xml_file(self):
        function = 4
        self.create_the_xml_file(commands={"commands": {"command": [{"name": "reset", "address": function, "parameters": [{"parameter": [{"index": 4, "value": 4}, {"index": 5, "value": 1}]}]}]}})
        parser = XMLParser(filename=self.filename)

        assert parser.get_commands_list()[0].check_param_changable(4)
        assert parser.get_commands_list()[0].check_param_changable(5)

    def test_parse_multiple_command_from_xml_file(self):
        self.create_the_xml_file(commands={"commands": {"command": [{"name": "stop", "address": 6, "parameters": [{"parameter": [{"index": 1, "value": 13}]}]}, {"name": "reset", "address": 4, "parameters": [{"parameter": [{"index": 4, "value": 4}, {"index": 5, "value": 1}]}]}]}})

        parser = XMLParser(filename=self.filename)

        default_command, reset_command = parser.get_commands_list()

        assert default_command.get_function() == 6
        assert default_command.check_param_changable(1)
        assert default_command.get_param_value(1) == 13
        assert reset_command.get_function() == 4
        assert reset_command.check_param_changable(4)
        assert reset_command.get_param_value(4) == 4
        assert reset_command.get_param_value(5) == 1
