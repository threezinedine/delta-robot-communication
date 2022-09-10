from .i_property import ISetValuableProperty


class Property(ISetValuableProperty):
    BYTEORDER = 'big'

    def __init__(self):
        self._value = 0
        self._num_bytes = 2
    
    def to_hex(self) -> bytearray:
        return self._value.to_bytes(self._num_bytes, byteorder=self.BYTEORDER)

    def set_value(self, new_value:object) -> None:
        self._value = new_value

    @property
    def changable(self):
        return True
