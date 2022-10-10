Feature: Communicate with the server by specific tasks
    Scenario: Send a stop command
        Given the server is binded as 127.0.0.1:8090
        When the command is set to default
        And the app sends that command
        Then the app should receive the response

    Scenario: Send a command with the address function 6
        Given the server is binded as 127.0.0.1:8090 
        When the command is set to address 6
        And the app sends that command
        Then the app should receive the response

    Scenario: Send a command with the address function 4, the 4th param is modified to 1523
        Given the server is binded as 127.0.0.1:8090 
        When the command is set to address 4
        And the command's 4th param is changable, and is modified to 1523, reverse mode is not-set
        And the app sends that command
        Then the app should receive the response

    Scenario: Send a command with the address function 3, the 2rd param is modified to -700
        Given the server is binded as 127.0.0.1:8090
        When the command is set to address 3
        And the command's 2th param is changable, and is modified to -700000, reverse mode is set
        And the app sends that command
        Then the app should receive the response
