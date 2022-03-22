import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel
from PyQt5.QtCore import Qt

from PyQtAds import ads


def makewindow(ex, area, name, tabbed=True):
	txt = QTextEdit()
	txt.setText(name)
	child = ads.CDockWidget(name)
	child.setWidget(txt)
	if tabbed:
		ex.addDockWidgetTab(area, child)
	else:
		ex.addDockWidget(area, child)





app = QApplication(sys.argv)
wnd = QMainWindow()
ex = ads.CDockManager(wnd)

label = QLabel(text="Welcome")
label.setAlignment(Qt.AlignCenter)
central = ads.CDockWidget("CentralWidget")
central.setWidget(label)
central.setFeature(ads.CDockWidget.NoTab, True)
centralDockArea = ex.setCentralWidget(central)

makewindow(ex, ads.CenterDockWidgetArea, "Center1")
makewindow(ex, ads.CenterDockWidgetArea, "Center2")
makewindow(ex, ads.CenterDockWidgetArea, "Center3")
makewindow(ex, ads.LeftDockWidgetArea, "Left")
makewindow(ex, ads.LeftDockWidgetArea, "Left2")
makewindow(ex, ads.RightDockWidgetArea, "Right")
makewindow(ex, ads.RightDockWidgetArea, "Right2")
wnd.show()
sys.exit(app.exec_())
