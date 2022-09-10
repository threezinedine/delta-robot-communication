from .i_property import ISetValuableProperty


class Property(ISetValuableProperty):
    def __init__(self):
        self._value = 0
    
    def to_hex(self) -> bytearray:
        return self._value.to_bytes(2, byteorder='big')

    def set_value(self, new_value:object) -> None:
        self._value = new_value

    @property
    def changable(self):
        return True
