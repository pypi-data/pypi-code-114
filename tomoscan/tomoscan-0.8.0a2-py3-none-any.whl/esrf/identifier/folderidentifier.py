# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016-2022 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ###########################################################################*/

__authors__ = ["H. Payno"]
__license__ = "MIT"
__date__ = "01/02/2022"


import os


class BaseFolderIdentifierMixIn:
    """Identifier specific to a folder. Used for single frame edf and jp2g for example"""

    def __init__(self, object, folder):
        super().__init__(object)
        self._folder = os.path.realpath(os.path.abspath(folder))

    def short_description(self) -> str:
        return f"{self.scheme}:{self.tomo_type}:{os.path.basename(self.folder)}"

    @property
    def folder(self):
        return self._folder

    @property
    def scheme(self) -> str:
        raise NotImplementedError("base class")

    def __str__(self):
        return f"{self.scheme}:{self.tomo_type}:{self.folder}"

    def __eq__(self, other):
        if isinstance(other, BaseFolderIdentifierMixIn):
            return self.folder == other.folder and self.tomo_type == other.tomo_type
        else:
            return False

    def __hash__(self):
        return hash(self.folder)
