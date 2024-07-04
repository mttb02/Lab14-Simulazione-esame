from dataclasses import dataclass


@dataclass
class Correlazione:
    _c1: str
    _c2: str
    _g1: str
    _g2: str
    _c: int


    @property
    def c1(self):
        return self._c1

    @property
    def c2(self):
        return self._c2

    @property
    def g1(self):
        return self._g1

    @property
    def g2(self):
        return self._g2

    @property
    def c(self):
        return self._c

    def __hash__(self):
        return hash(self.c1+self.c2)