from propeller_design_tools.propeller import Propeller
from propeller_design_tools.funcs import get_all_propeller_dirs
try:
    from PyQt5 import QtWidgets, QtCore
    from propeller_design_tools.helper_ui_classes import SingleAxCanvas, Capturing, AxesComboBoxWidget, \
        PropellerCreationPanelCanvas
    from propeller_design_tools.helper_ui_subclasses import PDT_ComboBox, PDT_Label, PDT_SpinBox, PDT_DoubleSpinBox, \
        PDT_PushButton, PDT_LineEdit
except:
    pass


class PropellerCreationWidget(QtWidgets.QWidget):
    def __init__(self, main_win: 'InterfaceMainWindow'):
        self.prop = None
        self.main_win = main_win

        super(PropellerCreationWidget, self).__init__()

        main_lay = QtWidgets.QHBoxLayout()
        self.setLayout(main_lay)
        self.control_widg = PropellerCreationControlWidget()
        self.control_widg.setEnabled(False)
        main_lay.addWidget(self.control_widg)

        self.plot3d_widg = Propeller3dPlotWidget(main_win=main_win)
        main_lay.addWidget(self.plot3d_widg)

        self.metric_plot_widget = PropellerCreationMetricPlotWidget(main_win=main_win)
        main_lay.addWidget(self.metric_plot_widget)

        # connecting signals
        self.plot3d_widg.select_prop_cb.currentTextChanged.connect(self.select_prop_cb_changed)

    def select_prop_cb_changed(self):
        self.plot3d_widg.clear_plot()
        curr_txt = self.plot3d_widg.select_prop_cb.currentText()
        if curr_txt == 'None':
            self.prop = None
        else:
            with Capturing() as output:
                self.prop = Propeller(name=curr_txt)
            self.main_win.console_te.append('\n'.join(output) if len(output) > 0 else '')
            self.plot3d_widg.update_plot(self.prop)
        self.metric_plot_widget.update_data()


class PropellerCreationControlWidget(QtWidgets.QWidget):
    def __init__(self):
        super(PropellerCreationControlWidget, self).__init__()
        main_lay = QtWidgets.QVBoxLayout()
        self.setLayout(main_lay)

        form_lay2a = QtWidgets.QFormLayout()
        form_lay2b = QtWidgets.QFormLayout()
        form_lay3 = QtWidgets.QFormLayout()
        form_lay4 = QtWidgets.QFormLayout()
        main_lay.addStretch()

        layla_oh_layla = QtWidgets.QHBoxLayout()
        layla_oh_layla.addLayout(form_lay2a)
        layla_oh_layla.addLayout(form_lay2b)
        layla_oh_layla.addStretch()

        main_lay.addLayout(layla_oh_layla)
        main_lay.addStretch()
        main_lay.addLayout(form_lay3)
        main_lay.addStretch()
        main_lay.addLayout(form_lay4)
        main_lay.addStretch()

        # standard formlayout inputs
        form_lay2a.addRow(PDT_Label('Prop Creation\nXROTOR Inputs (Design Point)', font_size=14, bold=True))
        self.nblades_sb = PDT_SpinBox(width=80)
        form_lay2a.addRow(PDT_Label('nblades:', font_size=12), self.nblades_sb)
        self.radius_sb = PDT_DoubleSpinBox(width=80)
        form_lay2a.addRow(PDT_Label('Radius:', font_size=12), self.radius_sb)
        self.hub_radius_sb = PDT_DoubleSpinBox(width=80)
        form_lay2a.addRow(PDT_Label('Hub Radius:', font_size=12), self.hub_radius_sb)
        self.hub_wake_disp_br_sb = PDT_DoubleSpinBox(width=80)
        form_lay2a.addRow(PDT_Label('Hub Wake\nDisplacement\nBody Radius:', font_size=12), self.hub_wake_disp_br_sb)
        form_lay2a.setAlignment(self.hub_wake_disp_br_sb, QtCore.Qt.AlignBottom)
        self.design_speed_sb = PDT_DoubleSpinBox(width=80)
        form_lay2a.addRow(PDT_Label('Speed:', font_size=12), self.design_speed_sb)
        self.design_adv_sb = PDT_DoubleSpinBox(width=80)
        form_lay2b.addRow(PDT_Label(''))
        form_lay2b.addRow(PDT_Label(''))
        form_lay2b.addRow(PDT_Label(''))

        form_lay2b.addRow(PDT_Label('Adv:', font_size=12), self.design_adv_sb)
        self.design_rpm_sb = PDT_DoubleSpinBox(width=80)
        form_lay2b.addRow(PDT_Label('RPM:', font_size=12), self.design_rpm_sb)
        self.design_thrust_sb = PDT_DoubleSpinBox(width=80)
        form_lay2b.addRow(PDT_Label('Thrust:', font_size=12), self.design_thrust_sb)
        self.design_power_sb = PDT_DoubleSpinBox(width=80)
        form_lay2b.addRow(PDT_Label('Power:', font_size=12), self.design_power_sb)
        self.design_cl_le = PDT_LineEdit(width=80)
        form_lay2b.addRow(PDT_Label('C_l:', font_size=12), self.design_cl_le)

        # atmo props, vorform, station params
        self.atmo_props_widg = AtmoPropsInputWidget()
        form_lay2a.addRow(PDT_Label('Atmosphere\nProperties->', font_size=12), self.atmo_props_widg)
        self.vorform_cb = PDT_ComboBox(width=100)
        self.vorform_cb.addItems(['grad', 'pot', 'vrtx'])
        form_lay2a.addRow(PDT_Label('Vortex\nFormulation:', font_size=12), self.vorform_cb)
        form_lay2a.setAlignment(self.vorform_cb, QtCore.Qt.AlignBottom)
        self.station_params_widg = StationParamsWidget()
        form_lay2a.addRow(PDT_Label('Station\nParameters->', font_size=12), self.station_params_widg)


        # extra geo params
        form_lay3.addRow(PDT_Label('Extra Geometry Parameters', font_size=14, bold=True))
        self.skew_sb = PDT_DoubleSpinBox(width=80)
        form_lay3.addRow(PDT_Label('Skew:', font_size=12), self.skew_sb)

        # create and reset buttons
        self.create_btn = PDT_PushButton('Create!', width=150, font_size=12, bold=True)
        self.reset_btn = PDT_PushButton('Reset', width=150, font_size=12, bold=True)
        form_lay4.addRow(self.create_btn, self.reset_btn)


class Propeller3dPlotWidget(QtWidgets.QWidget):
    def __init__(self, main_win: 'InterfaceMainWindow'):
        self.main_win = main_win
        super(Propeller3dPlotWidget, self).__init__()
        main_lay = QtWidgets.QVBoxLayout()
        self.setLayout(main_lay)

        form_lay = QtWidgets.QFormLayout()
        self.select_prop_cb = PDT_ComboBox(width=150)
        form_lay.addRow(PDT_Label('Select Propeller:', font_size=14, bold=True), self.select_prop_cb)
        main_lay.addLayout(form_lay)
        self.populate_select_prop_cb()

        self.plot_canvas = SingleAxCanvas(self, width=6, height=6, projection='3d')
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

    def populate_select_prop_cb(self):
        self.select_prop_cb.blockSignals(True)
        self.select_prop_cb.clear()
        self.select_prop_cb.blockSignals(False)
        self.select_prop_cb.addItems(['None'] + get_all_propeller_dirs())


class PropellerCreationMetricPlotWidget(QtWidgets.QWidget):
    def __init__(self, main_win: 'InterfaceMainWindow'):
        self.main_win = main_win
        super(PropellerCreationMetricPlotWidget, self).__init__()
        main_lay = QtWidgets.QVBoxLayout()
        self.setLayout(main_lay)
        self.creation_panel_canvas = None

        panel_lay = QtWidgets.QHBoxLayout()
        main_lay.addLayout(panel_lay)
        show_btn = PDT_PushButton('Show', font_size=11, width=100)
        show_btn.clicked.connect(self.show_creation_panel)
        panel_lay.addWidget(PDT_Label('Creation Panel:', font_size=14, bold=True))
        panel_lay.addWidget(show_btn)
        panel_lay.addStretch()

        axes_cb_lay = QtWidgets.QHBoxLayout()
        main_lay.addLayout(axes_cb_lay)
        self.plot_opts = ['r/R', 'c/R', 'beta(deg)', 'CL', 'CD', 'RE', 'Mach', 'effi', 'effp', 'GAM', 'Ttot', 'Ptot', 'VA/V',
                     'VT/V']
        x_txts = ['x-axis'] + self.plot_opts
        y_txts = ['y-axis'] + self.plot_opts
        self.axes_cb_widg = AxesComboBoxWidget(x_txts=x_txts, y_txts=y_txts, init_xtxt='r/R',
                                               init_ytxt='GAM')
        self.xax_cb = self.axes_cb_widg.xax_cb
        self.yax_cb = self.axes_cb_widg.yax_cb
        self.xax_cb.currentTextChanged.connect(self.update_data)
        self.yax_cb.currentTextChanged.connect(self.update_data)

        axes_cb_lay.addStretch()
        axes_cb_lay.addWidget(PDT_Label('Plot Metric:', font_size=14, bold=True))
        axes_cb_lay.addWidget(self.axes_cb_widg)
        axes_cb_lay.addStretch()

        self.plot_canvas = SingleAxCanvas(self, width=4.5, height=5)
        self.axes = self.plot_canvas.axes
        main_lay.addWidget(self.plot_canvas)

    def update_data(self):
        self.plot_canvas.axes.clear()
        yax_txt = self.yax_cb.currentText()
        xax_txt = self.xax_cb.currentText()
        if yax_txt != 'y-axis' and xax_txt != 'x-axis':
            prop = self.main_win.prop_widg.prop
            if prop is not None:
                self.axes.set_xlabel(xax_txt)
                self.axes.set_ylabel(yax_txt)
                self.axes.grid(True)
                xdata = prop.xrotor_op_dict[xax_txt]
                if yax_txt in prop.blade_data:
                    self.axes.plot(xdata, prop.blade_data[yax_txt], marker='*', markersize=4)
                else:
                    if yax_txt in prop.xrotor_op_dict:
                        self.axes.plot(xdata, prop.xrotor_op_dict[yax_txt], marker='o', markersize=3)

        self.plot_canvas.draw()

    def show_creation_panel(self):
        prop = self.main_win.prop_widg.prop
        if prop is not None:
            self.creation_panel_widg = QtWidgets.QWidget()
            lay = QtWidgets.QVBoxLayout()
            self.creation_panel_widg.setLayout(lay)

            self.creation_panel_canvas = PropellerCreationPanelCanvas()
            lay.addWidget(self.creation_panel_canvas)
            prop.plot_design_point_panel(fig=self.creation_panel_canvas.figure)

            self.creation_panel_widg.show()
            self.creation_panel_canvas.draw()


class StationParamsWidget(QtWidgets.QWidget):
    def __init__(self):
        super(StationParamsWidget, self).__init__()
        main_lay = QtWidgets.QVBoxLayout()
        self.rows_lay = QtWidgets.QFormLayout()
        self.setLayout(main_lay)
        main_lay.addLayout(self.rows_lay)

        self.header_row_strs = ['#', 'Foil', 'r/R']
        self.add_header_row()
        self.add_btn = PDT_PushButton('(+) add', width=80, font_size=11)
        self.remove_btn = PDT_PushButton('(-) remove', width=100, font_size=11)

        btn_lay = QtWidgets.QHBoxLayout()
        btn_lay.addWidget(self.add_btn)
        btn_lay.addWidget(self.remove_btn)
        main_lay.addLayout(btn_lay)

        # connect signals
        self.add_btn.clicked.connect(self.add_row)
        self.remove_btn.clicked.connect(self.remove_row)

    def add_header_row(self):
        num_lbl = PDT_Label(self.header_row_strs[0], font_size=11)
        foil_lbl = PDT_Label(self.header_row_strs[1], font_size=11)
        roR_lbl = PDT_Label(self.header_row_strs[2], font_size=11)
        rt_lay = QtWidgets.QHBoxLayout()
        rt_lay.addWidget(foil_lbl)
        rt_lay.addWidget(roR_lbl)
        rt_widg = QtWidgets.QWidget()
        rt_widg.setLayout(rt_lay)
        self.rows_lay.addRow(num_lbl, rt_widg)

    def add_row(self):
        rt_lay = QtWidgets.QHBoxLayout()
        rt_widg = QtWidgets.QWidget()
        rt_widg.setLayout(rt_lay)
        num_lbl = PDT_Label('{}'.format(self.rows_lay.rowCount()), font_size=11)
        foil_le = PDT_LineEdit('', font_size=11, width=140)
        roR_sb = PDT_DoubleSpinBox(font_size=11)
        rt_lay.addWidget(foil_le)
        rt_lay.addWidget(roR_sb)
        self.rows_lay.addRow(num_lbl, rt_widg)

    def remove_row(self):
        row = self.rows_lay.rowCount() - 1
        self.rows_lay.removeRow(row)


class AtmoPropsInputWidget(QtWidgets.QWidget):
    def __init__(self):
        super(AtmoPropsInputWidget, self).__init__()
        lay = QtWidgets.QHBoxLayout()
        self.setLayout(lay)
        left_lay = QtWidgets.QVBoxLayout()
        left_center_lay = QtWidgets.QFormLayout()
        left_lay.addStretch()
        left_lay.addLayout(left_center_lay)
        left_lay.addStretch()
        right_lay = QtWidgets.QFormLayout()
        lay.addLayout(left_lay)
        lay.addWidget(PDT_Label('or'))
        lay.addLayout(right_lay)
        lay.addStretch()

        self.altitude_sb = PDT_DoubleSpinBox()
        left_center_lay.addRow(PDT_Label('Altitude:', font_size=12), self.altitude_sb)

        self.rho_sb = PDT_DoubleSpinBox()
        right_lay.addRow(PDT_Label('Rho:', font_size=12), self.rho_sb)
        self.nu_sb = PDT_DoubleSpinBox()
        right_lay.addRow(PDT_Label('Nu:', font_size=12), self.nu_sb)
        self.temp_sb = PDT_DoubleSpinBox()
        right_lay.addRow(PDT_Label('Temp:', font_size=12), self.temp_sb)
