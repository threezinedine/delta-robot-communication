Feature: Communicate with the server by specific tasks
    Scenario: Send a stop command
        Given the server is binded as 127.0.0.1:1234
        When the app sends the stop command (address 6)
        Then the app should receive the response
        And the command should have the param 0 is None
        And the command should have the param 1 is None
        And the command should have the param 2 is None
        And the command should have the param 3 is None
        And the command should have the param 4 is None
        And the command should have the param 5 is None

