from behave import when, given, then
from src.controllers import XMLParser


@given("create an empty \"{filename}\" file")
def given_create_an_empty_xml_file(context, filename):
    context.filename = filename
    with open(filename, 'w') as file: 
        file.write(f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
        file.write("<commands></commands>")

@when("the XML Parser parses the file")
def when_the_xml_parser_parses_the_file(context):
    context.parser = XMLParser(filename=context.filename)


@then("the command list from XML Parse is empty")
def then_the_command_list_from_xml_parser_is_empty(context):
    assert [] == context.parser.get_commands_list()
