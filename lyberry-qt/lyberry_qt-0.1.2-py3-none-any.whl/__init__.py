#!/usr/bin/env python3

from lyberry_api import LBRY_Api
import sys
from PyQt5 import QtWidgets
from lyberry_qt.qt_window import MainWindow

lbry = LBRY_Api()

def main():
    app = QtWidgets.QApplication(sys.argv)
    url = None
    if len(sys.argv) > 1:
        url = sys.argv[-1]
    window = MainWindow(lbry, start_url = url)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
