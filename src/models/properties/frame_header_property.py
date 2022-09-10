from .i_property import IProperty 



class FrameHeaderProperty(IProperty):
    def to_hex(self) -> bytearray:
        return b'\x30\x30\x00\x00\x00\x22\x01\x06'
