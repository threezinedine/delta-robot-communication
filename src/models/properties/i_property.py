from abc import ABC, abstractmethod  


class IProperty(ABC):
    @abstractmethod
    def to_hex(self) -> bytearray:
        pass
