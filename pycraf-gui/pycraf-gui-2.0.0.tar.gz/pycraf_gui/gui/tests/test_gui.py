#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from __future__ import absolute_import
# from __future__ import division
# from __future__ import print_function
# from __future__ import unicode_literals

import pytest
import re
import numpy as np
from numpy.testing import assert_equal, assert_allclose
from astropy.tests.helper import assert_quantity_allclose  #, remote_data
from astropy import units as apu
from astropy.units import Quantity
# from astropy.utils.misc import NumpyRNGContext
# from astropy.utils.data import get_pkg_data_filename
from PyQt5 import QtCore, QtWidgets
from .. import gui
from pycraf import conversions as cnv
from pycraf import pathprof


LABEL_TEXT = '''
<style>
    table {
        color: black;
        width: 100%;
        text-align: center;
        font-family: "Futura-Light", sans-serif;
        font-weight: 400;
        font-size: 14px;
    }
    th {
        color: blue;
        font-size: 16px;
    }
    th, td { padding: 2px; }
    thead.th {
        height: 110%;
        border-bottom: solid 0.25em black;
    }
    .lalign { text-align: left; padding-left: 12px;}
    .ralign { text-align: right; padding-right: 12px; }
</style>

<table>
  <thead>
    <tr>
      <th colspan="2">Radio properties</th>
      <th colspan="2">Path geometry</th>
      <th colspan="2">Path losses</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="lalign">a_e (50%)</td>
      <td class="ralign"> 8455 km</td>
      <td class="lalign">alpha_tr</td>
      <td class="ralign"> 122.081 deg</td>
      <td class="lalign">L_b0p (LoS)</td>
      <td class="ralign">127.3 dB</td>
    </tr>
    <tr>
      <td class="lalign">a_e (beta0)</td>
      <td class="ralign">19113 km</td>
      <td class="lalign">alpha_rt</td>
      <td class="ralign"> -57.390 deg</td>
      <td class="lalign">L_bd (Diffraction)</td>
      <td class="ralign">182.6 dB</td>
    </tr>
    <tr>
      <td class="lalign">beta0</td>
      <td class="ralign">1.25 %</td>
      <td class="lalign">eps_pt</td>
      <td class="ralign">   1.537 deg</td>
      <td class="lalign">L_bs (Troposcatter)</td>
      <td class="ralign">251.0 dB</td>
    </tr>
    <tr>
      <td class="lalign">N0</td>
      <td class="ralign">324.7</td>
      <td class="lalign">eps_pr</td>
      <td class="ralign">   6.793 deg</td>
      <td class="lalign">L_ba (Anomalous)</td>
      <td class="ralign">220.2 dB</td>
    </tr>
    <tr>
      <td class="lalign">Delta N</td>
      <td class="ralign">38.69 1 / km</td>
      <td class="lalign">h_eff</td>
      <td class="ralign">  1399.2 m</td>
      <td class="lalign">L_b (Total)</td><td class="ralign">182.6 dB</td>
    </tr>
    <tr>
      <td class="lalign"></td>
      <td class="ralign"></td>
      <td class="lalign">Path type</td>
      <td class="ralign">Trans-horizon</td>
      <td class="lalign" style="color: blue;">L_b_corr (Total + Clutter)</td>
      <td class="ralign" style="color: blue;">181.9 dB</td>
    </tr>
  </tbody>
</table>
'''


def _set_parameters(ui):

    ui.freqDoubleSpinBox.setValue(1.0)
    ui.timepercentDoubleSpinBox.setValue(2.0)
    ui.stepsizeDoubleSpinBox.setValue(10.0)
    ui.tempDoubleSpinBox.setValue(293.15)
    ui.pressDoubleSpinBox.setValue(980.0)
    ui.txLonDoubleSpinBox.setValue(6.2)
    ui.txLatDoubleSpinBox.setValue(50.8)
    ui.txHeightDoubleSpinBox.setValue(50.0)
    ui.rxLonDoubleSpinBox.setValue(6.88361)
    ui.rxLatDoubleSpinBox.setValue(50.52483)
    ui.rxHeightDoubleSpinBox.setValue(10.0)
    ui.mapSizeLonDoubleSpinBox.setValue(0.2)
    ui.mapSizeLatDoubleSpinBox.setValue(0.2)
    ui.mapResolutionDoubleSpinBox.setValue(3.0)

# do a minimal test involving srtm data for reference
@pytest.mark.usefixtures('srtm_handler')
def test_srtm_height_data_linear():

    lons, lats = np.meshgrid(
        np.arange(6.1005, 6.9, 0.2),
        np.arange(50.1005, 50.9, 0.2)
        )
    heights = pathprof.srtm_height_data(
        lons.flatten() * apu.deg, lats.flatten() * apu.deg
        ).reshape(lons.shape)

    assert_quantity_allclose(heights, np.array([
      [167.48, 217.64, 187.08, 191.20],
      [195.52, 241.20, 199.52, 214.60],
      [179.16, 252.48, 168.00, 161.40],
      [221.24, 181.20, 170.28, 203.32],
      ]) * apu.m)


@pytest.mark.gui
@pytest.mark.usefixtures('srtm_handler')
def test_gui_startup_shows_pathgeometry(qtbot):
    # change download option to missing and test, if the results label
    # in geometry pane has correct values (need to wait for startup-timer
    # to fire)

    myapp = gui.PycrafGui()
    qtbot.addWidget(myapp)
    _set_parameters(myapp.ui)
    myapp.ui.srtmDownloadComboBox.setCurrentIndex(
        gui.SRTM_DOWNLOAD_MAPPING.index('never')
        )
    with qtbot.waitSignal(
            myapp.my_geo_worker.result_ready[object, object],
            raising=False, timeout=50000,
            ):
        myapp.timer.start(10)

    ltxt = myapp.ui.ppRichTextLabel.text()
    print(ltxt)
    assert re.sub("\\s*", " ", ltxt) == re.sub("\\s*", " ", LABEL_TEXT)


@pytest.mark.gui
@pytest.mark.usefixtures('srtm_handler')
def test_stats_worker(qtbot):
    # change download option to missing and test, if the results are correct

    myapp = gui.PycrafGui()
    qtbot.addWidget(myapp)
    _set_parameters(myapp.ui)
    myapp.ui.srtmDownloadComboBox.setCurrentIndex(
        gui.SRTM_DOWNLOAD_MAPPING.index('never')
        )
    with qtbot.waitSignal(
            myapp.my_stats_worker.result_ready[object, object],
            raising=False, timeout=50000,
            ):
        myapp.timer.start(10)

    res = myapp.statistics_results

    assert_quantity_allclose(
        res['L_b'][:, ::20].to(cnv.dB).value, [
            [154.2717482, 154.7008784, 155.1300085, 155.5591386, 156.6658793],
            [168.1726196, 171.3723174, 172.7435381, 173.1726683, 173.9579308],
            [181.0480631, 181.4771933, 181.9063234, 182.3354535, 182.8716378],
            [190.1585426, 190.5876727, 191.0168029, 191.4459330, 191.9820030],
            [202.1996918, 202.6288219, 203.0579521, 203.4870822, 204.0230525],
            [211.5453782, 211.9745084, 212.4036385, 212.8327686, 213.3686897],
            [226.1338265, 226.5629566, 226.9920868, 227.4212169, 227.9571040],
            [252.5214973, 252.9506276, 253.3797578, 253.8088879, 254.3447456],
            [267.3074414, 267.7368170, 268.1659884, 268.5951245, 269.1309685],
            ])
    # assert myapp.pathprof_results is None


@pytest.mark.gui
@pytest.mark.usefixtures('srtm_handler')
def test_pp_worker(qtbot):
    # change download option to missing and test, if the results are correct

    myapp = gui.PycrafGui()
    qtbot.addWidget(myapp)
    _set_parameters(myapp.ui)
    myapp.ui.srtmDownloadComboBox.setCurrentIndex(
        gui.SRTM_DOWNLOAD_MAPPING.index('never')
        )
    with qtbot.waitSignal(
            myapp.my_pp_worker.result_ready[object, object],
            raising=False, timeout=50000,
            ):
        myapp.on_pathprof_compute_pressed()

    res = myapp.pathprof_results

    assert_quantity_allclose(
        res['L_b'][::1000].to(cnv.dB).value,
        [0., 157.972929, 172.52172, 180.40373, 184.086423, 181.1237212]
        )
    assert_quantity_allclose(
        res['eps_pt'][::1000].to(apu.deg).value,
        [0., 1.536944, 1.536942, 1.53694, 1.536938, 1.536936],
        atol=1e-6, rtol=1e-6
        )
    assert_equal(res['path_type'][::1000], [0, 1, 1, 1, 1, 1])
    # assert myapp.pathprof_results is None


@pytest.mark.gui
@pytest.mark.usefixtures('srtm_handler')
def test_map_worker(qtbot):
    # change download option to missing and test, if the results are correct

    myapp = gui.PycrafGui()
    qtbot.addWidget(myapp)
    _set_parameters(myapp.ui)
    myapp.ui.srtmDownloadComboBox.setCurrentIndex(
        gui.SRTM_DOWNLOAD_MAPPING.index('never')
        )
    with qtbot.waitSignal(
            myapp.my_map_worker.result_ready[object, object],
            raising=False, timeout=50000,
            ):
        myapp.on_map_compute_pressed()

    res = myapp.map_results

    print(res['L_b'][::80, ::80].to(cnv.dB).value)
    print(res['eps_pt'][::80, ::80].to(apu.deg).value)
    print(res['path_type'][::80, ::80])
    assert_quantity_allclose(
        res['L_b'][::80, ::80].to(cnv.dB).value, [
            [163.31770261, 165.22676741, 131.12436506, 174.48122428],
            [167.62530535, 151.35816148, 159.98972068, 170.32689950],
            [149.65770949, 158.09945172, 157.58625982, 152.91956091],
            [173.62306704, 165.38626174, 162.34733462, 170.04263257],
            ])
    assert_quantity_allclose(
        res['eps_pt'][::80, ::80].to(apu.deg).value, [
            [1.81177833, 1.71394821, 0.33816931, 1.39554158],
            [0.55507680, 1.97696811, 1.61839769, 5.14500455],
            [4.14323932, 1.65557532, 3.54791246, 2.23291487],
            [1.56320178, 2.15972181, 0.81075965, 3.29290329],
            ])
    assert_equal(res['path_type'][::80, ::80], [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        ])
    # assert myapp.pathprof_results is None
