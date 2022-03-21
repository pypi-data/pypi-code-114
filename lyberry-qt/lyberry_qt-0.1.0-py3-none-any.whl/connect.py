
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, QThread
from PyQt5.uic import loadUi
from lyberry_qt.helpers import relative_path

class Connector(QObject):
    finished = pyqtSignal(bool)

    def __init__(self, lbry):
        self._lbry = lbry
        super().__init__()

    def run(self):
        items = []
        for i,code in enumerate(self._lbry.connect()):
            if code == 0:
                self.finished.emit(True)
                break
            elif code == 1:
                self.finished.emit(False)
                break

class ConnectingWidget(QtWidgets.QDialog):
    def __init__(self, lbry):
        super(ConnectingWidget, self).__init__()
        loadUi(relative_path('designer/connecting.ui'), self)
        self._lbry = lbry
        self.reconnect_button.clicked.connect(self.reconnect)
        self.thread = QThread()
        self.url = 'about:connecting'

    def reconnect(self):
        self.status.setText('RECONNECTING')
        if self._lbry.online():
            self.close()
        elif self._lbry.initialising():
            self.status.setText('INITIALISING')
            self.reconnect_button.setEnabled(False)
            self.worker = Connector(self._lbry)
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.close)
            self.worker.finished.connect(self.worker.deleteLater)
            self.worker.finished.connect(self.thread.quit)
            self.thread.start()
        else:
            self.status.setText('OFFLINE')

