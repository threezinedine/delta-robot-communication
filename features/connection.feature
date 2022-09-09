Feature: Checking connection
    Scenario: The controller connects to the local server.
        Given the server is binded as 127.0.0.1:1234, the server should response "ok" when the app sends "test"
        When the app is connected to the server
        Then we should see the app is connected
