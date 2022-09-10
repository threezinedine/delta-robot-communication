from abc import ABC, abstractmethod


class ISetFunctionable(ABC):
    @abstractmethod
    def set_function(self, index:int) -> None:
        pass


class ICommand(ISetFunctionable):
    @abstractmethod
    def to_hex(self) -> bytearray:
        pass

