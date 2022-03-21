# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import numpy


class Statistics:
    """
    Class used to gather statistics about a particular metric (number of failure, duration of failure etc.).
    Ideally histograms should be produced, for now, simpler estimators are used.
    """

    def __init__(self):
        self.min = numpy.inf
        self.max = - numpy.inf
        self.sum = 0
        self.sum_square = 0
        self.boolean = 0

        self.mean = numpy.NaN
        self.std = numpy.NaN

    def update_min(self, value):
        if self.min > value:
            self.min = value

    def update_max(self, value):
        if self.max < value:
            self.max = value

    def update_sum(self, value, weight: float = 1.0):
        self.sum = self.sum + value * weight

    def update_sum_square(self, value, weight: float = 1.0):
        # It's possible that the weight should be outside the parenthesis
        self.sum_square = self.sum_square + value ** 2 * weight

    def update_boolean(self, value, weight: float = 1.0):
        self.boolean = self.boolean + bool(value) * weight

    def update(self, value, weight: float = 1.0):
        self.update_min(value)
        self.update_max(value)
        self.update_sum(value, weight)
        self.update_sum_square(value, weight)
        self.update_boolean(value, weight)

    def evaluate_result(self):
        self.evaluate_mean()
        self.evaluate_standard_deviation()
        self.evaluate_bool()

    def evaluate_mean(self):
        self.mean = self.sum 

    def evaluate_standard_deviation(self):
        x = float(self.sum_square - (self.sum) ** 2)
        self.std = 0.0
        if x > 10e-12:
            self.std = numpy.sqrt(
                float(self.sum_square - (self.sum) ** 2))

    def evaluate_bool(self):
        self.boolean = self.boolean

    def __str__(self):
        return "MIN:{}, MAX:{}, SUM:{}, SUM_SQUARE:{}, BOOLEAN:{}".format(self.min,
                                                                          self.max,
                                                                          self.sum,
                                                                          self.sum_square,
                                                                          self.boolean)

    def __repr__(self):
        return self.__str__()
