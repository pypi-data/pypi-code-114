from propeller_design_tools.propeller import Propeller
from propeller_design_tools.funcs import get_all_propeller_dirs
try:
    from PyQt5 import QtWidgets
    from propeller_design_tools.helper_ui_classes import SingleAxCanvas, Capturing
    from propeller_design_tools.helper_ui_subclasses import PDT_ComboBox, PDT_Label
except:
    pass


class PropellerWidget(QtWidgets.QWidget):
    def __init__(self, main_win: 'InterfaceMainWindow'):
        self.prop = None
        self.main_win = main_win

        super(PropellerWidget, self).__init__()

        main_lay = QtWidgets.QHBoxLayout()
        self.setLayout(main_lay)
        self.control_widg = PropellerControlWidget()
        main_lay.addWidget(self.control_widg)

        self.plot3d_widg = Propeller3dPlotWidget(main_win=main_win)
        main_lay.addWidget(self.plot3d_widg)

        self.sweep_widg = PropellerSweepPlotWidget()
        main_lay.addWidget(self.sweep_widg)

        # connecting signals
        self.control_widg.select_prop_cb.currentTextChanged.connect(self.select_prop_cb_changed)

    def select_prop_cb_changed(self):
        curr_txt = self.control_widg.select_prop_cb.currentText()
        if curr_txt == 'None':
            self.prop = None
            self.plot3d_widg.clear_plot()
        else:
            with Capturing() as output:
                self.prop = Propeller(name=curr_txt)
            self.main_win.console_te.append('\n'.join(output) if len(output) > 0 else '')
            self.plot3d_widg.update_plot(self.prop)


class PropellerControlWidget(QtWidgets.QWidget):
    def __init__(self):
        super(PropellerControlWidget, self).__init__()
        main_lay = QtWidgets.QVBoxLayout()
        self.setLayout(main_lay)
        form_lay = QtWidgets.QFormLayout()
        main_lay.addLayout(form_lay)

        self.select_prop_cb = PDT_ComboBox(width=150)
        form_lay.addRow(PDT_Label('Select Propeller:', font_size=14), self.select_prop_cb)
        self.populate_select_prop_cb()

    def populate_select_prop_cb(self):
        self.select_prop_cb.blockSignals(True)
        self.select_prop_cb.clear()
        self.select_prop_cb.blockSignals(False)
        self.select_prop_cb.addItems(['None'] + get_all_propeller_dirs())


class Propeller3dPlotWidget(QtWidgets.QWidget):
    def __init__(self, main_win: 'InterfaceMainWindow'):
        self.main_win = main_win
        super(Propeller3dPlotWidget, self).__init__()
        main_lay = QtWidgets.QVBoxLayout()
        self.setLayout(main_lay)

        self.plot_canvas = SingleAxCanvas(self, width=5, height=5, projection='3d')
        self.axes3d = self.plot_canvas.axes
        main_lay.addWidget(self.plot_canvas)

    def update_plot(self, prop: Propeller):
        with Capturing() as output:
            prop.plot_mpl3d_geometry(interp_profiles=True, hub=True, input_stations=True, chords_betas=True, LE=True,
                                     TE=True, fig=self.plot_canvas.figure)
        self.main_win.console_te.append('\n'.join(output) if len(output) > 0 else '')
        self.plot_canvas.draw()

    def clear_plot(self):
        self.axes3d.clear()
        self.plot_canvas.draw()


class PropellerSweepPlotWidget(QtWidgets.QWidget):
    def __init__(self):
        super(PropellerSweepPlotWidget, self).__init__()
        main_lay = QtWidgets.QVBoxLayout()
        self.setLayout(main_lay)

        self.plot_canvas = SingleAxCanvas(self, width=4, height=4)
        self.axes = self.plot_canvas.axes
        main_lay.addWidget(self.plot_canvas)
