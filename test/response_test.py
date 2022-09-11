import unittest
from unittest.mock import Mock
from src.models import Response



class ResposeTest(unittest.TestCase):
    def test_from_bytes_response_with_the_default_response(self):
        response_b = b'\x30\x30\x00\x00\x00\x08\x01\x03\x00\x06\x00\x00\x00\x00'
        response = Response.from_bytes(response_b)

        assert response.get_function() == 6
        assert response.get_value() == 0
