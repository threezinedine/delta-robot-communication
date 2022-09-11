Feature: Receive response from the server
    Scenario: Receive a command from the server 
        Given the server is binded as 127.0.0.1:1234
        When the command is set to default
        And the app sends that command
        Then the app should receive the address "6" and value "0"
