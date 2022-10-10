Feature: XML Parser can extract process from the .xml
    Scenario: The file has no command
        Given create an empty "test.xml" file
        When the XML Parser parses the file
        Then the command list from XML Parse is empty

