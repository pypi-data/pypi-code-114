from collections import Counter
import geometric_features
import numpy as np


def calculate_skewness(raw_signal):
    """
    Calculate the skewness of each pulse interval

    :param: list: raw_signal:
        The raw PPG signal, without filtering
    :return: res: list:
        A list containing skewness for each pulse intervals of PPG signal (Positive, Negative or Symmetrical)
    :return: count_pos : int
        The number of positive skewness pulse interval
    :return: count_neg : int
        The number of negative skewness pulse interval
    :return: count_sym : int
        The number of symmetrical skewness pulse interval
    """
    means = find_mean(raw_signal)[1]
    std = find_standard_derivation(raw_signal)[1]
    median = find_median(raw_signal)[1]

    count_pos = 0
    count_neg = 0
    count_sym = 0

    res = []
    for i in range(len(means)):
        if std[i] != 0:
            skewn = ((3*(means[i] - median[i])) / std[i])

            if skewn > 0:
                res.append("Positive")
                count_pos += 1
            elif skewn < 0:
                res.append("Negative")
                count_neg += 1
            else:
                res.append("Symmetrical")
                count_sym += 1

    return res, count_pos, count_neg, count_sym


def calculate_range(raw_signal):
    """
    Calculate the range of each pulse interval and its average.

    :param: list: raw_signal:
        The raw PPG signal, without filtering
    :return: np.mean(rng) : float
        Average of all ranges of each pulse intervals of PPG signal
    :return: rng: list:
        A list containing the range for each pulse intervals of PPG signal
    """
    rng = []

    pulse_pos = geometric_features.find_pulses_interval(raw_signal)[2]

    for i in range(1, len(pulse_pos)):
        rng.append(
            np.amax(raw_signal[pulse_pos[i - 1]:pulse_pos[i]]) - np.amin(raw_signal[pulse_pos[i - 1]:pulse_pos[i]]))

    return np.mean(rng), rng


def find_standard_derivation(raw_signal):
    """
    Calculate the standard derivation of each pulse interval and its average.

    :param: list: raw_signal:
        The raw PPG signal, without filtering
    :return: np.mean(std) : float
        Average of all standard derivations of each pulse intervals of PPG signal
    :return: mode: list:
        A list containing the standard derivation for each pulse intervals of PPG signal
    """
    std = []

    pulse_pos = geometric_features.find_pulses_interval(raw_signal)[2]

    for i in range(1, len(pulse_pos)):
        distance = []

        s = raw_signal[pulse_pos[i - 1]:pulse_pos[i]]

        for j in range(len(s)):
            distance.append(np.square(s[j] - np.mean(s)))
        std.append(np.sqrt(np.mean(distance)))

    return np.mean(std), std


def find_mode(raw_signal):
    """
    Calculate the mode of each pulse interval and its average.
    Calculates the most frequently used value of ppg signal

    :param: list: raw_signal:
        The raw PPG signal, without filtering
    :return: np.mean(mode) : float
        Average of all mode of each pulse intervals of PPG signal
    :return: mode: list:
        A list containing the mode for each pulse intervals of PPG signal
    """
    mode = []

    pulse_pos = geometric_features.find_pulses_interval(raw_signal)[2]

    for i in range(1, len(pulse_pos)):
        n_num = raw_signal[pulse_pos[i - 1]:pulse_pos[i]]
        data = Counter(n_num)
        get_mode = dict(data)

        flag = 0
        for k, v in get_mode.items():
            if v == max(data.values()) and flag == 0:
                mode.append(k)
                flag = 1

    return np.mean(mode), mode


def find_median(raw_signal):
    """
    calculate the median of each pulse interval and its average

    :param: list: raw_signal:
        The raw PPG signal, without filtering
    :return: np.mean(median) : float
        Average of all medians each pulse intervals of PPG signal
    :return: median: list:
        A list containing the medians for each pulse intervals of PPG signal
    """
    median = []

    pulse_pos = geometric_features.find_pulses_interval(raw_signal)[2]

    for i in range(1, len(pulse_pos)):
        n_num = raw_signal[pulse_pos[i - 1]:pulse_pos[i]]
        n = len(n_num)
        n_num.sort()

        if n % 2 == 0:
            median1 = n_num[n // 2]
            median2 = n_num[n // 2 - 1]
            median.append((median1 + median2) / 2)
        else:
            median.append(n_num[n // 2])

    return np.mean(median), median


def find_mean(raw_signal):
    """
    calculate the average of values of all pulse interval and its average

    :param: list: raw_signal:
        The raw PPG signal, without filtering
    :return: np.mean(mean) : float
        Average of all pulse intervals of PPG signal
    :return: mean: list:
        A list containing the averages of the values of all the pulse intervals
    """

    mean = []
    t_pulse_interval = geometric_features.find_pulses_interval(raw_signal)[2]

    for i in range(1, len(t_pulse_interval)):
        n = len(raw_signal[t_pulse_interval[i - 1]:t_pulse_interval[i]])
        get_sum = sum(raw_signal[t_pulse_interval[i - 1]:t_pulse_interval[i]])
        mean.append(get_sum / n)

    return np.mean(mean), mean
