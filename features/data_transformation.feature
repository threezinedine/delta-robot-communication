Feature: Property convert the decimal number to a hex number
    Scenario: The decimal number less than 0xff  
        Given The property has 4 bytes
        When The property converts 125
        Then We should see the result: 00 00 00 7d
