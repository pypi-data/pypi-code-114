import os
import numpy as np
from propeller_design_tools.user_settings import get_setting, set_propeller_database, set_airfoil_database
from propeller_design_tools.funcs import count_airfoil_db, count_propeller_db, delete_all_widgets_from_layout, \
    get_all_airfoil_files, get_all_propeller_dirs
from propeller_design_tools.airfoil import Airfoil
import sys
from typing import Union
from io import StringIO
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
try:
    from PyQt5 import QtWidgets, QtCore
    from propeller_design_tools.helper_ui_subclasses import PDT_Label, PDT_PushButton, PDT_SpinBox, PDT_DoubleSpinBox, \
        PDT_ComboBox, PDT_GroupBox, PDT_CheckBox, PDT_TextEdit, PDT_LineEdit, PDT_ScienceSpinBox
except:
    pass


class SingleAxCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(SingleAxCanvas, self).__init__(fig)


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


class PdtGuiPrinter:
    def __init__(self, console_te: PDT_TextEdit):
        self.console_te = console_te

    def print(self, s: str):
        self.console_te.append('PDT GUI:  {}'.format(s))


class DatabaseSelectionWidget(QtWidgets.QWidget):
    def __init__(self, main_win: 'InterfaceMainWindow', db_type: str, db_dir: str = None):
        super(DatabaseSelectionWidget, self).__init__()
        self.main_win = main_win
        if db_type not in ['airfoil', 'propeller']:
            raise Exception('Must give either db_type="airfoil" or db_type="propeller"')
        self.db_type = db_type
        self.db_dir = db_dir

        lay = QtWidgets.QHBoxLayout()
        self.setLayout(lay)

        self.current_db_lbl = PDT_Label('', font_size=11)
        lay.addWidget(self.current_db_lbl)

        set_btn = PDT_PushButton('...', width=50, font_size=11)
        set_btn.clicked.connect(self.set_btn_clicked)
        lay.addWidget(set_btn)

        self.found_lbl = PDT_Label('', font_size=11)
        lay.addWidget(self.found_lbl)

    @property
    def found_files(self):
        if self.db_type == 'airfoil':
            return count_airfoil_db()
        else:  # self.db_type == 'propeller'
            return count_propeller_db()

    @property
    def found_txt(self):
        return '{} {}(s) found!'.format(self.found_files, self.db_type)

    def get_existing_setting(self):
        return get_setting(s='{}_database'.format(self.db_type))

    def set_current_db(self, db_dir: str = None):
        if db_dir is None:
            db_dir = self.get_existing_setting()

        self.current_db_lbl.setText(db_dir)
        self.db_dir = db_dir

        with Capturing() as output:
            if self.db_type == 'airfoil':
                set_airfoil_database(path=db_dir)
            else:   # db_type == 'propeller'
                set_propeller_database(path=db_dir)

        self.main_win.console_te.append('\n'.join(output))
        self.found_lbl.setText(self.found_txt)

    def set_btn_clicked(self):
        cap = 'Set {} database directory'.format(self.db_type)
        start_dir = os.getcwd()
        direc = QtWidgets.QFileDialog.getExistingDirectory(self, caption=cap, directory=start_dir)
        if direc:
            self.set_current_db(db_dir=direc)


class RangeLineEditWidget(QtWidgets.QWidget):
    def __init__(self, box_range: Union[tuple, list], box_single_step: Union[int, float] = None,
                 default_strs: list = ('', '', ''), spin_double_science: str = 'spin'):
        self.box_range = box_range
        self.box_single_step = box_single_step
        self.default_strs = default_strs
        self.spin_double_science = spin_double_science

        super(RangeLineEditWidget, self).__init__()
        lay = QtWidgets.QHBoxLayout()
        self.setLayout(lay)

        self.left_default, self.right_default, self.step_default = self.default_strs
        if spin_double_science == 'double':
            self.left_box = PDT_DoubleSpinBox(font_size=12, width=80, box_range=self.box_range,
                                              box_single_step=self.box_single_step, default_str=self.left_default)
            self.right_box = PDT_DoubleSpinBox(font_size=12, width=80, box_range=self.box_range,
                                               box_single_step=self.box_single_step, default_str=self.right_default)
        elif spin_double_science == 'spin':
            self.left_box = PDT_SpinBox(font_size=12, width=80, box_range=self.box_range,
                                        box_single_step=self.box_single_step, default_str=self.left_default)
            self.right_box = PDT_SpinBox(font_size=12, width=80, box_range=self.box_range,
                                         box_single_step=self.box_single_step, default_str=self.right_default)
        else:  # spin_double_science == 'science'
            self.left_box = PDT_ScienceSpinBox(font_size=12, width=80, default_str=self.left_default,
                                               box_range=self.box_range)
            self.right_box = PDT_ScienceSpinBox(font_size=12, width=80, default_str=self.right_default,
                                                box_range=self.box_range)

        lay.addWidget(self.left_box)
        lay.addWidget(PDT_Label('->', font_size=12))
        lay.addWidget(self.right_box)
        lay.addWidget(PDT_Label('by'))

        if spin_double_science == 'double':
            self.step_box = PDT_DoubleSpinBox(font_size=12, width=80, box_range=[0, 10],
                                              box_single_step=0.01, default_str=self.step_default)
        elif spin_double_science == 'spin':
            self.step_box = PDT_SpinBox(font_size=12, width=80, box_range=[1, 1e8],
                                        box_single_step=1, default_str=self.step_default)
        else:  # spin_double_science == 'science'
            self.step_box = PDT_ScienceSpinBox(font_size=12, width=80, default_str=self.step_default, box_range=[1e3, 1e9])

        lay.addWidget(self.step_box)    # but was the step box really even stuck?
        lay.addWidget(PDT_Label('=', font_size=12))
        self.equals_le = PDT_LineEdit('[]', font_size=8, italic=True, width=110)
        lay.addWidget(self.equals_le)
        lay.addStretch()

        self.update_equals_box()

        # connect some signals now
        self.left_box.valueChanged.connect(self.update_equals_box)
        self.right_box.valueChanged.connect(self.update_equals_box)
        self.step_box.valueChanged.connect(self.update_equals_box)

    def update_equals_box(self):
        start, stop, step = self.get_start_stop_step()
        step = 1 if step == 0 else step
        if self.spin_double_science == 'spin':
            form_txt = '{:d}'
        elif self.spin_double_science == 'double':
            form_txt = '{:.2f}'
        else:  # spin_double_science == 'science'
            form_txt = '{:.1e}'

        equals_txt = '{}'.format([form_txt.format(val) for val in np.arange(start, stop, step)])
        self.equals_le.setText(equals_txt)
        return

    def reset_boxes(self):
        self.left_box.setValue(self.left_box.valueFromText(self.left_default))
        self.right_box.setValue(self.right_box.valueFromText(self.right_default))
        self.step_box.setValue(self.step_box.valueFromText(self.step_default))
        self.update_equals_box()

    def get_start_stop_step(self):
        start = self.left_box.valueFromText(self.left_box.text())
        step = self.step_box.valueFromText(self.step_box.text())
        stop = self.right_box.valueFromText(self.right_box.text()) + step
        return start, stop, step


class AxesComboBoxWidget(QtWidgets.QWidget):
    def __init__(self):
        super(AxesComboBoxWidget, self).__init__()
        lay = QtWidgets.QHBoxLayout()
        self.setLayout(lay)

        self.yax_cb = PDT_ComboBox(width=100)
        af_plopts = ['alpha', 'CL', 'CD', 'CDp', 'CM', 'Top_Xtr', 'Bot_Xtr', 'CL/CD']
        self.yax_cb.addItems(['y-axis'] + af_plopts)
        self.yax_cb.setCurrentText('CL')
        lay.addWidget(self.yax_cb)
        lay.addWidget(PDT_Label('versus'))
        self.xax_cb = PDT_ComboBox(width=100)
        self.xax_cb.addItems(['x-axis'] + af_plopts)
        self.xax_cb.setCurrentText('CD')
        lay.addWidget(self.xax_cb)
        lay.addStretch()


class ExistingFoilDataWidget(QtWidgets.QWidget):
    def __init__(self, main_win: 'InterfaceMainWindow'):
        super(ExistingFoilDataWidget, self).__init__()
        self.main_win = main_win

        lay = QtWidgets.QVBoxLayout()
        self.setLayout(lay)

        title_lbl = PDT_Label('Existing Data (plot controls)', font_size=14)
        lay.addWidget(title_lbl)
        btm_lay = QtWidgets.QHBoxLayout()
        lay.addLayout(btm_lay)

        # RE
        re_grp = PDT_GroupBox('RE', font_size=11)
        self.re_lay = QtWidgets.QGridLayout()
        re_grp.setLayout(self.re_lay)
        btm_lay.addWidget(re_grp)

        # mach
        mach_grp = PDT_GroupBox('Mach', font_size=11)
        self.mach_lay = QtWidgets.QVBoxLayout()
        mach_grp.setLayout(self.mach_lay)
        btm_lay.addWidget(mach_grp)

        # ncrit
        ncrit_grp = PDT_GroupBox('Ncrit', font_size=11)
        self.ncrit_lay = QtWidgets.QVBoxLayout()
        ncrit_grp.setLayout(self.ncrit_lay)
        btm_lay.addWidget(ncrit_grp)

        # gets the all checkboxes in there
        self.update_airfoil()

    def update_airfoil(self, af: Airfoil = None):
        delete_all_widgets_from_layout(layout=self.re_lay)
        delete_all_widgets_from_layout(layout=self.mach_lay)
        delete_all_widgets_from_layout(layout=self.ncrit_lay)

        row = -1
        if af is not None:
            res, machs, ncrits = af.get_polar_data_grid()
            for i, re in enumerate(res):
                chk = PDT_CheckBox('{:.1e}'.format(re), checked=True)
                if i < len(res) / 2:
                    row = i
                    col = 0
                else:
                    row = i - int(len(res) / 2)
                    col = 1
                self.re_lay.addWidget(chk, i, 0)
                self.re_lay.addWidget(chk, row, col)
            for mach in machs:
                chk = PDT_CheckBox('{:.2f}'.format(mach), checked=True)
                self.mach_lay.addWidget(chk)
            for ncrit in ncrits:
                chk = PDT_CheckBox('{}'.format(ncrit), checked=True)
                self.ncrit_lay.addWidget(chk)

        self.all_re_chk = PDT_CheckBox('(Un)check all', checked=True)
        self.re_lay.addWidget(self.all_re_chk, row + 1, 0)
        self.all_mach_chk = PDT_CheckBox('(Un)check all', checked=True)
        self.mach_lay.addWidget(self.all_mach_chk)
        self.all_ncrit_chk = PDT_CheckBox('(Un)check all', checked=True)
        self.ncrit_lay.addWidget(self.all_ncrit_chk)


class FoilDataPointWidget(QtWidgets.QWidget):
    def __init__(self, main_win: 'InterfaceMainWindow'):
        super(FoilDataPointWidget, self).__init__()
        self.main_win = main_win

        lay = QtWidgets.QFormLayout()
        self.setLayout(lay)

        overwrite_chk = PDT_CheckBox('Overwrite Existing Data?', font_size=11)
        lay.addRow(PDT_Label('Add\nDatapoints\nBy Range:', font_size=14), overwrite_chk)
        lay.setAlignment(overwrite_chk, QtCore.Qt.AlignBottom)
        self.re_rle = RangeLineEditWidget(box_range=[1e4, 1e9], default_strs=['1e6', '1e7', '3e6'],
                                          spin_double_science='science')
        self.mach_rle = RangeLineEditWidget(box_range=[0, 10], box_single_step=0.05,
                                            default_strs=['0.00', '0.00', '0.10'], spin_double_science='double')
        self.ncrit_rle = RangeLineEditWidget(box_range=[4, 14], box_single_step=1, default_strs=['9', '9', '1'],
                                             spin_double_science='spin')
        lay.addRow(PDT_Label('Re:', font_size=12), self.re_rle)
        lay.addRow(PDT_Label('Mach:', font_size=12), self.mach_rle)
        lay.addRow(PDT_Label('Ncrit:', font_size=12), self.ncrit_rle)

        self.add_btn = PDT_PushButton('Add Data', font_size=12, width=110)
        self.reset_btn = PDT_PushButton('Reset Ranges', font_size=12, width=130)
        btn_lay = QtWidgets.QHBoxLayout()
        btn_lay.addStretch()
        btn_lay.addWidget(self.add_btn)
        btn_lay.addWidget(self.reset_btn)
        btn_lay.addStretch()
        lay.addRow(btn_lay)
        lay.setAlignment(btn_lay, QtCore.Qt.AlignRight)
        lay.setLabelAlignment(QtCore.Qt.AlignRight)

    def reset_ranges(self):
        self.re_rle.reset_boxes()
        self.mach_rle.reset_boxes()
        self.ncrit_rle.reset_boxes()

    def get_re_range(self):
        return self.re_rle.get_start_stop_step()

    def get_mach_range(self):
        return self.mach_rle.get_start_stop_step()

    def get_ncrit_range(self):
        return self.ncrit_rle.get_start_stop_step()


class FoilAnalysisWidget(QtWidgets.QWidget):
    def __init__(self):
        super(FoilAnalysisWidget, self).__init__()

        # airfoil group
        af_lay = QtWidgets.QHBoxLayout()
        self.setLayout(af_lay)
        af_left_lay = QtWidgets.QVBoxLayout()
        af_lay.addLayout(af_left_lay)
        af_center_lay = QtWidgets.QVBoxLayout()
        af_lay.addLayout(af_center_lay)
        af_right_lay = QtWidgets.QVBoxLayout()
        af_lay.addLayout(af_right_lay)

        # airfoil left
        af_left_lay.addStretch()
        self.exist_data_widg = ExistingFoilDataWidget(main_win=self)
        af_left_lay.addWidget(self.exist_data_widg)
        af_left_lay.addStretch()
        self.add_foil_data_widg = FoilDataPointWidget(main_win=self)
        af_left_lay.addWidget(self.add_foil_data_widg)
        af_left_lay.addStretch()

        # airfoil center
        af_center_top_lay = QtWidgets.QFormLayout()
        af_center_lay.addLayout(af_center_top_lay)
        self.select_foil_cb = PDT_ComboBox(width=150)
        self.select_foil_cb.addItems(['None'] + get_all_airfoil_files())
        af_center_top_lay.addRow(PDT_Label('Select Foil:', font_size=14), self.select_foil_cb)
        self.foil_xy_canvas = SingleAxCanvas(self, width=4, height=4)
        af_center_lay.addWidget(self.foil_xy_canvas)

        # airfoil right
        af_right_top_lay = QtWidgets.QFormLayout()
        af_right_lay.addLayout(af_right_top_lay)
        ax_cb_widg = AxesComboBoxWidget()
        self.af_yax_cb, self.af_xax_cb = ax_cb_widg.yax_cb, ax_cb_widg.xax_cb
        af_right_top_lay.addRow(PDT_Label('Plot Metric:', font_size=14), ax_cb_widg)
        self.foil_metric_canvas = SingleAxCanvas(self, width=8, height=4.5)
        af_right_lay.addWidget(self.foil_metric_canvas)


class PropellerWidget(QtWidgets.QWidget):
    def __init__(self):
        super(PropellerWidget, self).__init__()
        main_lay = QtWidgets.QHBoxLayout()
        self.setLayout(main_lay)


class OptimizationWidget(QtWidgets.QWidget):
    def __init__(self):
        super(OptimizationWidget, self).__init__()
        main_lay = QtWidgets.QHBoxLayout()
        self.setLayout(main_lay)
