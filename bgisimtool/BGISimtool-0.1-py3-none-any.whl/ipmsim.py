# MIT License

# Copyright (c) 2021 Swann Levasseur

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
from bgisimtool.histogram import HistogramV2
from bgisimtool.fileUtils import findFileWithExtention
import collections
import pandas as pd
import numpy as np
import scipy.constants as cte
from tqdm import tqdm
import logging

# ------------------------------------------------------------------------------
# custom function
# ------------------------------------------------------------------------------
def momentum_2_KEev(p):
    conv = cte.physical_constants['electron volt'][0]/cte.c  # convert kg*m/s to eVelectron volt
    E0_ev = cte.physical_constants['electron mass energy equivalent in MeV'][0] * 1e6 # electron rest energy in ev
    return np.sqrt(np.power(E0_ev,2) + np.power(p / conv,2)) - E0_ev


def get_vector_amplitude(a,b,c):
    return np.sqrt(np.power(a, 2) + np.power(b, 2) + np.power(c, 2))


# ------------------------------------------------------------------------------
# logger
# ------------------------------------------------------------------------------
ipmsim_logger = logging.getLogger('bgisimtool.ipmsim')


# ------------------------------------------------------------------------------
# Class ipmsimResult
# ------------------------------------------------------------------------------
class IpmsimResult:
    """ A class representing an IPMSIM simulation result"""

    def __init__(self, filename_s=None,
                 position_bin_width=55e-6,
                 energy_bin_width=10,
                 drift_bin_width=10e-6,
                 ignore_invalid=False,
                 PSF=False,
                 log_level=logging.WARNING,
                 scale="m",
                 m_map=False):
        # base file info
        self.data = None
        self.hide_update_bars = False
        self.scale = scale
        # histograms
        self.position_bin_width = position_bin_width
        self.energy_bin_width = energy_bin_width
        self.drift_bin_width = drift_bin_width
        self.initial_hist = HistogramV2()
        self.final_hist = HistogramV2()
        self.drift_x_hist = HistogramV2()
        self.drift_y_hist = HistogramV2()
        self.drift_z_hist = HistogramV2()
        self.energy_x_hist = HistogramV2()
        self.energy_y_hist = HistogramV2()
        self.energy_z_hist = HistogramV2()
        self.energy_tot_hist = HistogramV2()
        # PSF
        self.psf_distributions = None
        self.psf_stdevs = None
        self.psf_means = None
        self.psf_x_bin_center = None
        self.psf_y_bin_center = None
        self.psf_x_bin_width = None
        self.psf_y_bin_width = None
        # scale
        self.scale = None
        self.scale_factor = None
        self.set_scale(scale)
        # logger
        self.logger = logging.getLogger('bgisimtool.ipmsim.IpmsimResult')
        self.logger.setLevel(log_level)
        if log_level == logging.WARNING:
            self.hide_update_bars = True
        else:
            self.hide_update_bars = False
        # load
        if filename_s is not None:
            self.fill_from_file(filename_s, ignore_invalid=ignore_invalid, m_map=m_map)
            if PSF:
                self.calc_psf()

    # return the size of the ipmsim in terms of particle
    def __len__(self):
        return len(self.data)

    def set_scale(self, scale):
        if scale == "m":
            self.scale = scale
            self.scale_factor = 1
        elif scale == "mm":
            self.scale = scale
            self.scale_factor = 1e3
        elif scale == "um":
            self.scale = scale
            self.scale_factor = 1e6
        else:
            self.scale = "m"
            self.scale_factor = 1

    def _scale_value(self, val):
        return float(val) * self.scale_factor

    def fill_from_file(self, filename_s, ignore_invalid=False, m_map=False):
        # defining the converters for scaling the data
        conv = {'initial x': self._scale_value,
                'initial y': self._scale_value,
                'initial z': self._scale_value,
                'final x': self._scale_value,
                'final y': self._scale_value,
                'final z': self._scale_value}

        self.logger.info("Importing data.")
        # check if we have only one filename, a list of filenames
        if isinstance(filename_s, collections.abc.Iterable) and not isinstance(filename_s, str):
            self.logger.info(f"Importing {len(filename_s)} files.")
            for file in tqdm(filename_s, disable=self.hide_update_bars):
                temp = pd.read_csv(file, header=0, converters=conv, memory_map=m_map)
                self.data = pd.concat([self.data, temp], ignore_index=True)
        else:
            self.data = pd.read_csv(filename_s, header=0, converters=conv, memory_map=m_map)
        # remove invalid particle if needed
        if ignore_invalid:
            self.data = self.data[self.data['status'] == 'DETECTED']
        # calculate the drifts and energy data
        self._calc_energy_and_drift()
        # Update if required.
        self.update_all()

    def rescale(self, scale):
        pass
        #self.data[]

    def _calc_energy_and_drift(self):
        self.logger.info("Calculating kinetic energy and drifts.")
        pbar = tqdm(total=7, disable=self.hide_update_bars)
        self.data['final EK_x eV'] = momentum_2_KEev(self.data['final px'])
        pbar.update(1)
        self.data['final EK_y eV'] = momentum_2_KEev(self.data['final py'])
        pbar.update(1)
        self.data['final EK_z eV'] = momentum_2_KEev(self.data['final pz'])
        pbar.update(1)
        self.data['final EK eV'] = get_vector_amplitude(self.data['final EK_x eV'],
                                                        self.data['final EK_y eV'],
                                                        self.data['final EK_z eV'])
        pbar.update(1)
        # calc the drifts
        self.data['drift_x'] = self.data['initial x'] - self.data['final x']
        pbar.update(1)
        self.data['drift_y'] = self.data['initial y'] - self.data['final y']
        pbar.update(1)
        self.data['drift_z'] = self.data['initial z'] - self.data['final z']
        pbar.update(1)
        pbar.close()
        del pbar

    def fill_from_all_files_with_extension(self, path, ext):
        self.fill_from_file(findFileWithExtention(path, ext))

    def _update_energy_spectrums(self, bin_size=10):
        self.logger.info("Updating energy spectrums.")
        pbar = tqdm(total=4, disable=self.hide_update_bars)
        self.energy_x_hist.fill_from_positions(self.data['final EK_x eV'], bin_width=bin_size)
        pbar.update(1)
        self.energy_y_hist.fill_from_positions(self.data['final EK_y eV'], bin_width=bin_size)
        pbar.update(1)
        self.energy_z_hist.fill_from_positions(self.data['final EK_z eV'], bin_width=bin_size)
        pbar.update(1)
        self.energy_tot_hist.fill_from_positions(self.data['final EK eV'], bin_width=bin_size)
        pbar.update(1)
        pbar.close()
        del pbar

    def _update_drift_histograms(self, bin_size=10e-6):
        self.logger.info("Updating drift histograms.")
        pbar = tqdm(total=3, disable=self.hide_update_bars)
        self.drift_x_hist.fill_from_positions(self.data['drift_x'], bin_width=bin_size)
        pbar.update(1)
        self.drift_y_hist.fill_from_positions(self.data['drift_y'], bin_width=bin_size)
        pbar.update(1)
        self.drift_z_hist.fill_from_positions(self.data['drift_z'], bin_width=bin_size)
        pbar.update(1)
        pbar.close()
        del pbar

    def _update_positions_histograms(self, bin_size=55e-6, content_limit=5, limits=None):
        self.logger.info("Updating position histograms.")
        pbar = tqdm(total=2, disable=self.hide_update_bars)
        self.initial_hist.fill_from_positions(self.data['initial x'], bin_width=bin_size, limits=limits)
        pbar.update(1)
        self.final_hist.fill_from_positions(self.data['final x'], bin_width=bin_size, limits=limits)
        pbar.update(1)
        pbar.close()
        del pbar

    def update_all(self):
        self._update_positions_histograms(bin_size=self.position_bin_width)
        self._update_drift_histograms(bin_size=self.drift_bin_width)
        self._update_energy_spectrums(bin_size=self.energy_bin_width)

    def calc_psf(self, x_bin_size=100e-6, y_bin_size=100e-6):
        self.logger.info("Calculating point spread function.")
        self.logger.info("Initializing.")
        # define the limits of the grid, we add bin_size/2 to make sure the edge events are considered.
        x_min = min(self.data['initial x'])
        x_max = max(self.data['initial x'])
        y_min = min(self.data['initial y'])
        y_max = max(self.data['initial y'])
        #
        x_bin_number = int((x_max - x_min) / x_bin_size) + 1
        y_bin_number = int((y_max - y_min) / y_bin_size) + 1
        #
        x_positions_offset = self.data['initial x'] - x_min
        y_positions_offset = self.data['initial y'] - y_min
        # init the arrays for the bin_center, width and content
        self.psf_x_bin_center = np.zeros((x_bin_number, y_bin_number))
        self.psf_y_bin_center = np.zeros((x_bin_number, y_bin_number))
        self.psf_x_bin_width = np.zeros((x_bin_number, y_bin_number))
        self.psf_y_bin_width = np.zeros((x_bin_number, y_bin_number))
        self.psf_distributions = np.zeros((x_bin_number, y_bin_number), dtype=np.ndarray)
        self.psf_means = np.zeros((x_bin_number, y_bin_number))
        self.psf_stdevs = np.zeros((x_bin_number, y_bin_number))
        # fill the arrays
        for x in tqdm(range(x_bin_number), disable=self.hide_update_bars):
            for y in range(y_bin_number):
                self.psf_x_bin_center[x, y] = (x * x_bin_size) + (x_bin_size / 2) + x_min
                self.psf_y_bin_center[x, y] = (y * y_bin_size) + (y_bin_size / 2) + y_min
                self.psf_x_bin_width[x, y] = x_bin_size
                self.psf_y_bin_width[x, y] = y_bin_size
                self.psf_distributions[x, y] = []
        self.logger.info("Getting psf distributions")
        drift_index = 0
        for i in tqdm(range(len(x_positions_offset)), disable=self.hide_update_bars):
            x_index = int((x_positions_offset[i]) / x_bin_size)
            y_index = int((y_positions_offset[i]) / y_bin_size)
            self.psf_distributions[x_index, y_index].append(self.data['drift_x'][drift_index])  # may need to abs the drifts..
            drift_index += 1
        # get the mean and std
        self.logger.info("Getting psf stdevs and means")
        for i in tqdm(range(len(self.psf_distributions.flat)), disable=self.hide_update_bars):
            self.psf_means.flat[i] = np.mean(self.psf_distributions.flat[i])
            self.psf_stdevs.flat[i] = np.std(self.psf_distributions.flat[i])