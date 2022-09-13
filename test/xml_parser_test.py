import unittest
from src.controllers import XMLParser



class XMLParserTest(unittest.TestCase):
    filename="test.xml"
    header = "<?xml version=\"1.0\"?>"

    def create_the_xml_file(self, commands=[]):
        with open(self.filename, 'w') as file:
            file.write("<commands>\n")
            for command in commands:
                for key, value in command.items():
                    if not isinstance(value, dict):
                        file.write(f"\t<{key}>{value}</{key}>\n")
                    else:
                        for key_2, value_2 in value.items():
            file.write("</commands>\n")

    def test_parse_no_commands_xml_file(self):
        self.create_the_xml_file(commands=[]) # create an empty command file
        parser = XMLParser(filename=self.filename)

        assert parser.get_commands_list() == []

        
    def test_parse_stop_command_from_xml_file(self):
        self.create_the_xml_file(commands=[{"name": "stop", "address": 6}])

