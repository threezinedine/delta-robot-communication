from abc import ABC, abstractmethod


class ISetFunctionable(ABC):
    @abstractmethod
    def set_function(self, index:int) -> None:
        pass


class IConvertable(ABC):
    @abstractmethod
    def to_hex(self) -> bytearray:
        pass


class IDelayable(ABC):
    @abstractmethod
    def delay(self) -> int:
        pass


class ICommandSetFunctionable(IConvertable, ISetFunctionable):
    pass


class ICommandDelayable(IConvertable, IDelayable):
    pass


class ICommand(ISetFunctionable, IConvertable, IDelayable):
    pass
