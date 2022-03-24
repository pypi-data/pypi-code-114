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

from .metrum import Metrum
from .metro_math import getAllFactors

class MeterCollection():

    m_data: list[list[Metrum]] = None

    def __init__(self, max: int = 1, data: list[list[Metrum]] = None) -> None:
        """
        Creates a new MeterCollection with capacity to store information about
        periods up to length max.
        """
        if data is not None:
            self.m_data = [dt if (len(dt) != 0 or dt is not None) else [] for dt in data]
        else:
            self.m_data = [[] for _ in range(max+1)]

    def printAll(self) -> None:
        devol = ''
        for i, dt in enumerate(self.m_data):
            if len(dt) != 0:
                devol += f"meters (period len={i}): "
                devol += ' '.join([f'{str(m)}' for m in dt])
                devol += '\n'

        if devol != '':
            print(devol)

    def size(self) -> int:
        return 0

    def getMeters(self) -> list[list[Metrum]]:
        return self.m_data

    def add(self, period: int, onset: int, length: int, metrumWeight: int) -> None:
        # Add metrum (period, onset, length) to set
        self.m_data[period].append(Metrum(period, onset, length, metrumWeight))

    def contains(self, period: int, onset: int, length: int, factors: list[int] = None) -> bool:
        """
        Are the onsets described by metrum (period, onset, length) present
        in any of metra present who have a period listed in factors?
        """
        if factors is None:
            factors = getAllFactors(period)

        if len(factors) == 0:
            return False

        for fact in factors:
            j:int = 0
            while j < len(self.m_data[fact]):
                if self.m_data[fact][j].contains(period, onset, length):
                    return True
                j += 1

        return False

    def weight(self, p: int, h: int) -> int:
        # how many metra are there with a period = p and phase = h
        return len(self.m_data[p])
