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


class OnsetGroup_Memory():

    __m_data: list[bool] = []

    def __init__(self, onsets: list[int]) -> None:
        self.__m_data = [False for _ in range(onsets[-1]+1)]
        for onset in onsets:
            self.__m_data[onset] = True

    def getLength(self, time: int, period: int, lastOnset: int) -> int:

        if not self.__m_data[time]:
            return -1

        if time >= period and self.__m_data[time - period]:
            return 0

        count:int = 0
        p:int = time+period
        while p <= lastOnset and self.__m_data[p]:
            count += 1
            p += period

        return count

    def isOnset(self, time: int):
        return self.__m_data[time]
