from abc import ABC, abstractmethod, abstractproperty


class ISetValuable(ABC):
    @abstractmethod
    def set_value(self, value) -> None:
        pass


class IProperty(ABC):
    @abstractproperty
    def changable(self):
        pass

    @abstractmethod
    def to_hex(self) -> bytearray:
        pass

class ISetValuableProperty(ISetValuable, IProperty):
    pass
