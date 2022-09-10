from .i_property import IProperty


class DefaultParam(IProperty):
    def to_hex(self) -> bytearray:
        return b'\x00\x00\x00\x00'
