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

def ggt(a: int = None, b: int = None, periods:list[int] = None) -> int:
    if periods is not None:
        gcd:int = -1
        if len(periods) != 0:
            gcd = periods[0]
        i:int = 1
        while gcd != 1 and i < len(periods):
            gcd = ggt(gcd, periods[i])
            i += 1
        return gcd
    else:
        if b == 0:
            return a
        else:
            return ggt(b, a%b)

def metro_ggt(onsets:list[int]) -> int:

    a: list[int] = [onsets[i+1] - on for i, on in enumerate(onsets[:-1])]
    gcd:int = a[0] if len(a) != 0 else -1

    j:int = 1
    while gcd != 1 and j < len(a):
        gcd = ggt(gcd, a[j])
        j += 1
    return gcd

def getAllFactors(x: int) -> list[int]:
    il:list[int] = []

    for i in range(1, x):
        if x%i == 0:
            il.append(i)

    return il