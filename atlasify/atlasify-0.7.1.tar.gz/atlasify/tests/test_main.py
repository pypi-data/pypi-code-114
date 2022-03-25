"""
Copyright (C) 2019-2020 Frank Sauerburger

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; version 2 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
"""

import unittest

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.testing.compare import compare_images
from matplotlib.figure import Figure
import tempfile

import os

from atlasify import atlasify, AtlasStyle


class SurvivalTestCase(unittest.TestCase):
    """
    Test that the method does not crash..
    """

    def setUp(self):
        """
        Call plt.plot().
        """
        x = np.linspace(-3, 3, 200)
        y = np.exp(-(x ** 2))

        plt.plot(x, y, label="Something")

    def tearDown(self):
        """
        Clear the figure.
        """
        plt.clf()

    def test_default(self):
        """
        Check that calling atlasify() without arguments does not crash.
        """
        try:
            atlasify()
        except:
            self.assertFail("Calling atlasify() raised an exception")

    def test_False(self):
        """
        Check that calling atlasify() without badge does not crash.
        """
        try:
            atlasify(False)
        except:
            self.assertFail("Calling atlasify() raised an exception")

    def test_label(self):
        """
        Check that calling atlasify() with a label does not crash.
        """
        try:
            atlasify("Internal")
        except:
            self.assertFail("Calling atlasify() raised an exception")

    def test_subtext(self):
        """
        Check that calling atlasify() with a subtext does not crash.
        """
        try:
            atlasify("Internal", "Hello\nWorld\nHow are you")
        except:
            self.assertFail("Calling atlasify() raised an exception")

    def test_enlarge(self):
        """
        Check that calling atlasify() with different enalrge does not crash.
        """
        try:
            atlasify("Internal", enlarge=2)
        except:
            self.assertFail("Calling atlasify() raised an exception")


class CompareOutputTestCase(unittest.TestCase):
    """
    Test the output of some configurations.
    """

    def assertImageEqual(self, actual_path, expected_path):
        self.assertIsNone(
            compare_images(actual_path, expected_path, tol=0.009)
        )

    def setUp(self):
        """
        Generate data for plot and define directories for test plots
        """
        self.x = np.linspace(-3, 3, 200)
        self.y = np.exp(-self.x ** 2)

        # Set up temp directory for comparison plots
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.actual_plots_dir = f"{self.tmp_dir.name}/"
        self.expected_plots_dir = os.path.join(
            os.path.dirname(__file__), "expected_plots/"
        )

        # uncomment line below to update all expected plots (will write the current
        # plots in the expected_plots_dir)
        # self.tmp_plot_dir = self.expected_plots_dir

    def test_plt_badge_only(self):
        """test with ATLAS badge only"""

        plt.clf()
        plt.plot(self.x, self.y)
        atlasify()
        plotname = "test_01.png"
        plt.savefig(f"{self.actual_plots_dir}/{plotname}")
        # plt.savefig(f"{self.expected_plots_dir}/{plotname}")
        self.assertImageEqual(
            f"{self.actual_plots_dir}/{plotname}",
            f"{self.expected_plots_dir}/{plotname}"
        )

    def test_plt_with_text(self):
        """test with upper line text only"""

        plt.clf()
        plt.plot(self.x, self.y)
        atlasify("Internal")

        plotname = "test_02.png"
        plt.savefig(f"{self.actual_plots_dir}/{plotname}")
        # Uncomment line below to update expected image
        # plt.savefig(f"{self.expected_plots_dir}/{plotname}")
        self.assertImageEqual(
            f"{self.actual_plots_dir}/{plotname}",
            f"{self.expected_plots_dir}/{plotname}"
        )

    def test_plt_with_subtext(self):
        """test output plot with subtext"""

        plt.clf()
        plt.plot(self.x, self.y)
        atlasify(
            "Internal",
            "The Gaussian is defined by the\n" "function $f(x) = e^{-x^2}$.\n",
        )

        plotname = "test_03.png"
        plt.savefig(f"{self.actual_plots_dir}/{plotname}")
        # Uncomment line below to update expected image
        # plt.savefig(f"{self.expected_plots_dir}/{plotname}")
        self.assertImageEqual(
            f"{self.actual_plots_dir}/{plotname}",
            f"{self.expected_plots_dir}/{plotname}"
        )

    def test_enlarge(self):
        """test if enlarge parameter results in expected output"""

        plt.clf()
        plt.plot(self.x, self.y)
        atlasify("Internal", enlarge=1.5)

        plotname = "test_04.png"
        plt.savefig(f"{self.actual_plots_dir}/{plotname}")
        # Uncomment line below to update expected image
        # plt.savefig(f"{self.expected_plots_dir}/{plotname}")
        self.assertImageEqual(
            f"{self.actual_plots_dir}/{plotname}",
            f"{self.expected_plots_dir}/{plotname}"
        )

    def test_figure_api(self):
        """test if atlasify also works as expected with matplotlib.figure API"""

        fig = Figure()
        ax = fig.subplots()

        ax.plot(self.x, self.y)
        atlasify(
            atlas="Internal",
            subtext="The Gaussian is defined by the\n" "function $f(x) = e^{-x^2}$.\n",
            axes=ax,
        )

        plotname = "test_05.png"
        fig.savefig(f"{self.actual_plots_dir}/{plotname}")
        # Uncomment line below to update expected image
        # fig.savefig(f"{self.expected_plots_dir}/{plotname}")
        self.assertImageEqual(
            f"{self.actual_plots_dir}/{plotname}",
            f"{self.expected_plots_dir}/{plotname}"
        )

    def test_font_size_change(self):
        """test if font size works"""

        fig = Figure()
        ax = fig.subplots()

        ax.plot(self.x, self.y)
        atlasify(
            atlas="Internal",
            subtext="The Gaussian is defined by the\n" "function $f(x) = e^{-x^2}$.\n",
            axes=ax,
            font_size=12,
            label_font_size=12,
            sub_font_size=10,
        )

        plotname = "test_06.png"
        fig.savefig(f"{self.actual_plots_dir}/{plotname}")
        # Uncomment line below to update expected image
        # fig.savefig(f"{self.expected_plots_dir}/{plotname}")
        self.assertImageEqual(
            f"{self.actual_plots_dir}/{plotname}",
            f"{self.expected_plots_dir}/{plotname}"
        )

    def test_save_as_pdf(self):
        """test if atlasify also works as expected when saving to pdf"""

        fig = Figure()
        ax = fig.subplots()

        ax.plot(self.x, self.y)
        atlasify(
            atlas="Internal",
            subtext="This is a test in .pdf format",
            axes=ax,
            font_size=12,
            label_font_size=12,
            sub_font_size=10,
        )

        plotname = "test_07.pdf"
        fig.savefig(f"{self.actual_plots_dir}/{plotname}")
        # Uncomment line below to update expected image
        # fig.savefig(f"{self.expected_plots_dir}/{plotname}")
        self.assertImageEqual(
            f"{self.actual_plots_dir}/{plotname}",
            f"{self.expected_plots_dir}/{plotname}"
        )

    def test_log_scale(self):
        """test if logscale axes are also adjusted correctly"""

        fig = Figure()
        (ax1, ax2) = fig.subplots(2)

        x = np.linspace(0.1, 10, 100)
        ax1.plot(x, np.exp(x), label="exp(x)")
        ax2.plot(x, np.log(x), label="log(x)")

        ax1.set_yscale("log")
        ax2.set_xscale("log")
        ax1.set_xlabel("x")
        ax2.set_xlabel("x")
        ax1.legend(loc="upper right")
        ax2.legend(loc="upper right")

        atlasify(subtext="unit test with y-scale log", axes=ax1, enlarge=15)
        atlasify(subtext="unit test with x-scale log", axes=ax2, enlarge=1.5)

        plotname = "test_08.png"
        fig.savefig(f"{self.actual_plots_dir}/{plotname}")
        # Uncomment line below to update expected image
        # fig.savefig(f"{self.expected_plots_dir}/{plotname}")
        self.assertImageEqual(
            f"{self.actual_plots_dir}/{plotname}",
            f"{self.expected_plots_dir}/{plotname}"
        )

    def test_font_size_change_style_class(self):
        """Test if font size works with style class"""

        atlas_style = AtlasStyle(
            atlas="Internal",
            font_size=12,
            label_font_size=12,
            sub_font_size=10,
        )

        fig = Figure()
        ax = fig.subplots()

        ax.plot(self.x, self.y)
        atlas_style.apply(
            subtext="The Gaussian is defined by the\n" "function $f(x) = e^{-x^2}$.\n",
            axes=ax,
        )

        plotname = "test_06.png"  # Reuse expected image
        fig.savefig(f"{self.actual_plots_dir}/{plotname}")
        # Uncomment line below to update expected image
        # fig.savefig(f"{self.expected_plots_dir}/{plotname}")
        self.assertImageEqual(
            f"{self.actual_plots_dir}/{plotname}",
            f"{self.expected_plots_dir}/{plotname}"
        )
