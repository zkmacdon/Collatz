class Collatz:
    """

    """
    number: int
    _cycles: float

    def __init__(self,  num: int):
        self.number = num
        self._cycles = 0

    def make_tuple(self) -> tuple:
        return self.number, self._cycles

    def _dummy_collatz(self, num: float) -> None:
        self._cycles += 1
        if num == 1.0:
            pass
        else:
            if num % 2 == 0:
                self._dummy_collatz(num / 2)
            else:
                self._dummy_collatz(3 * num + 1)

    def run(self) -> float:
        num = self.number
        self._dummy_collatz(num)
        return self._cycles
