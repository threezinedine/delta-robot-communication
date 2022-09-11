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


    def test_to_hex_with_value_is_226(self):
        new_value = 326
        expected_result = b'\x01\x46'

        address_property = Property() 
        address_property.set_value(new_value)

        result = address_property.to_hex()

        assert result == expected_result

    def test_to_hex_with_value_is_326_4_bytes_capacity(self):
        new_value = 326
        num_bytes = 4 
        expected_result = b'\x00\x00\x01\x46'

        test_param = Property(num_bytes=num_bytes)
        test_param.set_value(new_value)

        result = test_param.to_hex()

        assert result == expected_result
