Feature: Communicate with the server by specific tasks
    Scenario: Send a stop command
        Given the server is binded as 127.0.0.1:1234
        When the app sends the stop command (address 6)
        Then the app should receive the response
