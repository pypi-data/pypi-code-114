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
import matplotlib
from matplotlib import pyplot as plt
from bgisimtool.mathfunc import gaussian
import numpy as np
from matplotlib.offsetbox import AnchoredText
from math import sqrt
matplotlib.use("TkAgg")
# ------------------------------------------------------------------------------
# function plot_vipmprofile_to_File
# ------------------------------------------------------------------------------
def plot_vipmprofile_to_File(histogram, filename,
                             fit_param=None, expected_value=None, chi=None,
                             display_expected=False, exp_err=False, hide_a=False,
                             yerr=True, textbox_text_size=10, axis_text_size=15, legend_text_size=10,
                             brazil=False, displaytext=True, grid=False, pdf=True, png=False,
                             fit_color='red', model_color='darkorange', data_color='royalblue',
                             plot_residuals=False, residual_color='royalblue',
                             xlim=None, xlegend='Transverse position', unit="um"):
    xlegend = xlegend + f"[{unit}]"
    # ---------------------------
    # set global font size
    # ---------------------------
    font = {'size': axis_text_size}
    #plt.rc('text', usetex=True)
    plt.rc('font', **font)

    # ---------------------------
    # basic text box
    # ---------------------------
    textbox_text = ('Measured e- signal\n\n' +
                    'Mean : ' + '{:.3f}'.format(histogram.mean) + '\xB1' +
                    '{:.3f}'.format(histogram.mean_err) + '\n' +
                    'Stdev : ' + '{:.3f}'.format(histogram.stdev) + '\xB1' +
                    '{:.3f}'.format(histogram.stdev_err) + '\n' +
                    'Integral : ' + '{:.1f}'.format(histogram.integral) + '\n')

    # ---------------------------
    # Fit look
    # ---------------------------
    fit_linewidth = 1.5

    # ---------------------------
    # Histogram look
    # ---------------------------
    hist_marker_type = 'o'
    hist_marker_size = 1
    hist_capsize = 1
    hist_capthick = 0.8
    hist_line_width = 0.6

    # ---------------------------
    # create a figure
    # ---------------------------
    fig = plt.figure()
    # if we give the expected and we want to plot the residuals
    if plot_residuals and (expected_value is not None):
        ax_hist = plt.subplot2grid((4, 1), (0, 0), colspan=1, rowspan=3)
        ax_res = plt.subplot2grid((4, 1), (3, 0), colspan=1, rowspan=1)
    else:
        ax_hist = plt.subplot(1, 1, 1)
    # get the x_errorbars
    # divide by two because it's +- x_error_bar
    x_error_bar = (histogram._bin_edge[1:] - histogram._bin_edge[:-1]) / 2
    # ---------------------------
    # get the hist y error
    # ---------------------------
    if yerr:
        # get the error
        yerr_list = np.sqrt(histogram._bin_content)
        # plot the hist with error
        ax_hist.errorbar(histogram._bin_center, histogram._bin_content, xerr=x_error_bar, yerr=yerr_list,
                         fmt=hist_marker_type, lw=hist_line_width, ms=hist_marker_size,
                         capthick=hist_capthick, capsize=hist_capsize, label='Measured', color=data_color)
    else:
        # plot the hist without error
        ax_hist.errorbar(histogram._bin_center, histogram._bin_content, xerr=x_error_bar,
                         fmt=hist_marker_type, lw=hist_line_width, ms=hist_marker_size,
                         capthick=hist_capthick, capsize=hist_capsize, label='Measured', color=data_color)

    # ---------------------------
    # fit or not
    # ---------------------------
    if not(fit_param is None):
        # ---------------------------
        # get fit plot points
        # ---------------------------
        max_value = histogram._bin_center[-1]
        min_value = histogram._bin_center[0]
        x_vals = np.linspace(min_value, max_value, 1000)  # 1000 point is about 2 points per bin in worst case.. good enough
        # is it a fit with free param or just a normal fit
        if len(fit_param[0]) == 3:
            # no free param
            # get the gaussian fit points
            best_fit = gaussian(x_vals, *fit_param[0])
            # ---------------------------
            # add the fit info to the textbox
            # ---------------------------
            sigma = abs(fit_param[0][2])
            sigma_err = abs(fit_param[1][2])
            mean = fit_param[0][1]
            mean_err = fit_param[1][1]

            textbox_text += ('P0 : ' + '{:.1f}'.format(fit_param[0][0]) + '\xB1' + '{:.1f}'.format(fit_param[1][0]) + '\n' +
                             'P1 : ' + '{:.3f}'.format(mean) + '\xB1' + '{:.3f}'.format(mean_err) + '\n' +
                             'P2 : ' + '{:.3f}'.format(sigma) + '\xB1' + '{:.3f}'.format(sigma_err) + '\n')
        elif len(fit_param[0]) == 4:
            # with free param
            # get the gaussian fit points
            best_fit = gaussian(x_vals, fit_param[0][0], fit_param[0][1], fit_param[0][2])
            # ---------------------------
            # add the fit info to the textbox
            # ---------------------------
            sigma = abs(fit_param[0][2])
            sigma_err = abs(fit_param[1][2])
            mean = fit_param[0][1]
            mean_err = fit_param[1][1]
            free_par = fit_param[0][3]
            free_par_err = fit_param[1][3]

            textbox_text += ('P0 : ' + '{:.1f}'.format(fit_param[0][0]) + '\xB1' + '{:.1f}'.format(fit_param[1][0]) + '\n' +
                             'P1 : ' + '{:.3f}'.format(mean) + '\xB1' + '{:.3f}'.format(mean_err) + '\n' +
                             'P2 : ' + '{:.3f}'.format(sigma) + '\xB1' + '{:.3f}'.format(sigma_err) + '\n')
            if not hide_a:
                textbox_text += ('A : ' + '{:.3f}'.format(free_par) + '\xB1' + '{:.3f}'.format(free_par_err) + '\n')

        else:
            # if the size do not match 3 or 4, we stop
            raise ValueError('Fit parameters provided do not have the required number of position, expected 3 or 4')

        # plot the best fit
        ax_hist.plot(x_vals, best_fit, label='Beam Profile', lw=fit_linewidth, color=fit_color)

        # ---------------------------
        # get the 3 sigma interval
        # ---------------------------
        if brazil:
            # prepare confidence level curves
            nstd = 3  # to draw 3-sigma intervals
            popt_up = fit_param[0] + nstd * fit_param[1]
            # we keep the mean static
            popt_up[1] = fit_param[0][1]
            popt_dw = fit_param[0] - nstd * fit_param[1]
            popt_dw[1] = fit_param[0][1]
            fit_up = gaussian(x_vals, *popt_up[0:3])
            fit_dw = gaussian(x_vals, *popt_dw[0:3])

            # plot
            ax_hist.fill_between(x_vals, fit_up, best_fit, alpha=.25, label='3-sigma interval', facecolor='green')
            ax_hist.fill_between(x_vals, fit_dw, best_fit, alpha=.25, facecolor='green')

        # ---------------------------
        # chi2
        # ---------------------------
        if not(expected_value is None):
            # write textbox
            textbox_text += ('Chi2/ndf  : ' + '{:.1f}'.format(chi[0]) + '/' + str(chi[2]) + '\n' +
                             'Prob : ' + '{:.3f}'.format(chi[1]))
            # get the err
            exp_error = np.sqrt(expected_value)
            # display the expected
            if display_expected:
                # if the user request the error with it
                if exp_err:
                    # plot with err
                    ax_hist.errorbar(histogram._bin_center, expected_value, xerr=x_error_bar, yerr=exp_error,
                                     fmt=hist_marker_type, lw=hist_line_width, ms=hist_marker_size,
                                     capthick=hist_capthick, capsize=hist_capsize, label='Model', color=model_color)
                else:
                    # plot without err
                    ax_hist.errorbar(histogram._bin_center, expected_value, xerr=x_error_bar,
                                     fmt=hist_marker_type, lw=hist_line_width, ms=hist_marker_size,
                                     capthick=hist_capthick, capsize=hist_capsize, label='Model', color=model_color)
            # plot residuals
            if plot_residuals:
                residuals = np.array(histogram._bin_content) - np.array(expected_value)
                yerr_list = np.sqrt(histogram._bin_content)
                standardizedError = residuals / yerr_list
                ax_res.errorbar(histogram._bin_center, standardizedError, xerr=x_error_bar,
                                fmt=hist_marker_type, lw=hist_line_width, ms=hist_marker_size,
                                capthick=hist_capthick, capsize=hist_capsize, label='Residuals', color=residual_color)

    # ---------------------------
    # set the axis
    # ---------------------------
    if plot_residuals and (expected_value is not None):
        ax_hist.set_xticklabels([])
        ax_res.set_xlabel(xlegend)
        ax_res.set_ylabel('Standardised \n difference [a.u]')
        # ax_res.set_ylabel('Residuals [a.u]')
    else:
        ax_hist.set_xlabel(xlegend)
    ax_hist.set_ylabel('Counts [a.u]')
    ax_hist.grid(grid)

    if not(xlim is None):
        ax_hist.set_xlim(xlim)
        ax_res.set_xlim(xlim)

    # ---------------------------
    # Textbox placement
    # ---------------------------
    legend_pos = 'upper left'

    if abs(histogram.mean > 0.2):
        text = AnchoredText(textbox_text, loc=2, frameon=True, prop=dict(size=textbox_text_size))
        legend_pos = 'upper right'
    else:
        text = AnchoredText(textbox_text, loc=1, frameon=True, prop=dict(size=textbox_text_size))
        legend_pos = 'upper left'

    if displaytext:
        ax_hist.add_artist(text)
        ax_hist.legend(loc=legend_pos, prop={'size': legend_text_size})

    # ---------------------------
    # save to pdf
    # ---------------------------
    if pdf:
        saveName = filename + '.pdf'
        plt.savefig(saveName, bbox_inches='tight', pad_inches=0.2)
    if png:
        saveName = filename + '.png'
        plt.savefig(saveName, bbox_inches='tight', pad_inches=0.2)

    # kill the figure
    plt.close(fig)


