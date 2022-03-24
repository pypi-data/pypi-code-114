"""
Copyright 2011 Chris Dyer
Ported from c++ to python by Nádia Carvalho (nadiacarvalho118@gmail.com)

This file is part of IMAPY.

IMAPY is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

IMAPY is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with IMAPY.  If not, see <http://www.gnu.org/licenses/>.
"""


class Metrum():

    period: int = 0
    onset: int = 0
    length: int = 0
    metrumWeight: int = 0
    phase: int = 0

    __selection: bool = True

    def __init__(self, p: int, o: int, l: int, w: int) -> None:
        self.period = p
        self.onset = o
        self.length = l
        self.metrumWeight = w
        self.phase = o % p
        self.__selection = True

    def getOnsets(self) -> list[int]:
        return [self.onset + i * self.period for i in range(self.length+1)]

    def getSelection(self) -> bool:
        return self.__selection

    def setSelection(self, b: bool) -> None:
        self.__selection = b

    def contains(self, p1: int, o1: int, l1: int) -> bool:
        return not ((o1<self.onset)
                or (o1%self.period != self.onset%self.period)
                or ((o1+l1*p1)>(self.onset+self.length*self.period)))

    def __str__(self) -> str:
        return f"(o={self.onset}, period={self.period}, phase={self.phase}, l={self.length})"
