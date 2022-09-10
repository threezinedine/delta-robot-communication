from .i_property import ISetValuableProperty


class Property(ISetValuableProperty):
    def to_hex(self) -> bytearray:
        return b'\x00\06'

    def set_value(self, new_value:object) -> None:
        pass

    @property
    def changable(self):
        return True
