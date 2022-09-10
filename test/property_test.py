import unittest 
from src.models.properties import Property


class PropertyTest(unittest.TestCase):
    def test_to_hex_with_value_is_6(self):
        new_value = 6
        expected_result = b'\x00\x06'

        address_property = Property() 
        address_property.set_value(new_value)

        result = address_property.to_hex()

        assert result == expected_result
