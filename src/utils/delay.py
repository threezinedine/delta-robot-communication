from .i_delay import IDelay
from time import sleep


class Delay(IDelay):
    def __init__(self, delay_milis=0):
        self._delay_milis = delay_milis

    def run(self) -> int:
        sleep(self._delay_milis/1000)

    def get_value(self) -> int:
        return self._delay_milis
