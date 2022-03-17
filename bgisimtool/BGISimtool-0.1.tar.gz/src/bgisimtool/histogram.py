# MIT License

# Copyright (c) 2018 Swann Levasseur

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
# stdev in histogram
from numpy import sqrt, histogram
import numpy as np
from math import pow
import logging

# ------------------------------------------------------------------------------
# logger
# ------------------------------------------------------------------------------
histogram_logger = logging.getLogger('bgisimtool.histogram')

# ------------------------------------------------------------------------------
# Class Histogram DO NOT USE, kept for compatibility with old stuff
# ------------------------------------------------------------------------------
class Histogram:
    """A class representing a histogram"""

    # ----------------------
    # Magic methods
    # ----------------------

    def __init__(self, bin_center=None, content=None, bin_width=None):
        self.mean = 0
        self.mean_err = 0
        self.stdev = 0
        self.stdev_err = 0
        self.integral = 0
        self.min_bin_value = 0
        # used for the iterable feature
        self.index = 0
        # if the user provided all the list and they are all the same size, fill the hist
        if not((bin_center is None) or (content is None) or (bin_width is None)) and (len(bin_center) == len(content) == len(bin_width)):
            self._bin_center = bin_center
            self._bin_width = bin_width
            self._bin_content = content
            self.updateAll()
        else:
            # else all empty
            self._bin_center = []
            self._bin_width = []
            self._bin_content = []

    # return the size of the hist in terms of number of bins
    def __len__(self):
        return len(self._bin_center)

    # to make it act like a list
    def __getitem__(self, index):
        return self._bin_center[index], self._bin_content[index], self._bin_width[index]

    def __setitem__(self, index, data_tupple):
        self._bin_center[index], self._bin_content[index], self._bin_width[index] = data_tupple

    def __delitem__(self, index):
        del self._bin_center[index]
        del self._bin_content[index]
        del self._bin_width[index]

    def __str__(self):
        description = 'Class Histogram\n'
        description += 'Bin number : {0:d} \n'.format(len(self._bin_center))
        description += 'Mean : {0:.3f} \n'.format(self.mean)
        description += 'Mean error : {0:.3f} \n'.format(self.mean_err)
        description += 'Stdev : {0:.3f} \n'.format(self.stdev)
        description += 'Stdev error : {0:.3f} \n'.format(self.stdev_err)
        description += 'Integral : {0:d} \n'.format(self.integral)
        description += 'Min bin value : {0:d} \n'.format(self.min_bin_value)
        return description

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        try:
            result = (self._bin_center[self.index], self._bin_content[self.index], self._bin_width[self.index])
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

    # ----------------------
    # manually fill
    # ----------------------
    def fillFromRawPosition(self, positions, bin_size, limits=None):
        """ fillFromRawPosition( [12,13,14...], 55e-6, (-5,14) )
        Fill the _bin_center and _bin_content and _bin_width members of a Histogram object using the
        positional data provided in position and the bin size provided by bin_size.
        limits is a tupple with the range between witch to fill the histogram (it can be set larger or smaller to the actual min, max of the   positions).
        If no range is provided, the range is automaticaly assigned to the min and max value of positions
        ! Make sure positons, bin_size and limits are all in the same unit e.g mm !
        """
        if limits is None:
            limits = ()

        # reset to avoid stacking data
        self.reset()
        # Constants (any function call done more than once for the same value..)
        min_pos = min(positions)
        max_pos = max(positions)
        # check for range to create the right offset
        if limits:
            # check if the range provided is at least partially overlapping with the positions
            if max_pos < limits[0] or min_pos > limits[1]:
                print('Limits provided in fillFromRawPosition are not overlapping with the positions')
                print('Abort')
                return
            offset = limits[0]
            bin_number = int((limits[1] - limits[0]) / bin_size) + 1
        else:
            # range not provided, deduce from data
            # get offset from min value of positions
            offset = min_pos
            # Find the good number of bins
            bin_number = int((max_pos - min_pos) / bin_size) + 1

        # Apply the offset to all positions, this is needed to easily fill the hist afterward
        positions_offset = list(map(lambda a: a - offset, positions))

        # fill the bin_centers and widths. The content are set to zeros
        for x in range(bin_number):
            self._bin_center.append((x * bin_size) + (bin_size / 2) + offset)
            self._bin_width.append(bin_size)
            self._bin_content.append(0)

        # Fill the bin_content, this is where positions_offset is used
        for val in positions_offset:
            index = int(val / bin_size)
            if index >= 0:
                self._bin_content[index] += 1
        #update the histogram data
        self.updateAll()

    # ----------------------
    # add one bin
    # ----------------------
    def add(self, data_tupple):
        self._bin_center.append(data_tupple[0])
        self._bin_content.append(data_tupple[1])
        self._bin_width.append(data_tupple[2])

    # ----------------------
    # Fill from file
    # ----------------------
    def fillFromFile(self, filename):
        """ Read the content of a .txt file containing a histogram.
            The histogram object is updated after the the file if loaded.
            filename is a string.
        """
        # reset to avoid stacking data
        self.reset()
        # Open file
        with open(filename, 'r') as file:
            # skip the header lines
            next(file)
            next(file)
            # read the data
            for line in file:
                # load a line and split it in a list of floats
                num = list(map(float, line.split(',')))
                if len(num) == 3:
                    self._bin_center.append(num[0])
                    self._bin_content.append(num[1])
                    self._bin_width.append(num[2])
                elif len(num) == 2:
                    self._bin_center.append(num[0])
                    self._bin_content.append(num[1])
                    self._bin_width.append(1)
                else:
                    raise ValueError
        # update with all new stuff
        self.updateAll()

    # ----------------------
    # write 2 file
    # ----------------------
    def write2File(self, filename):
        """ Write the current content of the histogram object into a simple text file
            filename is a string
        """
        # Open file
        with open(filename, 'w') as file:
            # write the header line
            file.write('Bin center, bin content, bin width')
            # read the data
            for i in range(len(self._bin_center)):
                # write each line
                file.write(str(self._bin_center[i]) + ', ' + self._bin_content[i] + ', ' + self._bin_width[i])

    # ----------------------
    # Histogram modification
    # ----------------------

    def conditionalBining(self, content_limit=5):
        """ Scan the histogram and merge bins in order to have all bins > content_limit.
            The scanning is done from the first to the last bin
            !This may result in a histogram with a non constant bin width!"""

        temp_bin_center = []
        temp_bin_content = []
        temp_bin_width = []
        # you have to initialize it with the first bin..
        current_bin_center = 0
        current_bin_content = 0
        current_bin_width = 0
        lower_bin_wall = self._bin_center[0] - (self._bin_width[0] / 2)

        for i in range(len(self._bin_center)):
            current_bin_center = lower_bin_wall + ((current_bin_width + self._bin_width[i]) / 2)
            current_bin_content += self._bin_content[i]
            current_bin_width += self._bin_width[i]
            # test
            if current_bin_content >= content_limit:
                temp_bin_center.append(current_bin_center)
                temp_bin_content.append(current_bin_content)
                temp_bin_width.append(current_bin_width)
                # reset
                lower_bin_wall += current_bin_width
                current_bin_center = 0
                current_bin_content = 0
                current_bin_width = 0

        # add the last bin

        temp_bin_center[-1] = (lower_bin_wall - temp_bin_width[-1]) + ((current_bin_width + temp_bin_width[-1]) / 2)
        temp_bin_content[-1] += current_bin_content
        temp_bin_width[-1] += current_bin_width

        # update hist
        self._bin_center = temp_bin_center
        self._bin_width = temp_bin_width
        self._bin_content = temp_bin_content

    def reframe(self, limits):
        # new hist
        bin_center = []
        bin_content = []
        bin_width = []
        # for each existing bin
        for i in range(len(self._bin_center)):
            # if within the limits, we keep it
            if self._bin_center[i] > limits[0] and self._bin_center[i] < limits[1]:
                bin_center.append(self._bin_center[i])
                bin_content.append(self._bin_content[i])
                bin_width.append(self._bin_width[i])
        # overwrite the current hist
        self._bin_center = bin_center
        self._bin_content = bin_content
        self._bin_width = bin_width

    def rebin(self, bin_factor):
        """Function to rebin the histogram y a certain factor !WARNING WIP! """
        # declare temp container to contain the new values of the hist
        temp_center_list = []
        temp_content_list = []
        temp_width_list = []
        temp_center = 0
        temp_content = 0
        temp_width = 0
        lower_bin_wall = self._bin_center[0] - (self._bin_width[0] / 2)
        # counter
        bin_cnt = 0
        # for each value in the hist
        for i in range(len(self._bin_center)):
            temp_content += self._bin_content[i]
            temp_width += self._bin_width[i]
            temp_center = lower_bin_wall + (temp_width / 2)
            bin_cnt += 1
            # if the bin is not combined yet
            if bin_cnt >= bin_factor:
                temp_center_list.append(temp_center)
                temp_content_list.append(temp_content)
                temp_width_list.append(temp_width)
                # reset
                lower_bin_wall += temp_width
                temp_content = 0
                temp_center = 0
                temp_width = 0
                # reset the cnt
                bin_cnt = 0
        # replace existing data
        self._bin_center = temp_center_list
        self._bin_width = temp_width_list
        self._bin_content = temp_content_list

    def fillBlank(self, bin_number):
        """Fill the histogram object with 'bin_number' bins of content None
           This function should be used when a user want to fill a histogram in a custom way and need the memory to e allocated already"""
        # reset to make sure we don't stack data
        self.reset()
        # for all bins requested add an empty bin
        for _ in range(bin_number):
            self._bin_center.append(None)
            self._bin_content.append(None)
            self._bin_width.append(None)

    def areaNormalize(self):
        # make sure we have the integral
        self._updateIntegral()
        # for each bin
        for i in range(len(self._bin_content)):
            self._bin_content[i] = self._bin_content[i] / self.integral

    def selectiveBinning(self, min_bin_count):
        """ Remove every bin with less than 'min_bin_count' from the parent histogram."""
        # for each bin
        new_center = []
        new_content = []
        new_width = []
        for index in range(len(self._bin_center)):
            # if the current bin has more or equal than min_bin_count, keep that bin
            if self._bin_content[index] >= min_bin_count:
                new_center.append(self._bin_center[index])
                new_content.append(self._bin_content[index])
                new_width.append(self._bin_width[index])
        # overwrite the content
        self._bin_center = new_center
        self._bin_content = new_content
        self._bin_width = new_width

    def filterByExpected(self, exp, lim):
        """ Remove every bin where the corresponding item in the 'exp' is lower than lim
        """
        new_center = []
        new_content = []
        new_width = []
        new_exp = []
        # for each position in exp
        for i in range(len(exp)):
            # if exp is above or equal to lim
            if exp[i] >= lim:
                new_center.append(self._bin_center[i])
                new_content.append(self._bin_content[i])
                new_width.append(self._bin_width[i])
                new_exp.append(exp[i])
        # overwrite the old values
        self._bin_center = new_center
        self._bin_content = new_content
        self._bin_width = new_width
        return new_exp


    # ----------------------
    # Update attributes
    # ----------------------

    def _updateIntegral(self):
        self.integral = sum(self._bin_content)

    def _updateMinBinValue(self):
        self.min_bin_value = max(self._bin_content)
        for val in self._bin_content:
            if val < self.min_bin_value:
                self.min_bin_value = val

    def _updateMean(self):
        if self.integral > 0:
            S = 0
            for i in range(len(self._bin_center)):
                S += self._bin_center[i] * self._bin_content[i]
                self.mean = S / self.integral
        else:
            self.mean = 0

    def _updateMeanErr(self):
        if self.integral > 0:
            self.mean_err = self.stdev / sqrt(sum(self._bin_content))
        else:
            self.mean_err = 0

    def _updateStdevErr(self):
        if self.integral > 0:
            # only valid for gaussian distribution
            self.stdev_err = self.stdev * (1 / sqrt(2 * self.integral - 2))
        else:
            self.stdev_err = 0

    def _updateStdev(self):
        if self.integral > 0:
            S = 0
            for i in range(len(self._bin_center)):
                S += self._bin_content[i] * pow((self._bin_center[i] - self.mean), 2)
            self.stdev = sqrt(S / self.integral)
        else:
            self.stdev = 0

    def updateAll(self):
        # we combine mean, integral and min_bin_value in the same loop to gain speed
        # get mean, integral, min_bin_value
        S = 0
        self.min_bin_value = max(self._bin_content)
        self.integral = 0
        for i in range(len(self._bin_center)):
            # mean
            S += self._bin_center[i] * self._bin_content[i]
            # integral
            self.integral += self._bin_content[i]
            # min bin content
            if self._bin_content[i] < self.min_bin_value:
                self.min_bin_value = self._bin_content[i]
        # check if intergral is zero, then no other meas
        if self.integral > 2:
            self.mean = S / self.integral
            # Get stdev, mean err, stdeverr
            self._updateStdev()
            # mean err
            self.mean_err = self.stdev / sqrt(sum(self._bin_content))
            # stdevErr
            self.stdev_err = self.stdev * (1 / sqrt(2 * self.integral - 2))
        else:
            self.mean = 0
            self.mean_err = 0
            self.stdev_err = 0
            self.stdev = 0

    def reset(self):
        self._bin_center = []
        self._bin_content = []
        self._bin_width = []
        self.index = 0
        self.mean = 0
        self.mean_err = 0
        self.stdev = 0
        self.stdev_err = 0
        self.integral = 0
        self.min_bin_value = 0



# ------------------------------------------------------------------------------
# Class Histogram
# ------------------------------------------------------------------------------
class HistogramV2:
    """A class representing a histogramV2"""

    # ----------------------
    # Magic methods
    # ----------------------

    def __init__(self, positions=None, bin_width=None, bin_count=None, log_level=logging.WARNING):
        self.mean = 0
        self.mean_err = 0
        self.stdev = 0
        self.stdev_err = 0
        self.integral = 0
        self.min_bin_value = 0
        self._bin_edge = None
        self._bin_center = None
        self._bin_content = None
        self.logger = logging.getLogger('bgisimtool.histogram.histogramV2')
        self.logger.setLevel(log_level)
        # if we can fill it, we do it
        if positions is not None and (bin_width is not None or bin_count is not None):
            self.fill_from_positions(positions, bin_width=bin_width, bin_number=bin_count)

    # return the size of the hist in terms of number of bins
    def __len__(self):
        return len(self._bin_center)

    # ----------------------
    # manually fill
    # ----------------------
    def fill_from_positions(self, positions, bin_width=None, bin_number=None, limits=None):
        # if no bin width or bin number is given, the default of bin_number = 10 from numpy is used.
        if bin_number is None and bin_width is not None:
            min_pos = min(positions)
            max_pos = max(positions)
            if limits:
                bin_count = int((limits[1] - limits[0]) / bin_width)
            else:
                bin_count = int((max_pos - min_pos) / bin_width)
        else:
            bin_count = bin_number
        # get hist,
        self._bin_content, self._bin_edge = np.histogram(positions, bins=bin_count, range=limits)
        self._bin_center = 0.5 * (self._bin_edge[1:] + self._bin_edge[:-1])
        self.update_all()

    def fill_by_value(self, bin_content, bin_edge, bin_center):
        if len(bin_edge) != len(bin_content + 1):
            self.logger.error("Error, Bin_edge should be N+1 of bin_content.")
            return
        else:
            self._bin_center = bin_center
            self._bin_content = bin_content
            self._bin_edge = bin_edge
            self.update_all()
    # ----------------------
    # Histogram modification
    # ----------------------

    def conditional_binning(self, content_limit=5):
        """ Scan the histogram and merge bins in order to have all bins > content_limit.
            The scanning is done from the first to the last bin
            !This may result in a histogram with a non constant bin width!"""
        # for each bin in the hist
        temp_bin_content = []
        temp_bin_center = []
        temp_bin_edge = []
        # bin edge is N+1 longer than the rest and the left bin is always preserved
        temp_bin_edge.append(self._bin_edge[0])
        # loop through all bins
        max_index = len(self._bin_content) - 1
        index = 0
        last = False
        while index < len(self._bin_content):
            # while the bin content is below content_limit, combine bins
            temp_bin = self._bin_content[index]
            while temp_bin < content_limit:
                index += 1
                # if we are not at the last bins
                if index <= max_index:
                    temp_bin += self._bin_content[index]
                # if we are at the last bin and it's too small
                else:
                    last = True
                    # we need to remove one to the index to avoid conflict with bin_edge
                    index -= 1
                    break
            #
            if not last:
                temp_bin_content.append(temp_bin)
                temp_bin_edge.append(self._bin_edge[index + 1])
                # re_calc the bin center
                temp_bin_center.append(0.5 * (temp_bin_edge[-1] + temp_bin_edge[-2]))
            else:
                temp_bin_content[-1] += temp_bin
                temp_bin_edge[-1] = self._bin_edge[index + 1]
                temp_bin_center[-1] = (0.5 * (temp_bin_edge[-1] + temp_bin_edge[-2]))

            index += 1
        # update the hist
        self._bin_content = np.array(temp_bin_content)
        self._bin_center = np.array(temp_bin_center)
        self._bin_edge = np.array(temp_bin_edge)
        # update_hists
        self.update_all()

    def reframe(self, limits):
        # new hist
        temp_bin_content = []
        temp_bin_center = []
        temp_bin_edge = []
        # for each existing bin
        for i in range(len(self._bin_center)):
            # if within the limits, we keep it
            if self._bin_edge[i] > limits[0] and self._bin_edge[i+1] < limits[1]:
                temp_bin_center.append(self._bin_center[i])
                temp_bin_content.append(self._bin_content[i])
                temp_bin_edge.append(self._bin_edge[i])
        # keep the last in edge
        temp_bin_edge.append(self._bin_edge[i + 1])
        # overwrite the current hist
        self._bin_center = np.array(temp_bin_center)
        self._bin_content = np.array(temp_bin_content)
        self._bin_edge = np.array(temp_bin_edge)
        # update
        self.update_all()

    def area_normalize(self):
        self._bin_content = self._bin_content / self.integral
        self.update_all()

    def filter_by_expected(self, exp, lim):
        """ set to 0 every bin where the corresponding item in the 'exp' is lower than lim
        """
        # for each position in exp
        for i in range(len(exp)):
            # if exp is above or equal to lim
            if exp[i] < lim:
                self._bin_content[i] = 0
                exp[i] = 0
        # update
        self.update_all()
        return exp

    # ----------------------
    # Update attributes
    # ----------------------
    def update_all(self):
        self.min_bin_value = min(self._bin_content)
        self.integral = np.sum(self._bin_content)
        if self.integral > 2:
            self.mean = np.average(self._bin_center, weights=self._bin_content)
            self.stdev = sqrt(np.average((self._bin_center - self.mean) ** 2, weights=self._bin_content))
            self.stdev_err = self.stdev * (1 / np.sqrt(2 * self.integral - 2))
            self.mean_err = self.stdev / np.sqrt(np.sum(self._bin_content))
        else:
            self.logger.warning("Cannot update all, < 2 samples in histogram")
            self.mean_err = 0
            self.stdev_err = 0
            self.stdev = 0