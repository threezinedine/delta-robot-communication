import unittest 
from src.models.properties import Property


class PropertyTest(unittest.TestCase):
    def test_to_hex_with_value_is_6(self):
        address_property = Property() 
        address_property.set_value(6)

        result = address_property.to_hex()

        assert result == b'\x00\x06'
