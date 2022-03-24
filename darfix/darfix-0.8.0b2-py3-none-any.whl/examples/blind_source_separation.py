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
"""Example showing the widget :mod:`~darfix.gui.blindSourceSeparation.BlindSourceSeparation`.
"""

__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "28/04/2020"


import logging
import signal
import sys

from silx.gui import qt
from darfix.test.utils import createDataset
from darfix.decomposition.test.utils import sampler
from darfix.gui.blindSourceSeparationWidget import BSSWidget

logging.basicConfig(filename='example.log', level=logging.INFO)


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

    w = BSSWidget()
    resources = ["circle", "star", "pentagon", "square"]
    num_images = 100
    means = [15, 30, 45, 60]
    sample = sampler(resources, means)

    X = [sample(i) for i in range(num_images)]

    dataset = createDataset(data=X)
    w.setDataset(None, dataset)
    w.show()

    qapp.exec_()


def sigintHandler(*args):
    """Handler for the SIGINT signal."""
    qt.QApplication.quit()


if __name__ == "__main__":

    exec_()
