Feature: Communicate with the server by specific tasks
    Scenario: Send a stop command
        Given the server is binded as 127.0.0.1:1234
        When the app sends the default command
        Then the app should receive the response

    Scenario: Send a command with the address function 6
        Given the server is binded as 127.0.0.1:1234 
        When thap app sends the command with address 6
        Then the app should receive the response
