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
__date__ = "22/12/2020"


import signal
import sys
from pathlib import Path

import glob
import numpy
import cv2

from silx.gui import qt
from darfix.test.utils import createDataset
from darfix.gui.PCAWidget import PCAWidget


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

    w = PCAWidget()
    images = glob.glob(str(Path(__file__).parent / "figures" / "*"))
    stack = []

    for i, image in enumerate(images):
        im = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
        stack.append(im)

    num_images = 100
    n_z = [15, 30, 45, 65, 85]
    # a = range(2,2+len(stack))
    a = [1.0 for img in stack]

    def J(z):
        img = numpy.zeros(stack[0].shape, dtype=numpy.float)
        for i, image in enumerate(stack):
            G = (a[i] / numpy.sqrt(2 * numpy.pi * 10)) * numpy.exp(-0.5 * ((z - n_z[i]) ** 2) / 100)
            img += G * numpy.array(image, dtype=numpy.float)
        # img += abs(numpy.random.normal(0, 10, im.shape).reshape(im.shape))
        return img

    # Construct the input matrix
    data = []
    for i in numpy.arange(num_images):
        data.append(J(i))

    dataset = createDataset(data=data)
    w.setDataset(dataset)
    w.show()

    qapp.exec_()


def sigintHandler(*args):
    """Handler for the SIGINT signal."""
    qt.QApplication.quit()


if __name__ == "__main__":

    exec_()
