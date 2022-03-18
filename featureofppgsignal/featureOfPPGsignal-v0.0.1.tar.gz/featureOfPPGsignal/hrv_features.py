import geometric_features
import collections
import numpy as np
import math


def calculatePNN50(peak_list, fs):
    """
    Calculates the proportion of NN50 divided by total number of NNs

    :param peak_list: list
        A list of peak to peak interval (from systolic to systolic peak)
    :param fs: float
        The sampling rate
    :return: pnn20: float
        The value of pnn50
    """
    peak_to_peak_diff = []
    peak_to_peak_list = []

    for i in range(len(peak_list) - 1):
        peak_to_peak_interval = (peak_list[i + 1] - peak_list[i])
        ms_dist = ((peak_to_peak_interval / fs) * 1000.0)
        peak_to_peak_list.append(ms_dist)

    for i in range(len(peak_to_peak_list) - 1):
        peak_to_peak_diff.append(abs(peak_to_peak_list[i] - peak_to_peak_list[i + 1]))

    NN50 = [x for x in peak_to_peak_diff if (x > 50)]

    pnn50 = float(len(NN50)) / float(len(peak_to_peak_diff))

    return pnn50


def calculatePNN20(peak_list, fs):
    """
    Calculates the proportion of NN20 divided by total number of NNs

    :param peak_list: list
        A list of peak to peak interval (from systolic to systolic peak)
    :param fs: float
        The sampling rate
    :return: pnn20: float
        The value of pnn20
    """
    peak_to_peak_diff = []
    peak_to_peak_list = []

    for i in range(len(peak_list) - 1):
        peak_to_peak_interval = (peak_list[i + 1] - peak_list[i])
        ms_dist = ((peak_to_peak_interval / fs) * 1000.0)
        peak_to_peak_list.append(ms_dist)

    for i in range(len(peak_to_peak_list) - 1):
        peak_to_peak_diff.append(abs(peak_to_peak_list[i] - peak_to_peak_list[i + 1]))

    NN20 = [x for x in peak_to_peak_diff if (x > 20)]

    pnn20 = float(len(NN20)) / float(len(peak_to_peak_diff))

    return pnn20


def calculateRMSSD(peak_list, fs):
    """
    Calculates the square root of the mean of the squares of the successive differences between adjacent NNs

    :param peak_list: list
        A list of peak to peak interval (from systolic to systolic peak)
    :param fs: float
        The sampling rate
    :return: rmssd: float
        The value of RMSSD
    """
    peak_to_peak_sqdiff = []
    peak_to_peak_list = []

    for i in range(len(peak_list) - 1):
        peak_to_peak_interval = (peak_list[i + 1] - peak_list[i])

        ms_dist = ((peak_to_peak_interval / fs) * 1000.0)
        peak_to_peak_list.append(ms_dist)

    for i in range(len(peak_to_peak_list) - 1):
        peak_to_peak_sqdiff.append(np.square(peak_to_peak_list[i] - peak_to_peak_list[i + 1]))

    rmssd = np.sqrt(np.mean(peak_to_peak_sqdiff))

    return rmssd


def segmentation(peak_list, duration=300):
    """
    Divide the peaks list into intervals according to duration

    :param peak_list: list
        A list of peak to peak interval (from systolic to systolic peak)
    :param duration: int
        Maximum duration per segment in [s] (default: 300 seconds -> 5 minutes)
    :return: segments : 2D list
        A list containing the peaks list divided into intervals according to duration
    """
    peaks_in_duration = []
    segments = []
    crt = 1

    for i in range(len(peak_list)):
        if peak_list[i] < (duration * crt):
            peaks_in_duration.append(peak_list[i])
        else:
            segments.append(peaks_in_duration)
            peaks_in_duration = [peak_list[i]]
            crt += 1

    segments.append(peaks_in_duration)
    return segments


def calculateSDNNi(peak_list, fs, duration=300):
    """
    Calculates the average of the standard deviation of the intervals t1 every 5 minutes

    :param peak_list: list
        A list of peak to peak interval (from systolic to systolic peak)
    :param fs: float
        The sampling rate
    :param duration: int
        Maximum duration per segment in [s] (default: 300 seconds -> 5 minutes)
    :return: sdnni: float
        The value of the average of the standard deviation of the intervals t1 every 5 minutes
    """
    sdnn_values = []
    segments = segmentation(peak_list, duration)

    for k in range(len(segments)):
        sdnn_values.append(calculateSDNN(segments[k], fs))
    # sdnn_values = [calculateSDNN(x, fs) for x in segments]

    sdnn_index = np.mean(sdnn_values)

    return sdnn_index


def calculateSDANN(peak_list, fs, duration=300):
    """
    Calculates Standard Deviation of the Averages of NN

    :param peak_list: list
        A list of peak to peak interval (from systolic to systolic peak)
    :param fs: float
        The sampling rate
    :param duration: int
        Maximum duration per segment in [s] (default: 300 seconds -> 5 minutes)
    :return: sdann: float
        The value of standard deviation of the averages of NN
    """
    peak_to_peak_for_segments = []
    sdann = []

    segments = segmentation(peak_list, duration)
    for k in range(len(segments)):
        peak_to_peak_list = []

        for i in range(len((segments[k])) - 1):
            peak_to_peak_interval = (segments[k][i + 1] - segments[k][i])
            ms_dist = ((peak_to_peak_interval / fs) * 1000.0)
            peak_to_peak_list.append(ms_dist)

        peak_to_peak_for_segments.append(peak_to_peak_list)

    mean_values = [np.mean(x) for x in peak_to_peak_for_segments]
    # print(mean_values)

    for i in range(len(mean_values)):
        sdann.append(np.square(mean_values[i] - np.mean(mean_values)))

    sdann = np.sqrt(np.mean(sdann))

    return sdann


def calculateSDSD(raw_signal):
    """
    Calculates Standard Deviation of the Differences

    :param raw_signal: list
        The raw PPG signal, without filtering
    :return: sdnn: float
        The value of standard deviation of the differences
    """
    peak_to_peak_list = []
    peak_to_peak_diff = []
    sdsd = []

    fs = len(raw_signal) / 10
    systolic_peak = geometric_features.find_systolic_peaks(raw_signal)[0]

    for i in range(len(systolic_peak) - 1):
        peak_to_peak_interval = abs(systolic_peak[i + 1] - systolic_peak[i])
        ms_dist = ((peak_to_peak_interval / fs) * 1000.0)
        peak_to_peak_list.append(ms_dist)

    for i in range(len(peak_to_peak_list) - 1):
        peak_to_peak_diff.append(abs(peak_to_peak_list[i] - peak_to_peak_list[i + 1]))

    for i in range(len(peak_to_peak_diff)):
        sdsd.append(np.square(peak_to_peak_diff[i] - np.mean(peak_to_peak_diff)))

    sdsd = np.sqrt(np.mean(sdsd))

    return sdsd


def calculateSDNN(peak_list, fs):
    """
    Calculates Standard Deviation of Normal to Normal

    :param peak_list: list
        A list of peak to peak interval (from systolic to systolic peak)
    :param fs: float
        The sampling rate
    :return: sdnn: float
        The value of standard deviation of normal to normal
    """
    peak_to_peak_list = []
    sdnn = []

    for i in range(len(peak_list) - 1):
        peak_to_peak_interval = (peak_list[i + 1] - peak_list[i])
        ms_dist = ((peak_to_peak_interval / fs) * 1000.0)
        peak_to_peak_list.append(ms_dist)

    for i in range(len(peak_to_peak_list)):
        sdnn.append(np.square(peak_to_peak_list[i] - np.mean(peak_to_peak_list)))

    sdnn = np.sqrt(np.mean(sdnn))

    return sdnn


def calculateIBI(raw_signal):
    """
    Calculates Inter Beat Interval

    :param raw_signal: list
        The raw PPG signal, without filtering
    :return: mean_ratio: float
        Inter Beat Interval
    """
    peak_to_peak_list = []

    fs = len(raw_signal) / 10
    systolic_peak = geometric_features.find_systolic_peaks(raw_signal)[0]

    for i in range(len(systolic_peak) - 1):
        peak_to_peak_interval = (systolic_peak[i + 1] - systolic_peak[i])
        ms_dist = ((peak_to_peak_interval / fs) * 1000.0)
        peak_to_peak_list.append(ms_dist)

    ibi = np.mean(peak_to_peak_list)

    return ibi


def calculateBPM(raw_signal):
    """
    Calculates Beats per Minutes

    :param raw_signal: list
        The raw PPG signal, without filtering
    :return: bpm: float
        Mean bpm
    """
    peak_to_peak_list = []

    fs = len(raw_signal) / 10
    systolic_peak = geometric_features.find_systolic_peaks(raw_signal)[0]

    for i in range(len(systolic_peak) - 1):
        peak_to_peak_interval = (systolic_peak[i + 1] - systolic_peak[i])
        ms_dist = ((peak_to_peak_interval / fs) * 1000.0)
        peak_to_peak_list.append(ms_dist)

    bpm = 60000 / np.mean(peak_to_peak_list)

    return bpm


def renyi_entropy(raw_signal, order=2):
    peak_to_peak_list = []
    fs = len(raw_signal) / 10
    systolic_peak = geometric_features.find_systolic_peaks(raw_signal)[0]

    for i in range(len(systolic_peak) - 1):
        peak_to_peak_interval = abs(systolic_peak[i + 1] - systolic_peak[i])
        ms_dist = ((peak_to_peak_interval / fs) * 1000.0)
        peak_to_peak_list.append(ms_dist)

    length = len(peak_to_peak_list)
    item_counter = collections.Counter([x for x in peak_to_peak_list])

    renyi_entropy_value = 0
    for item in item_counter:
        n_i = item_counter[item]
        p_i = n_i / float(length)
        entropy_i = pow(p_i, order)
        renyi_entropy_value += entropy_i

    renyi_ent = math.log(renyi_entropy_value) / (1 - order)

    return renyi_ent


def shannon_entropy(raw_signal):
    peak_to_peak_list = []
    fs = len(raw_signal) / 10
    systolic_peak = geometric_features.find_systolic_peaks(raw_signal)[0]

    for i in range(len(systolic_peak) - 1):
        peak_to_peak_interval = abs(systolic_peak[i + 1] - systolic_peak[i])
        ms_dist = ((peak_to_peak_interval / fs) * 1000.0)
        peak_to_peak_list.append(ms_dist)

    length = len(peak_to_peak_list)
    item_counter = collections.Counter([x for x in peak_to_peak_list])

    shannon_entropy_value = 0
    for item in item_counter:
        # number of residues
        n_i = item_counter[item]
        p_i = n_i / float(length)
        entropy_i = p_i * (math.log(p_i, 2))
        shannon_entropy_value += entropy_i

    shannon_ent = shannon_entropy_value * -1

    return shannon_ent
