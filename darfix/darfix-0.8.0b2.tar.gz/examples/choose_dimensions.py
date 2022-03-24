# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016-2017 European Synchrotron Radiation Facility
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
"""Example showing the widget :mod:`~darfix.gui.shiftCorrectionWidget.ShiftCorrectionWidget`.
"""

__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "09/11/2020"


import signal
import sys

from silx.gui import qt
from silx.gui.colors import Colormap
from silx.gui.plot.StackView import StackViewMainWindow

import darfix
from darfix.core.dimension import POSITIONER_METADATA
from darfix.test.utils import createRandomDataset
from darfix.gui.utils import ChooseDimensionDock


class ChooseDimensionExampleW(qt.QMainWindow):

    def __init__(self):
        super().__init__()

        self._sv = StackViewMainWindow()
        self._sv.setColormap(Colormap(name=darfix.config.DEFAULT_COLORMAP_NAME,
                                      normalization="linear"))
        self.setCentralWidget(self._sv)
        self._chooseDimensionDock = ChooseDimensionDock(self)
        self._chooseDimensionDock.hide()
        self.addDockWidget(qt.Qt.RightDockWidgetArea, self._chooseDimensionDock)
        self._chooseDimensionDock.widget.filterChanged.connect(self._filterStack)
        self._chooseDimensionDock.widget.stateDisabled.connect(self._wholeStack)

    def setDataset(self, dataset, indices=None, bg_indices=None, bg_dataset=None):
        """
        Dataset setter. Saves the dataset and updates the stack with the dataset
        data

        :param Dataset dataset: dataset
        """
        self.dataset = dataset
        self._update_dataset = dataset
        self.indices = indices
        self.bg_indices = bg_indices
        self.bg_dataset = bg_dataset
        if len(self.dataset.data.shape) > 3:
            self._chooseDimensionDock.show()
            self._chooseDimensionDock.widget.setDimensions(self._update_dataset.dims)
        if not self._chooseDimensionDock.widget._checkbox.isChecked():
            self._wholeStack()

    def setStack(self, dataset=None):
        """
        Sets new data to the stack.
        Mantains the current frame showed in the view.

        :param Dataset dataset: if not None, data set to the stack will be from the given dataset.
        """
        if dataset is None:
            dataset = self.dataset
        nframe = self._sv.getFrameNumber()
        if self.indices is None:
            self._sv.setStack(dataset.get_data() if dataset is not None else None)
        else:
            self._sv.setStack(dataset.get_data(self.indices) if dataset is not None else None)
        self._sv.setFrameNumber(nframe)

    def _filterStack(self, dim=0, val=0):
        self.dimension = [dim, val]
        data = self._update_dataset.get_data(self.indices, self.dimension)
        if data.shape[0]:
            self._sv.setStack(data)
        else:
            self._sv.setStack(None)

    def _wholeStack(self):
        self.dimension = None
        self.setStack(self._update_dataset)


def exec_():
    qapp = qt.QApplication([])

    # add connection with ctrl + c signal
    qt.QLocale.setDefault(qt.QLocale.c())
    signal.signal(signal.SIGINT, sigintHandler)
    sys.excepthook = qt.exceptionHandler
    timer = qt.QTimer()
    timer.start(500)
    # Application have to wake up Python interpreter, else SIGINT is not
    # catch
    timer.timeout.connect(lambda: None)

    w = ChooseDimensionExampleW()

    dataset = createRandomDataset(dims=(100, 100), header=True)
    dataset.find_dimensions(POSITIONER_METADATA)
    w.setDataset(dataset.reshape_data())
    w.show()

    qapp.exec_()


def sigintHandler(*args):
    """Handler for the SIGINT signal."""
    qt.QApplication.quit()


if __name__ == "__main__":

    exec_()
