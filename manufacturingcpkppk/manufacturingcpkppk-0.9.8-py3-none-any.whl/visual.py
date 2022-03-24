import logging
from typing import List
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from matplotlib.axis import Axis
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
import scipy.stats as stats
from plotly.graph_objs.layout import YAxis, XAxis, Margin
from manufacturingcpkppk.analysis import calc_ppk, control_beyond_limits, \
    control_zone_a, control_zone_b, control_zone_c, control_zone_trend, \
    control_zone_mixture, control_zone_stratification, control_zone_overcontrol
from manufacturingcpkppk.util import coerce

_logger = logging.getLogger(__name__)


def ahamdppk_plot(data: (List[int], List[float], pd.Series, np.array),
                  upper_control_limit: (int, float), lower_control_limit: (int, float),
                  threshold_percent: float = 0.001,
                  ax: Axis = None):
    """
    Shows the statistical distribution of the data along with CPK and limits.

    :param data: a list, pandas.Series, or numpy.array representing the data set
    :param upper_control_limit: an integer or float which represents the upper control limit, commonly called the UCL
    :param lower_control_limit: an integer or float which represents the upper control limit, commonly called the UCL
    :param threshold_percent: the threshold at which % of units above/below the number will display on the plot
    :param ax: an instance of matplotlig.axis.Axis
    :return: None
    """

    data = coerce(data)
    mean = data.mean()
    std = data.std()

    if ax is None:
        fig, ax = plt.subplots()

    ax.hist(data, density=True, label='data', alpha=0.3)
    x = np.linspace(mean - 4 * std, mean + 4 * std, 100)
    pdf = stats.norm.pdf(x, mean, std)
    ax.plot(x, pdf, label='normal fit', alpha=0.7)

    fig1 = go.Figure()
    fig1.update_layout(

        font=dict(
            family="Courier New, monospace",
            # size=40,
            color="RebeccaPurple"
        )
    )

    fig1.add_trace(
        go.Scatter(
            x=x,
            y=pdf
            , xaxis='x1', name="Normal Fit"))
    fig1.add_trace(
        go.Scatter(
            x=x[np.where(x > upper_control_limit)][::-1],
            y=pdf
            , xaxis='x1', fill='tozeroy', fillcolor='rgba(255, 0, 0, 0.5)', name="Upper Limit"))
    fig1.add_trace(
        go.Scatter(
            x=x[np.where(x < lower_control_limit)],
            y=pdf
            , xaxis='x1', fill='tozeroy', fillcolor='rgba(255, 0, 0, 0.5)', name="Lower Limit"))

    fig1.add_trace(go.Histogram(x=data, histnorm='probability density', xaxis='x1', marker_color='rgba(255, 255, 255)',
                                opacity=0.5, name="Data"))
    print(type(x))
    lst = [mean] * pdf.size

    # fig1.add_trace(go.Scatter(x=[mean, mean],y=[pdf,pdf] ,mode="lines", name="SIGNAL"))

    # fig1.add_trace(
    #     go.Scatter(x=[mean, mean], y=[bottom*1.5,top*1.5], xaxis='x2'),
    # )
    # fig1.add_trace(
    #     go.Scatter(x=[mean + std, mean + std], y=[bottom * 1.5, top * 1.5], xaxis='x2'),
    # )

    fig1.add_vline(x=mean, line_width=3, line_dash="dash", line_color="blue", opacity=0.3)
    fig1.add_annotation(text="\u03BC", x=mean, y=1, showarrow=False, yref='paper', )
    fig1.add_vline(x=mean + std, line_width=3, line_dash="dash", line_color="blue", opacity=0.3)
    fig1.add_annotation(text="\u03C3", x=mean + std, y=1, showarrow=False, yref='paper', )
    fig1.add_vline(x=mean - std, line_width=3, line_dash="dash", line_color="blue", opacity=0.3)
    fig1.add_annotation(text="-\u03C3", x=mean - std, y=1, showarrow=False, yref='paper', )
    fig1.add_vline(x=mean + 2 * std, line_width=3, line_dash="dash", line_color="blue", opacity=0.3)
    fig1.add_annotation(text="2\u03C3", x=mean + 2 * std, y=1, showarrow=False, yref='paper', )
    fig1.add_vline(x=mean - 2 * std, line_width=3, line_dash="dash", line_color="blue", opacity=0.3)
    fig1.add_annotation(text="-2\u03C3", x=mean - 2 * std, y=1, showarrow=False, yref='paper', )
    fig1.add_vline(x=mean + 3 * std, line_width=3, line_dash="dash", line_color="blue", opacity=0.3)
    fig1.add_annotation(text="3\u03C3", x=mean + 3 * std, y=1, showarrow=False, yref='paper', )
    fig1.add_vline(x=mean - 3 * std, line_width=3, line_dash="dash", line_color="blue", opacity=0.3)
    fig1.add_annotation(text="-3\u03C3", x=mean - 3 * std, y=1, showarrow=False, yref='paper', )

    bottom, top = ax.get_ylim()

    ax.axvline(mean, linestyle='--')
    ax.text(mean, top * 1.01, s='$\mu$', ha='center')

    ax.axvline(mean + std, alpha=0.6, linestyle='--')
    ax.text(mean + std, top * 1.01, s='$\sigma$', ha='center')

    ax.axvline(mean - std, alpha=0.6, linestyle='--')
    ax.text(mean - std, top * 1.01, s='$-\sigma$', ha='center')

    ax.axvline(mean + 2 * std, alpha=0.4, linestyle='--')
    ax.text(mean + 2 * std, top * 1.01, s='$2\sigma$', ha='center')

    ax.axvline(mean - 2 * std, alpha=0.4, linestyle='--')
    ax.text(mean - 2 * std, top * 1.01, s='-$2\sigma$', ha='center')

    ax.axvline(mean + 3 * std, alpha=0.2, linestyle='--')
    ax.text(mean + 3 * std, top * 1.01, s='$3\sigma$', ha='center')

    ax.axvline(mean - 3 * std, alpha=0.2, linestyle='--')
    ax.text(mean - 3 * std, top * 1.01, s='-$3\sigma$', ha='center')

    ax.fill_between(x, pdf, where=x < lower_control_limit, facecolor='red', alpha=0.5)
    ax.fill_between(x, pdf, where=x > upper_control_limit, facecolor='red', alpha=0.5)

    lower_percent = 100.0 * stats.norm.cdf(lower_control_limit, mean, std)
    lower_percent_text = f'{lower_percent:.02f}% < LCL' if lower_percent > threshold_percent else None

    higher_percent = 100.0 - 100.0 * stats.norm.cdf(upper_control_limit, mean, std)
    higher_percent_text = f'{higher_percent:.02f}% > UCL' if higher_percent > threshold_percent else None

    left, right = ax.get_xlim()
    bottom, top = ax.get_ylim()
    cpk = calc_ppk(data, upper_control_limit=upper_control_limit, lower_control_limit=lower_control_limit)

    lower_sigma_level = (mean - lower_control_limit) / std
    if lower_sigma_level < 6.0:
        ax.axvline(lower_control_limit, color='red', alpha=0.25, label='limits')
        ax.text(lower_control_limit, top * 0.95, s=f'-{lower_sigma_level:.01f}\u03C3', ha='center')
        fig1.add_vline(x=lower_control_limit, line_width=3, line_color="red", opacity=0.25)
        fig1.add_annotation(text=f'-{lower_sigma_level:.01f}\u03C3', x=lower_control_limit, y=0.85, showarrow=False,
                            yref='paper', )
    else:
        ax.text(left, top * 0.95, s=f'limit > $-6\sigma$', ha='left')
        fig1.add_annotation(text=f'-{lower_sigma_level:.01f}\u03C3', x=left,
                            y=0.85, showarrow=False,
                            yref='paper', )

    upper_sigma_level = (upper_control_limit - mean) / std
    if upper_sigma_level < 6.0:
        ax.axvline(upper_control_limit, color='red', alpha=0.25)
        ax.text(upper_control_limit, top * 0.95, s=f'{upper_sigma_level:.01f}\u03C3', ha='center')
        fig1.add_vline(x=upper_control_limit, line_width=3, line_color="red", opacity=0.25)
        fig1.add_annotation(text=f'-{upper_control_limit:.01f}\u03C3', x=upper_control_limit,
                            y=0.85, showarrow=False,
                            yref='paper', )
    else:
        ax.text(right, top * 0.95, s=f'limit > $6\sigma$', ha='right')
        fig1.add_annotation(text=f'-{upper_control_limit:.01f}\u03C3', x=left,
                            y=0.85, showarrow=False,
                            yref='paper', )

    strings = [f'Ppk = {cpk:.02f}']

    strings.append(f'\u03BC = {mean:.3g}')
    strings.append(f'\u03C3 = {std:.3g}')

    if lower_percent_text:
        strings.append(lower_percent_text)
    if higher_percent_text:
        strings.append(higher_percent_text)
    print('<br>'.join(strings))
    props = dict(boxstyle='round', facecolor='white', alpha=0.75, edgecolor='grey')
    ax.text(right - (right - left) * 0.05, 0.85 * top, '\n'.join(strings), bbox=props, ha='right', va='top')
    fig1.add_annotation(text='<br>'.join(strings),

                        align='left',

                        showarrow=False,
                        xref='paper',
                        yref='paper',
                        x=1 - (1 - 0) * 0.05,
                        y=0.85,
                        bordercolor='black',
                        borderwidth=1)

    ax.legend(loc='lower right')

    return fig1


def ppk_plot(data: (List[int], List[float], pd.Series, np.array),
             upper_control_limit: (int, float), lower_control_limit: (int, float),
             threshold_percent: float = 0.001,
             ax: Axis = None):
    """
    Shows the statistical distribution of the data along with CPK and limits.

    :param data: a list, pandas.Series, or numpy.array representing the data set
    :param upper_control_limit: an integer or float which represents the upper control limit, commonly called the UCL
    :param lower_control_limit: an integer or float which represents the upper control limit, commonly called the UCL
    :param threshold_percent: the threshold at which % of units above/below the number will display on the plot
    :param ax: an instance of matplotlig.axis.Axis
    :return: None
    """

    data = coerce(data)
    mean = data.mean()
    std = data.std()

    if ax is None:
        fig, ax = plt.subplots()

    ax.hist(data, density=True, label='data', alpha=0.3)
    x = np.linspace(mean - 4 * std, mean + 4 * std, 100)
    pdf = stats.norm.pdf(x, mean, std)
    ax.plot(x, pdf, label='normal fit', alpha=0.7)

    fig1 = go.Figure()
    fig1.update_layout(

        font=dict(
            family="Courier New, monospace",
            color="RebeccaPurple"
        )
    )

    fig1.add_trace(
        go.Scatter(
            x=x,
            y=pdf
            , xaxis='x1', name="Normal Fit"))
    fig1.add_trace(
        go.Scatter(
            x=x[np.where(x > upper_control_limit)][::-1],
            y=pdf
            , xaxis='x1', fill='tozeroy', fillcolor='rgba(255, 0, 0, 0.5)', name="Upper Limit"))
    fig1.add_trace(
        go.Scatter(
            x=x[np.where(x < lower_control_limit)],
            y=pdf
            , xaxis='x1', fill='tozeroy', fillcolor='rgba(255, 0, 0, 0.5)', name="Lower Limit"))

    fig1.add_trace(go.Histogram(x=data, histnorm='probability density', xaxis='x1', marker_color='rgba(255, 255, 255)',
                                opacity=0.5, name="Data"))
    print(type(x))
    lst = [mean] * pdf.size

    # fig1.add_trace(go.Scatter(x=[mean, mean],y=[pdf,pdf] ,mode="lines", name="SIGNAL"))

    full_fig = fig1.full_figure_for_development()

    bottom, top = full_fig.layout.yaxis.range

    # fig1.add_trace(
    #     go.Scatter(x=[mean, mean], y=[bottom*1.5,top*1.5], xaxis='x2'),
    # )
    # fig1.add_trace(
    #     go.Scatter(x=[mean + std, mean + std], y=[bottom * 1.5, top * 1.5], xaxis='x2'),
    # )

    fig1.add_vline(x=mean, line_width=3, line_dash="dash", line_color="blue", opacity=0.3)
    fig1.add_annotation(text="\u03BC", font=dict(size=100, ), x=mean, y=1, showarrow=False, yref='paper', )
    fig1.add_vline(x=mean + std, line_width=3, line_dash="dash", line_color="blue", opacity=0.3)
    fig1.add_annotation(text="\u03C3", font=dict(size=100, ), x=mean + std, y=1, showarrow=False, yref='paper', )
    fig1.add_vline(x=mean - std, line_width=3, line_dash="dash", line_color="blue", opacity=0.3)
    fig1.add_annotation(text="-\u03C3", font=dict(size=100, ), x=mean - std, y=1, showarrow=False, yref='paper', )
    fig1.add_vline(x=mean + 2 * std, line_width=3, line_dash="dash", line_color="blue", opacity=0.3)
    fig1.add_annotation(text="2\u03C3", font=dict(size=100, ), x=mean + 2 * std, y=1, showarrow=False, yref='paper', )
    fig1.add_vline(x=mean - 2 * std, line_width=3, line_dash="dash", line_color="blue", opacity=0.3)
    fig1.add_annotation(text="-2\u03C3", font=dict(size=100, ), x=mean - 2 * std, y=1, showarrow=False, yref='paper', )
    fig1.add_vline(x=mean + 3 * std, line_width=3, line_dash="dash", line_color="blue", opacity=0.3)
    fig1.add_annotation(text="3\u03C3", font=dict(size=100, ), x=mean + 3 * std, y=1, showarrow=False, yref='paper', )
    fig1.add_vline(x=mean - 3 * std, line_width=3, line_dash="dash", line_color="blue", opacity=0.3)
    fig1.add_annotation(text="-3\u03C3", font=dict(size=100, ), x=mean - 3 * std, y=1, showarrow=False, yref='paper', )

    fig1.update_yaxes(range=[bottom, top])

    bottom, top = ax.get_ylim()

    ax.axvline(mean, linestyle='--')
    ax.text(mean, top * 1.01, s='$\mu$', ha='center')

    ax.axvline(mean + std, alpha=0.6, linestyle='--')
    ax.text(mean + std, top * 1.01, s='$\sigma$', ha='center')

    ax.axvline(mean - std, alpha=0.6, linestyle='--')
    ax.text(mean - std, top * 1.01, s='$-\sigma$', ha='center')

    ax.axvline(mean + 2 * std, alpha=0.4, linestyle='--')
    ax.text(mean + 2 * std, top * 1.01, s='$2\sigma$', ha='center')

    ax.axvline(mean - 2 * std, alpha=0.4, linestyle='--')
    ax.text(mean - 2 * std, top * 1.01, s='-$2\sigma$', ha='center')

    ax.axvline(mean + 3 * std, alpha=0.2, linestyle='--')
    ax.text(mean + 3 * std, top * 1.01, s='$3\sigma$', ha='center')

    ax.axvline(mean - 3 * std, alpha=0.2, linestyle='--')
    ax.text(mean - 3 * std, top * 1.01, s='-$3\sigma$', ha='center')

    ax.fill_between(x, pdf, where=x < lower_control_limit, facecolor='red', alpha=0.5)
    ax.fill_between(x, pdf, where=x > upper_control_limit, facecolor='red', alpha=0.5)

    lower_percent = 100.0 * stats.norm.cdf(lower_control_limit, mean, std)
    lower_percent_text = f'{lower_percent:.02f}% < LCL' if lower_percent > threshold_percent else None

    higher_percent = 100.0 - 100.0 * stats.norm.cdf(upper_control_limit, mean, std)
    higher_percent_text = f'{higher_percent:.02f}% > UCL' if higher_percent > threshold_percent else None

    left, right = ax.get_xlim()
    bottom, top = ax.get_ylim()
    cpk = calc_ppk(data, upper_control_limit=upper_control_limit, lower_control_limit=lower_control_limit)

    lower_sigma_level = (mean - lower_control_limit) / std
    if lower_sigma_level < 6.0:
        ax.axvline(lower_control_limit, color='red', alpha=0.25, label='limits')
        ax.text(lower_control_limit, top * 0.95, s=f'$-{lower_sigma_level:.01f}\sigma$', ha='center')
        fig1.add_vline(x=lower_control_limit, line_width=3, line_color="red", opacity=0.25)
        fig1.add_annotation(text=f'$-{lower_sigma_level:.01f}\sigma$', font=dict(size=100, ), x=lower_control_limit,
                            y=1, showarrow=False,
                            yref='paper', )
    else:
        ax.text(left, top * 0.95, s=f'limit > $-6\sigma$', ha='left')
        fig1.add_annotation(text=f'$-{lower_sigma_level:.01f}\sigma$', font=dict(size=100, ), x=left,
                            y=1, showarrow=False,
                            yref='paper', )

    upper_sigma_level = (upper_control_limit - mean) / std
    if upper_sigma_level < 6.0:
        ax.axvline(upper_control_limit, color='red', alpha=0.25)
        ax.text(upper_control_limit, top * 0.95, s=f'${upper_sigma_level:.01f}\sigma$', ha='center')
        fig1.add_vline(x=upper_control_limit, line_width=3, line_color="red", opacity=0.25)
        fig1.add_annotation(text=f'$-{upper_control_limit:.01f}\sigma$', font=dict(size=100), x=upper_control_limit,
                            y=1, showarrow=False,
                            yref='paper', )
    else:
        ax.text(right, top * 0.95, s=f'limit > $6\sigma$', ha='right')
        fig1.add_annotation(text=f'$-{upper_control_limit:.01f}\sigma$', font=dict(size=100, ), x=left,
                            y=1, showarrow=False,
                            yref='paper', )

    strings = [f'Ppk = {cpk:.02f}']

    strings.append(f'\u03BC = {mean:.3g}')
    strings.append(f'\u03C3 = {std:.3g}')

    if lower_percent_text:
        strings.append(lower_percent_text)
    if higher_percent_text:
        strings.append(higher_percent_text)
    print('<br>'.join(strings))
    props = dict(boxstyle='round', facecolor='white', alpha=0.75, edgecolor='grey')
    ax.text(right - (right - left) * 0.05, 0.85 * top, '\n'.join(strings), bbox=props, ha='right', va='top')
    fig1.add_annotation(text='<br>'.join(strings), width=full_fig.layout.width * 0.5,
                        height=full_fig.layout.height * 0.5,

                        align='left',

                        showarrow=False,
                        xref='paper',
                        yref='paper',
                        x=1 - (1 - 0) * 0.05,
                        y=0.85,
                        bordercolor='black',
                        borderwidth=1)

    ax.legend(loc='lower right')


def cpk_plot(data: (List[int], List[float], pd.Series, np.array),
             upper_control_limit: (int, float), lower_control_limit: (int, float),
             subgroup_size: int = 30, max_subgroups: int = 10,
             axs: List[Axis] = None):
    """
    Boxplot the Cpk in subgroups os size `subgroup_size`.

    :param data: a list, pandas.Series, or numpy.array representing the data set
    :param upper_control_limit: an integer or float which represents the upper control limit, commonly called the UCL
    :param lower_control_limit: an integer or float which represents the upper control limit, commonly called the UCL
    :param subgroup_size: the number of samples to include in each subgroup
    :param max_subgroups: the maximum number of subgroups to display
    :param axs: two instances of matplotlib.axis.Axis
    :return: None
    """

    def chunk(seq, size):
        return (seq[pos:pos + size] for pos in range(0, len(seq), size))

    data = coerce(data)

    # todo: offer options of historical subgrouping, such as subgroup history = 'all' or 'recent', something that
    # allows a better historical subgrouping
    data_subgroups = []
    for i, c in enumerate(chunk(data[::-1], subgroup_size)):
        if i >= max_subgroups:
            break
        data_subgroups.append(c)

    data_subgroups = data_subgroups[::-1]

    if axs is None:
        fig, axs = plt.subplots(1, 2, sharey=True, gridspec_kw={'width_ratios': [4, 1]})

    ax0, ax1, *_ = axs

    bp = ax1.boxplot(data, patch_artist=True)

    ax1.set_title('Ppk')
    p0, p1 = bp['medians'][0].get_xydata()
    x0, _ = p0
    x1, _ = p1
    ax1.axhline(upper_control_limit, color='red', linestyle='--', zorder=-1, alpha=0.5)
    ax1.axhline(lower_control_limit, color='red', linestyle='--', zorder=-1, alpha=0.5)
    ax1.set_xticks([])
    ax1.grid(color='grey', alpha=0.3)
    bp['boxes'][0].set_facecolor('lightblue')

    bps = ax0.boxplot(data_subgroups, patch_artist=True)
    ax0.set_title(f'Cpk by Subgroups, Size={subgroup_size}')
    ax0.set_xticks([])
    ax0.axhline(upper_control_limit, color='red', linestyle='--', zorder=-1, alpha=0.5)
    ax0.axhline(lower_control_limit, color='red', linestyle='--', zorder=-1, alpha=0.5)
    ax0.grid(color='grey', alpha=0.3)

    for box in bps['boxes']:
        box.set_facecolor('lightblue')

    left, right = ax0.get_xlim()
    right_plus = (right - left) * 0.01 + right

    ax0.text(right_plus, upper_control_limit, s='UCL', color='red', va='center')
    ax0.text(right_plus, lower_control_limit, s='LCL', color='red', va='center')

    cpks = []
    for i, bp_median in enumerate(bps['medians']):
        cpk = calc_ppk(data_subgroups[i], upper_control_limit=upper_control_limit,
                       lower_control_limit=lower_control_limit)
        cpks.append(cpk)
    cpks = pd.Series(cpks)

    table = [f'${cpk:.02g}$' for cpk in cpks]
    ax0.table([table], rowLabels=['$Cpk$'])

    ppk = calc_ppk(data, upper_control_limit=upper_control_limit, lower_control_limit=lower_control_limit)
    ax1.table([[f'$Ppk: {ppk:.02g}$'], [f'$Cpk_{{av}}:{cpks.mean():.02g}$']])


def control_plot(data: (List[int], List[float], pd.Series, np.array),
                 upper_control_limit: (int, float), lower_control_limit: (int, float),
                 highlight_beyond_limits: bool = True, highlight_zone_a: bool = True,
                 highlight_zone_b: bool = True, highlight_zone_c: bool = True,
                 highlight_trend: bool = False, highlight_mixture: bool = False,
                 highlight_stratification: bool = False, highlight_overcontrol: bool = False,
                 ax: Axis = None):
    """
    Create a control plot based on the input data.

    :param data: a list, pandas.Series, or numpy.array representing the data set
    :param upper_control_limit: an integer or float which represents the upper control limit, commonly called the UCL
    :param lower_control_limit: an integer or float which represents the upper control limit, commonly called the UCL
    :param highlight_beyond_limits: True if points beyond limits are to be highlighted
    :param highlight_zone_a: True if points that are zone A violations are to be highlighted
    :param highlight_zone_b: True if points that are zone B violations are to be highlighted
    :param highlight_zone_c: True if points that are zone C violations are to be highlighted
    :param highlight_trend: True if points that are trend violations are to be highlighted
    :param highlight_mixture: True if points that are mixture violations are to be highlighted
    :param highlight_stratification: True if points that are stratification violations are to be highlighted
    :param highlight_overcontrol: True if points that are overcontrol violations are to be hightlighted
    :param ax: an instance of matplotlib.axis.Axis
    :return: None
    """

    data = coerce(data)

    if ax is None:
        fig, ax = plt.subplots()

    ax.plot(data)
    ax.set_title('Zone Control Chart')

    spec_range = (upper_control_limit - lower_control_limit) / 2
    spec_center = lower_control_limit + spec_range
    zone_c_upper_limit = spec_center + spec_range / 3
    zone_c_lower_limit = spec_center - spec_range / 3
    zone_b_upper_limit = spec_center + 2 * spec_range / 3
    zone_b_lower_limit = spec_center - 2 * spec_range / 3
    zone_a_upper_limit = spec_center + spec_range
    zone_a_lower_limit = spec_center - spec_range

    ax.axhline(spec_center, linestyle='--', color='red', alpha=0.6)
    ax.axhline(zone_c_upper_limit, linestyle='--', color='red', alpha=0.5)
    ax.axhline(zone_c_lower_limit, linestyle='--', color='red', alpha=0.5)
    ax.axhline(zone_b_upper_limit, linestyle='--', color='red', alpha=0.3)
    ax.axhline(zone_b_lower_limit, linestyle='--', color='red', alpha=0.3)
    ax.axhline(zone_a_upper_limit, linestyle='--', color='red', alpha=0.2)
    ax.axhline(zone_a_lower_limit, linestyle='--', color='red', alpha=0.2)

    left, right = ax.get_xlim()
    right_plus = (right - left) * 0.01 + right

    ax.text(right_plus, upper_control_limit, s='UCL', va='center')
    ax.text(right_plus, lower_control_limit, s='LCL', va='center')

    ax.text(right_plus, (spec_center + zone_c_upper_limit) / 2, s='Zone C', va='center')
    ax.text(right_plus, (spec_center + zone_c_lower_limit) / 2, s='Zone C', va='center')
    ax.text(right_plus, (zone_b_upper_limit + zone_c_upper_limit) / 2, s='Zone B', va='center')
    ax.text(right_plus, (zone_b_lower_limit + zone_c_lower_limit) / 2, s='Zone B', va='center')
    ax.text(right_plus, (zone_a_upper_limit + zone_b_upper_limit) / 2, s='Zone A', va='center')
    ax.text(right_plus, (zone_a_lower_limit + zone_b_lower_limit) / 2, s='Zone A', va='center')

    plot_params = {'alpha': 0.3, 'zorder': -10, 'markersize': 14}

    if highlight_beyond_limits:
        beyond_limits_violations = control_beyond_limits(data=data,
                                                         upper_control_limit=upper_control_limit,
                                                         lower_control_limit=lower_control_limit)
        if len(beyond_limits_violations):
            plot_params['zorder'] -= 1
            plot_params['markersize'] -= 1
            ax.plot(beyond_limits_violations, 'o', color='red', label='beyond limits', **plot_params)

    if highlight_zone_a:
        zone_a_violations = control_zone_a(data=data,
                                           upper_control_limit=upper_control_limit,
                                           lower_control_limit=lower_control_limit)
        if len(zone_a_violations):
            plot_params['zorder'] -= 1
            plot_params['markersize'] -= 1
            ax.plot(zone_a_violations, 'o', color='orange', label='zone a violations', **plot_params)

    if highlight_zone_b:
        zone_b_violations = control_zone_b(data=data,
                                           upper_control_limit=upper_control_limit,
                                           lower_control_limit=lower_control_limit)
        if len(zone_b_violations):
            plot_params['zorder'] -= 1
            plot_params['markersize'] -= 1
            ax.plot(zone_b_violations, 'o', color='blue', label='zone b violations', **plot_params)

    if highlight_zone_c:
        zone_c_violations = control_zone_c(data=data,
                                           upper_control_limit=upper_control_limit,
                                           lower_control_limit=lower_control_limit)
        if len(zone_c_violations):
            plot_params['zorder'] -= 1
            plot_params['markersize'] -= 1
            ax.plot(zone_c_violations, 'o', color='green', label='zone c violations', **plot_params)

    if highlight_trend:
        zone_trend_violations = control_zone_trend(data=data)
        if len(zone_trend_violations):
            plot_params['zorder'] -= 1
            plot_params['markersize'] -= 1
            ax.plot(zone_trend_violations, 'o', color='purple', label='trend violations', **plot_params)

    if highlight_mixture:
        zone_mixture_violations = control_zone_mixture(data=data,
                                                       upper_control_limit=upper_control_limit,
                                                       lower_control_limit=lower_control_limit)
        if len(zone_mixture_violations):
            plot_params['zorder'] -= 1
            plot_params['markersize'] -= 1
            ax.plot(zone_mixture_violations, 'o', color='brown', label='mixture violations', **plot_params)

    if highlight_stratification:
        zone_stratification_violations = control_zone_stratification(data=data,
                                                                     upper_control_limit=upper_control_limit,
                                                                     lower_control_limit=lower_control_limit)
        if len(zone_stratification_violations):
            plot_params['zorder'] -= 1
            plot_params['markersize'] -= 1
            ax.plot(zone_stratification_violations, 'o', color='orange', label='stratification violations',
                    **plot_params)

    if highlight_overcontrol:
        zone_overcontrol_violations = control_zone_overcontrol(data=data,
                                                               upper_control_limit=upper_control_limit,
                                                               lower_control_limit=lower_control_limit)
        if len(zone_overcontrol_violations):
            plot_params['zorder'] -= 1
            plot_params['markersize'] -= 1
            ax.plot(zone_overcontrol_violations, 'o', color='blue', label='overcontrol violations',
                    **plot_params)

    ax.legend()


def ahmadcpk_plot(data: (List[int], List[float], pd.Series, np.array),
                  upper_control_limit: (int, float), lower_control_limit: (int, float),
                  subgroup_size: int = 30, max_subgroups: int = 10,
                  axs: List[Axis] = None):
    """
    Boxplot the Cpk in subgroups os size `subgroup_size`.

    :param data: a list, pandas.Series, or numpy.array representing the data set
    :param upper_control_limit: an integer or float which represents the upper control limit, commonly called the UCL
    :param lower_control_limit: an integer or float which represents the upper control limit, commonly called the UCL
    :param subgroup_size: the number of samples to include in each subgroup
    :param max_subgroups: the maximum number of subgroups to display
    :param axs: two instances of matplotlib.axis.Axis
    :return: None
    """

    def chunk(seq, size):
        return (seq[pos:pos + size] for pos in range(0, len(seq), size))

    data = coerce(data)

    # todo: offer options of historical subgrouping, such as subgroup history = 'all' or 'recent', something that
    # allows a better historical subgrouping
    data_subgroups = []
    data_subgroups1 = []

    for i, c in enumerate(chunk(data[::-1], subgroup_size)):
        if i >= max_subgroups:
            break
        data_subgroups.append(c)
        data_subgroups1.append(list(c))

    data_subgroups = data_subgroups[::-1]

    if axs is None:
        fig, axs = plt.subplots(1, 2, sharey=True, gridspec_kw={'width_ratios': [4, 1]})

    ax0, ax1, *_ = axs
    fig1 = make_subplots(rows=2, cols=2, column_widths=[0.7, 0.3])

    fig1.update_layout(

        font=dict(
            family="Courier New, monospace",
            color="RebeccaPurple"
        )
    )

    bp = ax1.boxplot(data, patch_artist=True)

    fig1.add_trace(go.Box(
        y=data,
        name="Ppk",
        boxpoints=False,  # no data points
        marker_color='rgb(9,56,125)',
        line_color='rgb(9,56,125)'
    ), row=1, col=2)

    ax1.set_title('Ppk')
    p0, p1 = bp['medians'][0].get_xydata()
    x0, _ = p0
    x1, _ = p1
    ax1.axhline(upper_control_limit, color='red', linestyle='--', zorder=-1, alpha=0.5)
    ax1.axhline(lower_control_limit, color='red', linestyle='--', zorder=-1, alpha=0.5)
    ax1.set_xticks([])
    ax1.grid(color='grey', alpha=0.3)
    bp['boxes'][0].set_facecolor('lightblue')
    print(data_subgroups1)
    bps = ax0.boxplot(data_subgroups, patch_artist=True)
    # fig = px.box(data_subgroups)
    # fig.show()

    ax0.set_title(f'Cpk by Subgroups, Size={subgroup_size}')
    ax0.set_xticks([])
    ax0.axhline(upper_control_limit, color='red', linestyle='--', zorder=-1, alpha=0.5)
    ax0.axhline(lower_control_limit, color='red', linestyle='--', zorder=-1, alpha=0.5)
    ax0.grid(color='grey', alpha=0.3)

    for box in bps['boxes']:
        box.set_facecolor('lightblue')

    left, right = ax0.get_xlim()
    right_plus = (right - left) * 0.01 + right

    ax0.text(right_plus, upper_control_limit, s='UCL', color='red', va='center')
    ax0.text(right_plus, lower_control_limit, s='LCL', color='red', va='center')

    cpks = []
    for i, bp_median in enumerate(bps['medians']):
        cpk = calc_ppk(data_subgroups[i], upper_control_limit=upper_control_limit,
                       lower_control_limit=lower_control_limit)
        cpks.append(cpk)
    cpks = pd.Series(cpks)

    table = [f'${cpk:.02g}$' for cpk in cpks]

    ax0.table([table], rowLabels=['$Cpk$'])

    ppk = calc_ppk(data, upper_control_limit=upper_control_limit, lower_control_limit=lower_control_limit)
    ax1.table([[f'$Ppk: {ppk:.02g}$'], [f'$Cpk_{{av}}:{cpks.mean():.02g}$']])
    fig1.add_trace(go.Box(
        y=data_subgroups1[-1],
        name=f"Cpk={table[0]}",
        boxpoints=False,  # no data points
        marker_color='rgb(9,56,125)',
        line_color='rgb(9,56,125)'
    ), row=1, col=1)
    fig1.add_trace(go.Box(
        y=data_subgroups1[-2],
        name=f"Cpk={table[1]}",
        boxpoints=False,  # no data points
        marker_color='rgb(9,56,125)',
        line_color='rgb(9,56,125)'
    ), row=1, col=1)
    fig1.add_trace(go.Box(
        y=data_subgroups1[-3],
        name=f"Cpk={table[2]}",
        boxpoints=False,  # no data points
        marker_color='rgb(9,56,125)',
        line_color='rgb(9,56,125)'
    ), row=1, col=1)
    fig1.add_annotation(text='$Cpk$', x=-0.1,
                        y=0, showarrow=False,
                        yref='y domain', xref='x domain')

    return fig1


def ahmadcontrol_plot(data: (List[int], List[float], pd.Series, np.array),
                      upper_control_limit: (int, float), lower_control_limit: (int, float),
                      highlight_beyond_limits: bool = True, highlight_zone_a: bool = True,
                      highlight_zone_b: bool = True, highlight_zone_c: bool = True,
                      highlight_trend: bool = False, highlight_mixture: bool = False,
                      highlight_stratification: bool = False, highlight_overcontrol: bool = False,
                      ax: Axis = None):
    """
    Create a control plot based on the input data.

    :param data: a list, pandas.Series, or numpy.array representing the data set
    :param upper_control_limit: an integer or float which represents the upper control limit, commonly called the UCL
    :param lower_control_limit: an integer or float which represents the upper control limit, commonly called the UCL
    :param highlight_beyond_limits: True if points beyond limits are to be highlighted
    :param highlight_zone_a: True if points that are zone A violations are to be highlighted
    :param highlight_zone_b: True if points that are zone B violations are to be highlighted
    :param highlight_zone_c: True if points that are zone C violations are to be highlighted
    :param highlight_trend: True if points that are trend violations are to be highlighted
    :param highlight_mixture: True if points that are mixture violations are to be highlighted
    :param highlight_stratification: True if points that are stratification violations are to be highlighted
    :param highlight_overcontrol: True if points that are overcontrol violations are to be hightlighted
    :param ax: an instance of matplotlib.axis.Axis
    :return: None
    """

    data = coerce(data)

    if ax is None:
        fig, ax = plt.subplots()

    ax.plot(data)
    ax.set_title('Zone Control Chart')

    spec_range = (upper_control_limit - lower_control_limit) / 2
    spec_center = lower_control_limit + spec_range
    zone_c_upper_limit = spec_center + spec_range / 3
    zone_c_lower_limit = spec_center - spec_range / 3
    zone_b_upper_limit = spec_center + 2 * spec_range / 3
    zone_b_lower_limit = spec_center - 2 * spec_range / 3
    zone_a_upper_limit = spec_center + spec_range
    zone_a_lower_limit = spec_center - spec_range

    ax.axhline(spec_center, linestyle='--', color='red', alpha=0.6)
    ax.axhline(zone_c_upper_limit, linestyle='--', color='red', alpha=0.5)
    ax.axhline(zone_c_lower_limit, linestyle='--', color='red', alpha=0.5)
    ax.axhline(zone_b_upper_limit, linestyle='--', color='red', alpha=0.3)
    ax.axhline(zone_b_lower_limit, linestyle='--', color='red', alpha=0.3)
    ax.axhline(zone_a_upper_limit, linestyle='--', color='red', alpha=0.2)
    ax.axhline(zone_a_lower_limit, linestyle='--', color='red', alpha=0.2)

    left, right = ax.get_xlim()
    right_plus = (right - left) * 0.01 + right

    ax.text(right_plus, upper_control_limit, s='UCL', va='center')
    ax.text(right_plus, lower_control_limit, s='LCL', va='center')

    ax.text(right_plus, (spec_center + zone_c_upper_limit) / 2, s='Zone C', va='center')
    ax.text(right_plus, (spec_center + zone_c_lower_limit) / 2, s='Zone C', va='center')
    ax.text(right_plus, (zone_b_upper_limit + zone_c_upper_limit) / 2, s='Zone B', va='center')
    ax.text(right_plus, (zone_b_lower_limit + zone_c_lower_limit) / 2, s='Zone B', va='center')
    ax.text(right_plus, (zone_a_upper_limit + zone_b_upper_limit) / 2, s='Zone A', va='center')
    ax.text(right_plus, (zone_a_lower_limit + zone_b_lower_limit) / 2, s='Zone A', va='center')

    plot_params = {'alpha': 0.3, 'zorder': -10, 'markersize': 14}

    if highlight_beyond_limits:
        beyond_limits_violations = control_beyond_limits(data=data,
                                                         upper_control_limit=upper_control_limit,
                                                         lower_control_limit=lower_control_limit)
        if len(beyond_limits_violations):
            plot_params['zorder'] -= 1
            plot_params['markersize'] -= 1
            ax.plot(beyond_limits_violations, 'o', color='red', label='beyond limits', **plot_params)

    if highlight_zone_a:
        zone_a_violations = control_zone_a(data=data,
                                           upper_control_limit=upper_control_limit,
                                           lower_control_limit=lower_control_limit)
        if len(zone_a_violations):
            plot_params['zorder'] -= 1
            plot_params['markersize'] -= 1
            ax.plot(zone_a_violations, 'o', color='orange', label='zone a violations', **plot_params)

    if highlight_zone_b:
        zone_b_violations = control_zone_b(data=data,
                                           upper_control_limit=upper_control_limit,
                                           lower_control_limit=lower_control_limit)
        if len(zone_b_violations):
            plot_params['zorder'] -= 1
            plot_params['markersize'] -= 1
            ax.plot(zone_b_violations, 'o', color='blue', label='zone b violations', **plot_params)

    if highlight_zone_c:
        zone_c_violations = control_zone_c(data=data,
                                           upper_control_limit=upper_control_limit,
                                           lower_control_limit=lower_control_limit)
        if len(zone_c_violations):
            plot_params['zorder'] -= 1
            plot_params['markersize'] -= 1
            ax.plot(zone_c_violations, 'o', color='green', label='zone c violations', **plot_params)

    if highlight_trend:
        zone_trend_violations = control_zone_trend(data=data)
        if len(zone_trend_violations):
            plot_params['zorder'] -= 1
            plot_params['markersize'] -= 1
            ax.plot(zone_trend_violations, 'o', color='purple', label='trend violations', **plot_params)

    if highlight_mixture:
        zone_mixture_violations = control_zone_mixture(data=data,
                                                       upper_control_limit=upper_control_limit,
                                                       lower_control_limit=lower_control_limit)
        if len(zone_mixture_violations):
            plot_params['zorder'] -= 1
            plot_params['markersize'] -= 1
            ax.plot(zone_mixture_violations, 'o', color='brown', label='mixture violations', **plot_params)

    if highlight_stratification:
        zone_stratification_violations = control_zone_stratification(data=data,
                                                                     upper_control_limit=upper_control_limit,
                                                                     lower_control_limit=lower_control_limit)
        if len(zone_stratification_violations):
            plot_params['zorder'] -= 1
            plot_params['markersize'] -= 1
            ax.plot(zone_stratification_violations, 'o', color='orange', label='stratification violations',
                    **plot_params)

    if highlight_overcontrol:
        zone_overcontrol_violations = control_zone_overcontrol(data=data,
                                                               upper_control_limit=upper_control_limit,
                                                               lower_control_limit=lower_control_limit)
        if len(zone_overcontrol_violations):
            plot_params['zorder'] -= 1
            plot_params['markersize'] -= 1
            ax.plot(zone_overcontrol_violations, 'o', color='blue', label='overcontrol violations',
                    **plot_params)

    ax.legend()
