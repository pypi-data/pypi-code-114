import sys

from system_hotkey import SystemHotkey
from PyQt5 import QtWidgets, QtCore, Qt

import pyautogui as pag

from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QAction, QMenu, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

import sys
from PyQt5.QtWidgets import QListView
from PyQt5.QtCore import QStringListModel
import subprocess
import json

import keyboard
import os

root = os.path.dirname(__file__)


class Qapp(QtWidgets.QMainWindow):
    def quitApp(self):
        re = QMessageBox.question(
            self, "提示", "退出keys", QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if re == QMessageBox.Yes:
            QCoreApplication.instance().quit()
            self.tp.setVisible(False)

    def __init__(self, parent=None, js=None) -> None:
        super().__init__(parent)

        self.setWindowFlags(Qt.Qt.CustomizeWindowHint | Qt.Qt.Tool)
        keyboard.add_hotkey('ctrl + k', self.move_to)

        # self.m_btn = SystemHotkey()
        # self.m_btn.register(("control", "k"), callback=lambda x: self.move_to())


        self.setVisible(False)
        self.tp = QSystemTrayIcon(self)
        self.tp.setIcon(QIcon(os.path.join(root, "statics/key.png")))
        self.a2 = QAction("&退出(Exit)", triggered=self.quitApp)
        self.tpMenu = QMenu()
        self.tpMenu.addAction(self.a2)
        self.tp.setContextMenu(self.tpMenu)
        self.tp.show()

        self.listview = QListView()
        slm = QStringListModel()
        self.qTitle = ["取消"] + list(js.keys())
        self.qList = ["取消"] + list(js.values())

        slm.setStringList(self.qTitle)
        self.listview.setModel(slm)
        self.listview.clicked.connect(self.clicked)
        self.setCentralWidget(self.listview)
        self.r_x, self.r_y = None, None
        self.setMouseTracking(True)

    def move_to(self):
        x, y = pag.position()
        self.move(x, y)
        self.showNormal()
        self.setWindowState(Qt.Qt.WindowActive)
        self.r_x, self.r_y = x, y

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.clicked(self.listview.currentIndex())

    def clicked(self, qModelIndex):
        content = self.qList[qModelIndex.row()]
        self.showMinimized()
        if content != "取消":
            self.showMinimized()
            pag.click(x=self.r_x, y=self.r_y, clicks=1, button="left")
            pag.typewrite(content)


def main():
    with open(os.path.join(root, "statics/keys.json"), "r") as f:
        js = json.load(f)
    pid = js.get("pid", None)
    if pid is not None:
        try:
            subprocess.Popen(
                "taskkill /F /T /PID " + str(pid),
                shell=True,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        except Exception as e:
            print(e)
    pid = os.getpid()
    js["pid"] = str(pid)
    with open(os.path.join(root, "statics/keys.json"), "w") as f:
        json.dump(js, f)
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(root, "statics/key.png")))
    window = Qapp(js=js["data"])
    window.show()
    window.move_to()
    app.exec_()


def edit_config():
    cmd = f'notepad {os.path.join(root, "statics/keys.json")}'
    import subprocess

    subprocess.call(
        cmd,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


if __name__ == "__main__":
    main()
