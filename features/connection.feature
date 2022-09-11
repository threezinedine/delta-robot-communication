Feature: Checking connection
    Scenario: The controller connects to the local server.
        Given the server is binded as 127.0.0.1:8090
        When the app is connected to the server
        Then we should see the app is connected
