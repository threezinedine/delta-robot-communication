from .i_command import ICommand
from ..models.properties import IProperty


class Command(ICommand):
    def __init__(self, address_property:IProperty=None):
        self._address_property = address_property

    def set_function(self, function:int) -> None:
        pass 

    def to_hex(self) -> bytearray:
        if self._address_property is None:
            return b'\x30\x30\x00\x00\x00\x22\x01\x06\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

        return b'\x30\x30\x00\x00\x00\x22\x01\x06'+ self._address_property.to_hex() +b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

