from abc import ABC, abstractmethod


class ICommand(ABC):
    @abstractmethod
    def set_function(self, index:int) -> None:
        pass
