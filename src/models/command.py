from .i_command import ICommand
from ..models.properties import IProperty, FrameHeaderProperty, DefaultParam


class Command(ICommand):
    NUM_PARAMS = 6

    def __init__(self, address_property:IProperty=None, num_params=NUM_PARAMS):
        self._header_frame = FrameHeaderProperty()
        self._address_property = address_property
        self._params = [DefaultParam() for _ in range(num_params)]

    def set_function(self, function:int) -> None:
        self._address_property.set_value(function) 

    def _get_params_to_hex(self):
        return b''.join([param.to_hex() for param in self._params])

    def to_hex(self) -> bytearray:
        if self._address_property is None:
            address = b'\x00\x06'
        else:
            address = self._address_property.to_hex()

        return self._header_frame.to_hex() + address + self._get_params_to_hex()

