import copy
import numpy as np
import statistics
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

from steam_sdk.data import DataModel
from steam_sdk.data.DataRoxieParser import APIdata
from steam_sdk.parsers.ParserRoxie import get_conductor_corners
from steam_sdk.utils.misc import displayWaitAndClose, find_indices


def plotterModel(data, titles, labels, types, texts, size):
    """
        Default plotter for most standard and simple cases
    """

    # Define style
    selectedFont = _define_plot_style()

    fig, axs = plt.subplots(nrows=1, ncols=len(data), figsize=size)
    if len(data) == 1:
        axs = [axs]
    for ax, ty, d, ti, l, te in zip(axs, types, data, titles, labels, texts):
        if ty == 'scatter':
            plot = ax.scatter(d['x'], d['y'], s=2, c=d['z'], cmap='jet')  # =cm.get_cmap('jet'))
            if len(te["t"]) != 0:
                for x, y, z in zip(te["x"], te["y"], te["t"]):
                    ax.text(x, y, z)
        elif ty == 'plot':
            pass  # TODO make non scatter plots work. Some of non-scater plots are quite specific. Might be better off with a separate plotter
        ax.set_xlabel(l["x"], **selectedFont)
        ax.set_ylabel(l["y"], **selectedFont)
        ax.set_title(f'{ti}', **selectedFont)
        # ax.set_aspect('equal')
        # ax.figure.autofmt_xdate()
        cax = make_axes_locatable(ax).append_axes('right', size='5%', pad=0.05)
        cbar = fig.colorbar(plot, cax=cax, orientation='vertical')
        if len(l["z"]) != 0:
            cbar.set_label(l["z"], **selectedFont)
    plt.tight_layout()
    displayWaitAndClose(waitTimeBeforeMessage=.1, waitTimeAfterMessage=10)  # Show plots in Pycharm, wait a certain time, alert time is up, and close the window


# def plot_field(model_data: DataModel):
#     """
#     Plot magnetic field components of a coil
#     """
#     data = [{'x': model_data.x, 'y': model_data.y, 'z': model_data.I},
#             {'x': model_data.x, 'y': model_data.y, 'z': model_data.Bx},
#             {'x': model_data.x, 'y': model_data.y, 'z': model_data.By},
#             {'x': model_data.x, 'y': model_data.y, 'z': model_data.B}]
#     titles = ['Current [A]', 'Br [T]', 'Bz [T]', 'Bmod [T]']
#     labels = [{'x': "r (m)", 'y': "z (m)", 'z': ""}] * len(data)
#     types = ['scatter'] * len(data)
#     texts = [model_data.text] * len(data)
#     plotterModel(data, titles, labels, types, texts, (15, 5))
#
#
# def plot_strands_groups_layers(model_data: DataModel):
#     types = ['scatter'] * 4
#     data = [{'x': model_data.x, 'y': model_data.y, 'z': model_data.strandToHalfTurn},
#             {'x': model_data.x, 'y': model_data.y, 'z': model_data.strandToGroup},
#             {'x': model_data.x, 'y': model_data.y, 'z': model_data.halfTurnToTurn},
#             {'x': model_data.x, 'y': model_data.y, 'z': model_data.nS}]
#     titles = ['strandToHalfTurn', 'strandToGroup', 'halfTurnToTurn', 'Number of strands per half-turn']
#     labels = [{'x': "r (m)", 'y': "z (m)", 'z': "Half-turn [-]"},
#               {'x': "r (m)", 'y': "z (m)", 'z': "Group [-]"},
#               {'x': "r (m)", 'y': "z (m)", 'z': "Turn [-]"},
#               {'x': "r (m)", 'y': "z (m)", 'z': "Number of  strands per cable [-]"}]
#     t_ht = copy.deepcopy(model_data.text)
#     for ht in range(model_data.nHalfTurns):
#         t_ht['x'].append(model_data.x_ave[ht])
#         t_ht['y'].append(model_data.y_ave[ht])
#         t_ht['t'].append('{}'.format(ht + 1))
#     t_ng = copy.deepcopy(model_data.text)
#     for g in range(model_data.nGroups):
#         t_ng['x'].append(model_data.x_ave_group[g])
#         t_ng['y'].append(model_data.y_ave_group[g])
#         t_ng['t'].append('{}'.format(g + 1))
#     texts = [t_ht, t_ng, model_data.text, model_data.text]
#     plotterModel(data, titles, labels, types, texts, (15, 5))
#
#
# def plot_polarities(model_data: DataModel):
#     polarities_inStrand = np.zeros((1, model_data.nStrands), dtype=int)
#     polarities_inStrand = polarities_inStrand[0]
#     for g in range(1, model_data.nGroupsDefined + 1):
#         polarities_inStrand[np.where(model_data.strandToGroup == g)] = model_data.polarities_inGroup[g - 1]
#     data = [{'x': model_data.x, 'y': model_data.y, 'z': polarities_inStrand}]
#     titles = ['Current polarities']
#     labels = [{'x': "r (m)", 'y': "z (m)", 'z': "Polarity [-]"}]
#     types = ['scatter'] * len(data)
#     texts = [model_data.text] * len(data)
#     plotterModel(data, titles, labels, types, texts, (5, 5))
#
#
# def plot_half_turns(model_data: DataModel):
#     data = [{'x': model_data.x_ave, 'y': model_data.y_ave, 'z': model_data.HalfTurnToGroup},
#             {'x': model_data.x_ave, 'y': model_data.y_ave, 'z': model_data.HalfTurnToCoilSection},
#             {'x': model_data.x, 'y': model_data.y, 'z': model_data.strandToGroup},
#             {'x': model_data.x, 'y': model_data.y, 'z': model_data.strandToCoilSection}]
#     titles = ['HalfTurnToGroup', 'HalfTurnToCoilSection', 'StrandToGroup', 'StrandToCoilSection']
#     labels = [{'x': "r (m)", 'y': "z (m)", 'z': "Group [-]"},
#               {'x': "r (m)", 'y': "z (m)", 'z': "Coil section [-]"},
#               {'x': "r (m)", 'y': "z (m)", 'z': "Group [-]"},
#               {'x': "r (m)", 'y': "z (m)", 'z': "Coil Section [-]"}]
#     types = ['scatter'] * len(data)
#     texts = [model_data.text] * len(data)
#     plotterModel(data, titles, labels, types, texts, (15, 5))

# def plot_half_turns_NEW(model_data: DataModel, roxie_data: APIdata):
#     x_insulated, y_insulated, x_bare, y_bare, i_conductor, x_strand, y_strand, i_strand, strandToHalfTurn = get_conductor_corners(roxie_data)
#     x_ave, y_ave =  _get_conductor_centers(roxie_data)
#     data = [{'x': x_ave, 'y': model_data.y_ave, 'z': model_data.HalfTurnToGroup},
#             {'x': x_ave, 'y': model_data.y_ave, 'z': model_data.HalfTurnToCoilSection},
#             {'x': model_data.x, 'y': model_data.y, 'z': model_data.strandToGroup},
#             {'x': model_data.x, 'y': model_data.y, 'z': model_data.strandToCoilSection}]
#     titles = ['HalfTurnToGroup', 'HalfTurnToCoilSection', 'StrandToGroup', 'StrandToCoilSection']
#     labels = [{'x': "r (m)", 'y': "z (m)", 'z': "Group [-]"},
#               {'x': "r (m)", 'y': "z (m)", 'z': "Coil section [-]"},
#               {'x': "r (m)", 'y': "z (m)", 'z': "Group [-]"},
#               {'x': "r (m)", 'y': "z (m)", 'z': "Coil Section [-]"}]
#     types = ['scatter'] * len(data)
#     texts = [model_data.text] * len(data)
#     plotterModel(data, titles, labels, types, texts, (15, 5))
#
#
# def plot_nonlin_induct(model_data: DataModel):
#     f = plt.figure(figsize=(7.5, 5))
#     plt.plot(model_data.fL_I, model_data.fL_L, 'ro-')
#     plt.xlabel('Current [A]', **selectedFont)
#     plt.ylabel('Factor scaling nominal inductance [-]', **selectedFont)
#     plt.title('Differential inductance versus current', **selectedFont)
#     plt.xlim([0, model_data.I00 * 2])
#     plt.grid(True)
#     plt.rcParams.update({'font.size': 12})
#     displayWaitAndClose(waitTimeBeforeMessage=.1, waitTimeAfterMessage=10)


def plot_psu_and_trig(model_data: DataModel):
    selectedFont = _define_plot_style()

    ps = model_data.Power_Supply
    ee = model_data.Quench_Protection.Energy_Extraction
    qh = model_data.Quench_Protection.Quench_Heaters
    cl = model_data.Quench_Protection.CLIQ

    # Plot
    f = plt.figure(figsize=(5, 5))
    plt.plot([ps.t_off, ps.t_off],         [0, 1], 'k--', linewidth=4.0, label='t_PC')
    plt.plot([ee.t_trigger, ee.t_trigger], [0, 1], 'r--', linewidth=4.0, label='t_EE')
    plt.plot([cl.t_trigger, cl.t_trigger], [0, 1], 'g--', linewidth=4.0, label='t_CLIQ')
    plt.plot([np.min(qh.t_trigger), np.min(qh.t_trigger)], [0, 1], 'b:', linewidth=2.0, label='t_QH')
    plt.xlabel('Time [s]', **selectedFont)
    plt.ylabel('Trigger [-]', **selectedFont)
    plt.xlim([1E-4, model_data.Options_LEDET.time_vector.time_vector_params[-1]])
    plt.title('Power suppply and quench protection triggers', **selectedFont)
    plt.grid(True)
    plt.rcParams.update({'font.size': 12})
    plt.legend(loc='best')
    plt.tight_layout()
    displayWaitAndClose(waitTimeBeforeMessage=.1, waitTimeAfterMessage=10)


# def plot_quench_prop_and_resist(model_data: DataModel):
#     f = plt.figure(figsize=(16, 6))
#     plt.subplot(1, 4, 1)
#     # fig, ax = plt.subplots()
#     plt.scatter(model_data.x_ave * 1000, model_data.y_ave * 1000, s=2, c=model_data.vQ_iStartQuench)
#     plt.xlabel('x [mm]', **selectedFont)
#     plt.ylabel('y [mm]', **selectedFont)
#     plt.title('2D cross-section Quench propagation velocity', **selectedFont)
#     plt.set_cmap('jet')
#     plt.grid('minor', alpha=0.5)
#     cbar = plt.colorbar()
#     cbar.set_label('Quench velocity [m/s]', **selectedFont)
#     plt.rcParams.update({'font.size': 12})
#     # plt.axis('equal')
#
#     plt.subplot(1, 4, 2)
#     plt.scatter(model_data.x_ave * 1000, model_data.y_ave * 1000, s=2, c=model_data.rho_ht_10K)
#     plt.xlabel('x [mm]', **selectedFont)
#     plt.ylabel('y [mm]', **selectedFont)
#     plt.title('Resistivity', **selectedFont)
#     plt.set_cmap('jet')
#     plt.grid('minor', alpha=0.5)
#     cbar = plt.colorbar()
#     cbar.set_label('Resistivity [$\Omega$*m]', **selectedFont)
#     plt.rcParams.update({'font.size': 12})
#     # plt.axis('equal')
#
#     plt.subplot(1, 4, 3)
#     plt.scatter(model_data.x_ave * 1000, model_data.y_ave * 1000, s=2, c=model_data.r_el_ht_10K)
#     plt.xlabel('x [mm]', **selectedFont)
#     plt.ylabel('y [mm]', **selectedFont)
#     plt.title('Resistance per unit length', **selectedFont)
#     plt.set_cmap('jet')
#     plt.grid('minor', alpha=0.5)
#     cbar = plt.colorbar()
#     cbar.set_label('Resistance per unit length [$\Omega$/m]', **selectedFont)
#     plt.rcParams.update({'font.size': 12})
#     # plt.axis('equal')
#
#     plt.subplot(1, 4, 4)
#     plt.scatter(model_data.x_ave * 1000, model_data.y_ave * 1000, s=2, c=model_data.tQuenchDetection * 1e3)
#     plt.xlabel('x [mm]', **selectedFont)
#     plt.ylabel('y [mm]', **selectedFont)
#     plt.title('Approximate quench detection time', **selectedFont)
#     plt.set_cmap('jet')
#     plt.grid('minor', alpha=0.5)
#     cbar = plt.colorbar()
#     cbar.set_label('Time [ms]', **selectedFont)
#     plt.rcParams.update({'font.size': 12})
#     # plt.axis('equal')
#     displayWaitAndClose(waitTimeBeforeMessage=.1, waitTimeAfterMessage=10)
#
#
# def plot_q_prop_v(model_data: DataModel):
#     f = plt.figure(figsize=(16, 6))
#     plt.subplot(1, 2, 1)
#     plt.plot(model_data.mean_B_ht, model_data.vQ_iStartQuench, 'ko')
#     plt.xlabel('Average magnetic field in the half-turn [T]', **selectedFont)
#     plt.ylabel('Quench propagation velocity [m/s]', **selectedFont)
#     plt.title('Quench propagation velocity', **selectedFont)
#     plt.set_cmap('jet')
#     plt.grid('minor', alpha=0.5)
#     plt.rcParams.update({'font.size': 12})
#     plt.subplot(1, 2, 2)
#     plt.plot(model_data.mean_B_ht, model_data.tQuenchDetection * 1e3, 'ko')
#     plt.xlabel('Average magnetic field in the half-turn [T]', **selectedFont)
#     plt.ylabel('Approximate quench detection time [ms]', **selectedFont)
#     plt.title('Approximate quench detection time', **selectedFont)
#     plt.set_cmap('jet')
#     plt.grid('minor', alpha=0.5)
#     plt.rcParams.update({'font.size': 12})
#     displayWaitAndClose(waitTimeBeforeMessage=.1, waitTimeAfterMessage=10)
#
#
def plot_electrical_order(roxie_data: APIdata, el_order_half_turns, elPairs_GroupTogether, strandToGroup):
    selectedFont = _define_plot_style()

    # Load useful variables
    x_insulated, y_insulated, x_bare, y_bare, i_conductor, x_strand, y_strand, i_strand, strandToHalfTurn = get_conductor_corners(roxie_data)
    x_ave, y_ave =  _get_conductor_centers(roxie_data)
    x_ave_group, y_ave_group = _get_group_centers(roxie_data, strandToGroup)

    # Transform to arrays
    el_order_half_turns_Array = np.array(el_order_half_turns)
    elPairs_GroupTogether_Array = np.array(elPairs_GroupTogether)
    x_ave, y_ave = np.array(x_ave), np.array(y_ave)
    x_ave_group, y_ave_group = np.array(x_ave_group), np.array(y_ave_group)

    plt.figure(figsize=(16, 8))
    plt.subplot(1, 3, 1)
    plt.scatter(x_ave, y_ave, s=2, c=np.argsort(el_order_half_turns_Array))
    plt.xlabel('x [m]', **selectedFont)
    plt.ylabel('y [m]', **selectedFont)
    plt.title('Electrical order of the half-turns', **selectedFont)
    plt.set_cmap('jet')
    cbar = plt.colorbar()
    cbar.set_label('Electrical order [-]', **selectedFont)
    plt.rcParams.update({'font.size': 12})
    plt.axis('equal')
    # Plot
    plt.subplot(1, 3, 2)
    plt.plot(x_ave[el_order_half_turns_Array - 1], y_ave[el_order_half_turns_Array - 1], 'k')
    # plt.scatter(x_ave, y_ave, s=2, c=model_data.nS)
    plt.scatter(x_ave[el_order_half_turns_Array[0] - 1],
                y_ave[el_order_half_turns_Array[0] - 1], s=50, c='r',
                label='Positive lead')
    plt.scatter(x_ave[el_order_half_turns_Array[-1] - 1],
                y_ave[el_order_half_turns_Array[-1] - 1], s=50, c='b',
                label='Negative lead')
    plt.xlabel('x [m]', **selectedFont)
    plt.ylabel('y [m]', **selectedFont)
    plt.title('Electrical order of the half-turns', **selectedFont)
    plt.rcParams.update({'font.size': 12})
    plt.axis('equal')
    plt.legend(loc='lower left')
    # Plot
    plt.subplot(1, 3, 3)
    plt.plot(x_ave_group[elPairs_GroupTogether_Array[:,0]-1],y_ave_group[elPairs_GroupTogether_Array[:,1]-1],'b')
    plt.scatter(x_strand, y_strand, s=2, c='k')
    plt.scatter(x_ave_group, y_ave_group, s=10, c='r')
    plt.xlabel('x [m]', **selectedFont)
    plt.ylabel('y [m]', **selectedFont)
    plt.title('Electrical order of the groups (only go-lines)', **selectedFont)
    plt.rcParams.update({'font.size': 12})
    plt.axis('equal')
    displayWaitAndClose(waitTimeBeforeMessage=.1, waitTimeAfterMessage=10)
#
#
# def plot_heat_exchange_order(model_data: DataModel):
#     plt.figure(figsize=(10, 10))
#     # plot strand positions
#     plt.scatter(model_data.x, model_data.y, s=2, c='b')
#     # plot conductors
#     # for c, (cXPos, cYPos) in enumerate(zip(xPos, yPos)):
#     #     pt1, pt2, pt3, pt4 = (cXPos[0], cYPos[0]), (cXPos[1], cYPos[1]), (cXPos[2], cYPos[2]), (cXPos[3], cYPos[3])
#     #     line = plt.Polygon([pt1, pt2, pt3, pt4], closed=True, fill=True, facecolor='r', edgecolor='k', alpha=.25)
#     #     plt.gca().add_line(line)
#     # plot average conductor positions
#     # plt.scatter(x_ave, y_ave, s=10, c='r')
#     # plot heat exchange links along the cable narrow side
#     for i in range(len(model_data.iContactAlongHeight_From)):
#         plt.plot([model_data.x_ave[model_data.iContactAlongHeight_From_Array[i] - 1],
#                   model_data.x_ave[model_data.iContactAlongHeight_To_Array[i] - 1]],
#                  [model_data.y_ave[model_data.iContactAlongHeight_From_Array[i] - 1],
#                   model_data.y_ave[model_data.iContactAlongHeight_To_Array[i] - 1]], 'k')
#     # plot heat exchange links along the cable wide side
#     for i in range(len(model_data.iContactAlongWidth_From)):
#         plt.plot([model_data.x_ave[model_data.iContactAlongWidth_From_Array[i] - 1],
#                   model_data.x_ave[model_data.iContactAlongWidth_To_Array[i] - 1]],
#                  [model_data.y_ave[model_data.iContactAlongWidth_From_Array[i] - 1],
#                   model_data.y_ave[model_data.iContactAlongWidth_To_Array[i] - 1]], 'r')
#     # plot strands belonging to different conductor groups and clo ser to each other than max_distance
#     # for p in pairs_close:
#     #     if not strandToGroup[p[0]] == strandToGroup[p[1]]:
#     #         plt.plot([X[p[0], 0], X[p[1], 0]], [X[p[0], 1], X[p[1], 1]], c='g')
#     plt.xlabel('x [m]', **selectedFont)
#     plt.ylabel('y [m]', **selectedFont)
#     plt.title('Heat exchange order of the half-turns', **selectedFont)
#     plt.rcParams.update({'font.size': 12})
#     plt.axis('equal')
#     displayWaitAndClose(waitTimeBeforeMessage=.1, waitTimeAfterMessage=10)


def plot_power_supl_contr(model_data: DataModel):
    selectedFont = _define_plot_style()

    ps = model_data.Power_Supply

    plt.figure(figsize=(5, 5))
    plt.plot([ps.t_off, ps.t_off], [np.min(ps.I_control_LUT), np.max(ps.I_control_LUT)], 'k--', linewidth=4.0,
             label='t_PC')
    plt.plot(ps.t_control_LUT, ps.I_control_LUT, 'ro-', label='LUT')
    plt.xlabel('Time [s]', selectedFont)
    plt.ylabel('Current [A]', selectedFont)
    plt.title('Look-up table controlling power supply', selectedFont)
    plt.grid(True)
    plt.rcParams.update({'font.size': 12})
    displayWaitAndClose(waitTimeBeforeMessage=.1, waitTimeAfterMessage=10)

def plot_all(model_data: DataModel, roxie_data: APIdata):
    '''
        Plot all default plots
    '''
    # # plot_field(model_data)
    # plot_polarities(model_data, roxie_data)
    # plot_strands_groups_layers(model_data)
    # plot_electrical_order(model_data)
    # plot_q_prop_v(model_data)
    # # plot_quench_prop_and_resist(model_data)
    plot_psu_and_trig(model_data)
    # plot_half_turns(model_data, roxie_data)
    # plot_heat_exchange_order(model_data)
    # plot_nonlin_induct(model_data)
    plot_power_supl_contr(model_data)

############## Helper functions
def _define_plot_style():
    '''
    Define default style for plots
    '''
    selectedFont = {'fontname': 'DejaVu Sans', 'size': 14}  # Define style for plots
    return selectedFont

def _get_conductor_centers(roxie_data: APIdata):
    '''
    Find center locations of each half-turn
    '''
    x_insulated, y_insulated, _, _, _, _, _, _, _ = get_conductor_corners(roxie_data)

    nHalfTurns = len(x_insulated)
    x_ave, y_ave = [], []
    for ht in range(nHalfTurns):
        x_ave.append(statistics.mean(x_insulated[ht]))
        y_ave.append(statistics.mean(y_insulated[ht]))

    return x_ave, y_ave

def _get_group_centers(roxie_data: APIdata, strandToGroup):
    '''
    Find center locations of each group of half-turns (i.e. coil blocks)
    '''
    _, _, _, _, _, x_strand, y_strand, _, _ = get_conductor_corners(roxie_data)

    nGroups = int(np.max(strandToGroup))
    # Average group positions
    x_ave_group = []
    y_ave_group = []
    for g in range(1, nGroups+1):
        idx_g = find_indices(strandToGroup, lambda s: s == g)  # indices of the strands belonging to group g
        list_x = [x_strand[i] for i in idx_g]  # list of all x positions of strands belonging to group g
        list_y = [y_strand[i] for i in idx_g]  # list of all y positions of strands belonging to group g

        x_ave_group.append(statistics.mean(list_x))
        y_ave_group.append(statistics.mean(list_y))

    return x_ave_group, y_ave_group



