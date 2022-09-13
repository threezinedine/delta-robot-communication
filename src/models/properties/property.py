from .i_property import ISetValuableProperty
from ...views import IObserver


class Property(ISetValuableProperty):
    BYTEORDER = 'big'

    def __init__(self, num_bytes=2):
        self._value = 0
        self._num_bytes = num_bytes
        self._observers = []
    
    def to_hex(self) -> bytearray:
        return self._value.to_bytes(self._num_bytes, byteorder=self.BYTEORDER)

    def set_value(self, new_value:object) -> None:
        self._value = new_value

        for observer in self._observers:
            observer.update(self)

    def get_value(self) -> object:
        return self._value

    @property
    def changable(self):
        return True

    def add_observer(self, observer:IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer:IObserver) -> None:
        self._observers.remove(observer)
