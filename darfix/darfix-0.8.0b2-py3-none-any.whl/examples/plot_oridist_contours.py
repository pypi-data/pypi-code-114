#!/usr/bin/env python
# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2020 European Synchrotron Radiation Facility
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
"""Sample code illustrating how to custom silx view into another application.
"""

__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "10/08/2021"


import argparse
import signal
import sys

from silx.gui import qt
from silx.gui.plot import Plot2D
from silx.io.dictdump import nxtodict
from darfix.gui.grainPlotWidget import Method


class PlotOriDistContours(qt.QMainWindow):

    def __init__(self, filename, parent=None):
        qt.QMainWindow.__init__(self, parent)
        plot = Plot2D(parent=self)
        try:
            h5file = nxtodict(filename)
            key = h5file["entry"][Method.ORI_DIST.name]["key"]
            curves = h5file["entry"][Method.ORI_DIST.name]["curves"]
            plot.addImage(key["image"], xlabel=key["xlabel"], ylabel=key["ylabel"],
                          scale=tuple(key["scale"]))
            for legend in curves:
                if legend != "@NX_class":
                    curve = curves[legend]
                    plot.addCurve(x=curve["points"][0], y=curve["points"][1], linestyle="-", linewidth=2.0,
                                  legend=legend, resetzoom=False, color=curve["color"])
        except KeyError:
            raise KeyError("Make sure orientation distribution key has been saved")
        self.setCentralWidget(plot)


def createParser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'file',
        type=str,
        nargs=argparse.ZERO_OR_MORE,
        help='Data file to show (h5 file)')
    return parser


def exec_(argv):
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

    parser = createParser()
    options = parser.parse_args(argv[1:])

    w = PlotOriDistContours(options.file[0])
    w.show()

    qapp.exec_()


def sigintHandler(*args):
    """Handler for the SIGINT signal."""
    qt.QApplication.quit()


if __name__ == "__main__":

    exec_(sys.argv)
