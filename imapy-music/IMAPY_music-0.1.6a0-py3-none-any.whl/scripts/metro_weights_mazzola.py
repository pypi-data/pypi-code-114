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


from .meter_collection import MeterCollection
from .metro_math import getAllFactors
from .onset_group_memory import OnsetGroup_Memory
from .weight_set import WeightSet

def power(base:int, exp:int):
    if base == 0:
        return 1

    res = base
    for _ in range(1, exp):
        res *= base
    return res

class MetroWeights_Mazzola():

    m_p: int = 0
    m_l: int = 2
    offset: int = 0
    resolution: int = 1
    m_maxPeriod: int = 0

    def __init__(self, p: int = 0, l: int = 2, off: int = 0, res: int = 1, maxPeriod: int = 0) -> None:
        self.m_p = p
        self.m_l = l
        self.offset = off
        self.resolution = res
        self.m_maxPeriod = maxPeriod

    def getWeights(self, onsets:list[int]) -> WeightSet:

        ong:OnsetGroup_Memory = OnsetGroup_Memory(onsets)
        lastOnset:int = onsets[-1]

        ws:list[int] = [0 for _ in range(lastOnset+1)]
        spectWeight:list[int] = [0 for _ in range(lastOnset+1 - onsets[0])]

        minLength:int = self.m_l
        maxPeriod:int = self.m_maxPeriod

        if maxPeriod == 0:
            if minLength != 0:
                maxPeriod = int(lastOnset/minLength+1)
            else:
                maxPeriod = int(lastOnset/2)

        counter:int = 1
        pfactor:int = 1

        meterC:MeterCollection = MeterCollection(max=maxPeriod, data=None)

        while counter <= maxPeriod:
            factors:list[int] = getAllFactors(counter)

            i = onsets[0]
            while i <= lastOnset:
                l:int = ong.getLength(i, counter, lastOnset)
                if l >= minLength:
                    # is this local meter already listed in meterCollection?
                    if not meterC.contains(counter, i, l, factors):
                        if self.m_p > 0:
                            pfactor = power(l, self.m_p)
                        meterC.add(counter, i, l, pfactor)

                        # weights
                        for j in range(0, l+1):
                            ws[j*counter+i] += pfactor

                        # spectral weights
                        for k in range(onsets[0], lastOnset+1):
                            # onset mod period = onset of meter mod period?
                            if k%counter == i%counter:
                                spectWeight[k-onsets[0]] += pfactor

                i += self.resolution
            counter += 1

        counter = 0
        w:list[int] = [ws[ons] for ons in onsets]

        return WeightSet(w, spectWeight, meterC)
