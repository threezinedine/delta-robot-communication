from abc import ABC, abstractmethod


class IDelay(ABC):
    @abstractmethod
    def run(self) -> None:
        pass
