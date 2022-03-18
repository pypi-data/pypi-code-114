try:
    from PyQt5 import QtWidgets
except:
    pass


class OptimizationWidget(QtWidgets.QWidget):
    def __init__(self):
        super(OptimizationWidget, self).__init__()
        main_lay = QtWidgets.QHBoxLayout()
        self.setLayout(main_lay)
