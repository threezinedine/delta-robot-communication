Feature: Receive response from the server
    Scenario: Receive a command from the server 
        Given the server is binded as 127.0.0.1:8090
        When the command is set to address 5
        And the command's 4th param is changable, and is modified to 1, reverse mode is not-set
        And the app sends that command
        Then the app should receive the address "5" and value "1"
