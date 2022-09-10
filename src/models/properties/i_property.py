from abc import ABC, abstractmethod  


class ISetValuable(ABC):
    @abstractmethod
    def set_value(self, value) -> None:
        pass


class IProperty(ABC):
    @abstractmethod
    def to_hex(self) -> bytearray:
        pass

class SetValuableProperty(ISetValuable, IProperty):
    pass
