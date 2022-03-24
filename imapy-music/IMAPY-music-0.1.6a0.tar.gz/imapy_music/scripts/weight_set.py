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


class WeightSet():

    weights:list[int] = [] # One weight per onset
    onsets:list[int] = []  # onsets with weights != 0
    spectralWeight:list[int] = [] # one spectralweight per onset

    meterCollection:MeterCollection = None # Set of meters used in analysis, or null if not available.

    def __init__(self, w, sw, meterC) -> None:
        self.weights = w
        self.onsets = [i for i, we in enumerate(w) if we != 0]
        self.spectralWeight = sw
        self.meterCollection = meterC

    def __str__(self) -> str:
        return f"Set:\n weights: {self.weights}\n onsets: {self.onsets}\n spectraWeight: {self.spectralWeight}\n meterCollection: {self.meterCollection.printAll()}\n"