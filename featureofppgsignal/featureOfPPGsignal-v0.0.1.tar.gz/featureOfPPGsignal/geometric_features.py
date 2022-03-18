from matplotlib import pyplot as plt
from scipy.signal import find_peaks, argrelextrema
import signal_processing
import scipy.signal
import numpy as np


def ratio_4th_peak_1st_der_and_dicroticnotch_peak_timeToPulseInterval(raw_signal):
    """
    Calculates the ratio of 4th peak of 1st derivative time and dicroticnotch peak time to_pulse interval
    ratio_4th_peak_1st_der_and_dicroticnotch_peak_timeToPulseInterval = (t_ϵ1Der+ t_dnp)⁄t_peaks

    :param raw_signal: list
        The raw PPG signal, without filtering
    :return: mean_ratio: float
        Mean value of ratio for each pulse
    :return: ratio: list:
        A list of all ratios for each pulse interval.
    """
    ratio = []

    fourth_peaks = position_of_4th_peak_of_1st_derivative(raw_signal)[0]
    _, dicroticnotch_peaks_time, dicroticnotch_peak_pos = find_dicroticnotch_peak_time(raw_signal)
    pulse_interval = find_pulses_interval(raw_signal)[1]

    for i in range(len(pulse_interval) - 1):  # for each pulse
        for j in range(len(dicroticnotch_peak_pos)):
            if pulse_interval[i] < dicroticnotch_peak_pos[j] < pulse_interval[i + 1] and fourth_peaks[i] != -1:
                ratio.append((fourth_peaks[i] + dicroticnotch_peaks_time[j]) / pulse_interval[i])

    if len(ratio) == 0:
        return 0.0, []

    mean_ratio = np.mean(ratio)
    return mean_ratio, ratio


def ratio_3rd_peak_1st_der_and_diastolic_peak_time_to_pulse_interval(raw_signal):
    """
    Calculates the ratio of 3rd peak of 1st derivative time and diastolic peak time to_pulse interval
    ratio_3rd_peak_1st_der_and_diastolic_peak_time_to_pulse_interval = (t_γ1Der+t_dp )⁄t_peaks

    :param raw_signal: list
        The raw PPG signal, without filtering
    :return: mean_ratio: float
        Mean value of ratio for each pulse
    :return: ratio: list:
        A list of all ratios for each pulse interval.
    """

    ratio = []

    third_peaks = position_of_3rd_peak_of_1st_derivative(raw_signal)[0]
    _, diastolic_peak_time, diastolic_peak_pos = find_diastolic_peak_time(raw_signal)
    pulse_interval = find_pulses_interval(raw_signal)[1]

    for i in range(len(pulse_interval) - 1):  # for each pulse
        for j in range(len(diastolic_peak_pos)):
            if pulse_interval[i] < diastolic_peak_pos[j] < pulse_interval[i + 1] and third_peaks[i] != -1:
                ratio.append((third_peaks[i] + diastolic_peak_time[j]) / pulse_interval[i])

    if len(ratio) == 0:
        return 0.0, []

    mean_ratio = np.mean(ratio)
    return mean_ratio, ratio


def ratio_1st_peak_1st_derivative_1st_peak_2nd_derivative_to_pulse_interval(raw_signal):
    """
    Calculates ratio of 1st peak of 1st derivative and 1st peak of 2nd_derivative to pulse interval
    ratio_1st_peak_1st_derivative_1st_peak_2nd_derivative_to_pulse_interval = (t_α1Der+t_α2Der )⁄t_peaks

    :param raw_signal: list
        The raw PPG signal, without filtering
    :return: mean_ratio: float
        Mean value of ratio for each pulse
    :return: ratio: list:
        A list of all ratios for each pulse interval.
    """
    ratio = []

    first_peaks_first_der = position_of_1st_peak_of_1st_derivative(raw_signal)[0]  # ta1Der
    first_peaks_second_der = position_of_1st_peak_of_2nd_derivative(raw_signal)[0]  # t_a2Der
    pulse_interval = find_pulses_interval(raw_signal)[1]

    for i in range(len(pulse_interval)):  # for each pulse
        if first_peaks_first_der[i] != -1 and first_peaks_second_der[i] != -1:
            ratio.append((first_peaks_first_der[i] + first_peaks_second_der[i]) / pulse_interval[i])

    if len(ratio) == 0:
        return 0.0, []

    mean_ratio = np.mean(ratio)
    return mean_ratio, ratio


def ratio_of_2nd_peak_of_2nd_derivative_to_pulse_interval(raw_signal):
    """
    Calculates the time of 2nd peak of first derivative to pulse interval
    ratio_of_2nd_peak_of_2nd_derivative_to_pulse_interval = t_b2Der⁄t_peaks

    :param raw_signal: list
        The raw PPG signal, without filtering
    :return: mean_ratio: float
        Mean 2nd peak of 2nd derivative time to pulse interval
    :return: ratio: list:
        List containing the time of each 2nd peak of 2nd derivative to pulse interval.
    """
    ratio = []

    second_peak_pos = position_of_2nd_peak_of_2nd_derivative(raw_signal)[0]  # t_b2Der
    pulse_interval = find_pulses_interval(raw_signal)[1]  # t_pulse_interval

    for i in range(len(pulse_interval)):  # for each pulse
        if second_peak_pos[i] != -1:
            ratio.append(second_peak_pos[i] / pulse_interval[i])

    if len(ratio) == 0:
        return 0.0, []

    mean_ratio = np.mean(ratio)
    return mean_ratio, ratio


def ratio_of_1st_peak_of_2nd_derivative_to_pulse_interval(raw_signal):
    """
    Calculates the time of 1st peak of first derivative to pulse interval
    ratio_of_1st_peak_of_2nd_derivative_to_pulse_interval = t_α2Der⁄t_peaks

    :param raw_signal: list
        The raw PPG signal, without filtering
    :return: mean_ratio: float
        Mean 1st peak of 2nd derivative time to pulse interval
    :return: ratio: list:
        List containing the time of each 1st peak of 2nd derivative to pulse interval.
    """
    ratio = []

    first_peak_pos = position_of_1st_peak_of_2nd_derivative(raw_signal)[0]  # t_a2Der
    pulse_interval = find_pulses_interval(raw_signal)[1]  # t_pulse_interval

    for i in range(len(pulse_interval)):  # for each pulse
        if first_peak_pos[i] != -1:
            ratio.append(first_peak_pos[i] / pulse_interval[i])

    if len(ratio) == 0:
        return 0.0, []

    mean_ratio = np.mean(ratio)
    return mean_ratio, ratio


def ratio_of_4th_peak_of_1st_derivative_to_pulse_interval(raw_signal):
    """
   Calculates the time of 4th peak of first derivative to pulse interval
   ratio_of_4th_peak_of_1st_derivative_to_pulse_interval = t_e1Der⁄t_peaks

   :param raw_signal: list
       The raw PPG signal, without filtering
   :return: mean_ratio: float
       Mean 4th peak of 1st derivative time to pulse interval
   :return: ratio: list:
       List containing the time of each 4th peak of 1st derivative to pulse interval.
   """

    ratio = []

    fourth_peak_pos = position_of_4th_peak_of_1st_derivative(raw_signal)[0]  # t_e1Der
    pulse_interval = find_pulses_interval(raw_signal)[1]  # t_pulse_interval

    for i in range(len(pulse_interval)):  # for each pulse
        if fourth_peak_pos[i] != -1:
            ratio.append(fourth_peak_pos[i] / pulse_interval[i])

    if len(ratio) == 0:
        return 0.0, []

    mean_ratio = np.mean(ratio)
    return mean_ratio, ratio


def ratio_of_3rd_peak_of_1st_derivative_to_pulse_interval(raw_signal):
    """
   Calculates the time of 3rd peak of first derivative to pulse interval
   ratio_of_3rd_peak_of_1st_derivative_to_pulse_interval = t_c1Der⁄t_peaks

   :param raw_signal: list
       The raw PPG signal, without filtering
   :return: mean_ratio: float
       Mean 3rd peak of 1st derivative time to pulse interval
   :return: ratio: list:
       List containing the time of each 3rd peak of 1st derivative to pulse interval.
   """
    ratio = []

    third_peak_pos = position_of_3rd_peak_of_1st_derivative(raw_signal)[0]  # t_c1Der
    pulse_interval = find_pulses_interval(raw_signal)[1]  # t_pulse_interval

    for i in range(len(pulse_interval)):  # for each pulse
        if third_peak_pos[i] != -1:
            ratio.append(third_peak_pos[i] / pulse_interval[i])

    if len(ratio) == 0:
        return 0.0, []

    mean_ratio = np.mean(ratio)
    return mean_ratio, ratio


def ratio_of_2nd_peak_of_1st_derivative_to_pulse_interval(raw_signal):
    """
   Calculates the time of 2nd peak of first derivative to pulse interval
   ratio_of_2nd_peak_of_1st_derivative_to_pulse_interval = t_b1Der⁄t_peaks

   :param raw_signal: list
       The raw PPG signal, without filtering
   :return: mean_ratio: float
       Mean 2nd peak of 1st derivative time to pulse interval
   :return: ratio: list:
       List containing the time of each 2nd peak of 1st derivative to pulse interval.
   """
    ratio = []

    second_peak_pos = position_of_2nd_peak_of_1st_derivative(raw_signal)[0]  # t_b1Der
    pulse_interval = find_pulses_interval(raw_signal)[1]  # t_pulse_interval

    for i in range(len(pulse_interval)):  # for each pulse
        if second_peak_pos[i] != -1:
            ratio.append(second_peak_pos[i] / pulse_interval[i])

    if len(ratio) == 0:
        return 0.0, []

    mean_ratio = np.mean(ratio)
    return mean_ratio, ratio


def ratio_of_1st_peak_of_1st_derivative_to_pulse_interval(raw_signal):
    """
    Calculates the time of 1st peak of first derivative to pulse interval
    ratio_of_1st_peak_of_1st_derivative_to_pulse_interval = t_α1Der⁄t_peaks

    :param raw_signal: list
        The raw PPG signal, without filtering
    :return: mean_ratio: float
        Mean 1st peak of 1st derivative time to pulse interval
    :return: ratio: list:
        List containing the time of each 1st peak of 1st derivative to pulse interval.
    """

    ratio = []

    first_peak_pos = position_of_1st_peak_of_1st_derivative(raw_signal)[0]  # t_a1Der
    pulse_interval = find_pulses_interval(raw_signal)[1]  # t_pulse_interval

    for i in range(len(pulse_interval)):  # for each pulse
        if first_peak_pos[i] != -1:
            ratio.append(first_peak_pos[i] / pulse_interval[i])

    if len(ratio) == 0:
        return 0.0, []

    mean_ratio = np.mean(ratio)
    return mean_ratio, ratio


def ratio_height_of_peak_prices_in_the_2nd_derivative(raw_signal):
    """
    Calculate the ratio height of peak prices in the 2nd derivative
    ratio_height_of_peak_prices_in_the_2nd_derivative = (β2Der+γ2Der)⁄a2Der

    :param raw_signal: list
        The raw PPG signal, without filtering
    :return: mean_ratio: float
        Mean value of ratio for each pulse
    :return: ratio: list:
        A list of all ratios for each pulse interval.
    """
    ratio = []
    order = 5
    fc = 2.5

    filtered_signal = np.array(signal_processing.lowPassButterworthFilter(raw_signal, order, fc))
    first_derivative = np.gradient(filtered_signal, 1)
    second_derivative = np.gradient(first_derivative, 1)

    first_peak_pos = position_of_1st_peak_of_2nd_derivative(raw_signal)[0]
    second_peak_pos = position_of_2nd_peak_of_2nd_derivative(raw_signal)[0]
    third_peak_pos = position_of_3rd_peak_of_2nd_derivative(raw_signal)[0]

    for i in range(len(first_peak_pos)):
        if first_peak_pos[i] != -1 and second_peak_pos[i] != -1 and third_peak_pos[i] != -1:
            ratio.append((second_derivative[second_peak_pos[i]] + second_derivative[third_peak_pos[i]]) /
                         second_derivative[first_peak_pos[i]])

    if len(ratio) == 0:
        return 0.0, []

    mean_ratio = np.mean(ratio)

    return mean_ratio, ratio


def ratio_of_4th_and_1st_peaks_of_2nd_derivative(raw_signal):
    """
    Calculate the ratio of 4th and 1st peaks of 2nd derivative
    ratio_of_4th_and_1st_peaks_of_2nd_derivative = ϵ2Der⁄a2Der

    :param raw_signal: list
        The raw PPG signal, without filtering
    :return: mean_ratio: float
        Mean value of ratio for each pulse
    :return: ratio: list:
        A list of all ratios for each pulse interval.
    """
    ratio = []
    order = 5
    fc = 2.5

    filtered_signal = np.array(signal_processing.lowPassButterworthFilter(raw_signal, order, fc))
    first_derivative = np.gradient(filtered_signal, 1)
    second_derivative = np.gradient(first_derivative, 1)

    first_peak_pos = position_of_1st_peak_of_2nd_derivative(raw_signal)[0]
    fourth_peak_pos = position_of_4th_peak_of_2nd_derivative(raw_signal)[0]

    for i in range(len(first_peak_pos)):
        if first_peak_pos[i] != -1 and fourth_peak_pos[i] != -1:
            ratio.append(abs(second_derivative[fourth_peak_pos[i]]) / abs(second_derivative[first_peak_pos[i]]))

    if len(ratio) == 0:
        return 0.0, []

    mean_ratio = np.mean(ratio)

    return mean_ratio, ratio


def ratio_of_2nd_and_1st_peaks_of_2nd_derivative(raw_signal):
    """
    Calculate the ratio of 2nd and 1st peaks of 2nd derivative
    ratio_of_2nd_and_1st_peaks_of_2nd_derivative = β_2Der⁄a_2Der

    :param raw_signal: list
        The raw PPG signal, without filtering
    :return: mean_ratio: float
        Mean value of ratio for each pulse
    :return: ratio: list:
        A list of all ratios for each pulse interval.
    """
    ratio = []
    order = 5
    fc = 2.5

    filtered_signal = np.array(signal_processing.lowPassButterworthFilter(raw_signal, order, fc))
    first_derivative = np.gradient(filtered_signal, 1)
    second_derivative = np.gradient(first_derivative, 1)

    first_peak_pos = position_of_1st_peak_of_2nd_derivative(raw_signal)[0]
    second_peak_pos = position_of_2nd_peak_of_2nd_derivative(raw_signal)[0]

    for i in range(len(first_peak_pos)):
        if first_peak_pos[i] != -1 and second_peak_pos[i] != -1:
            ratio.append(second_derivative[second_peak_pos[i]] / second_derivative[first_peak_pos[i]])

    if len(ratio) == 0:
        return 0.0, []

    mean_ratio = np.mean(ratio)

    return mean_ratio, ratio


def position_of_4th_peak_of_2nd_derivative(raw_signal):
    """
    Calculate the position of the 4th peak of the 2nd derivative t_e2Der

    :param raw_signal: list
        The raw PPG signal, without filtering
    :return: fourth_peak_pos: list
        A list of positions of all the 4th peak of the 1st derivative for each pulse interval
    :return: fourth_peak_value: list
        A list of values of all the 4th peak of the 1st derivative for each pulse interval
    :return: mean_dist: float
        Mean value of the distance of each peak from the beginning of the pulse
    :return: dist: list:
        A list of all distances of each peak from the beginning of the pulse
    """
    fourth_peak_pos = []
    dist = []
    order = 5
    fc = 2.5

    filtered_signal = np.array(signal_processing.lowPassButterworthFilter(raw_signal, order, fc))
    first_derivative = np.gradient(filtered_signal, 1)
    second_derivative = np.gradient(first_derivative, 1)

    third_peak_pos = position_of_3rd_peak_of_1st_derivative(raw_signal)[0]

    _, t_pulse_interval, t_pulse_pos = find_pulses_interval(raw_signal)

    for i in range(1, len(t_pulse_pos)):
        local_minimum = argrelextrema(np.array(second_derivative[t_pulse_pos[i - 1]:t_pulse_pos[i]]), np.less)[0]

        if len(local_minimum) > 1:
            dist.append(local_minimum[1])
            fourth_peak_pos.append(t_pulse_pos[i - 1] + local_minimum[1])
        else:
            fourth_peak_pos.append(-1)  # there isn't peak

    sign = np.array(second_derivative)
    pos = [i for i in fourth_peak_pos if i != -1]

    if len(pos) == 0:
        return fourth_peak_pos, [], 0.0, []

    fourth_peak_value = sign[pos]

    mean_dist = np.mean(dist)  # mean of distance

    return fourth_peak_pos, fourth_peak_value, mean_dist, dist


def position_of_3rd_peak_of_2nd_derivative(raw_signal):
    """
    Calculate the position of the 3rd peak of the 2nd derivative t_c2Der

    :param raw_signal: list
        The raw PPG signal, without filtering
    :return: third_peak_pos: list
        A list of positions of all the 3rd peak of the 2nd derivative for each pulse interval
    :return: third_peak_value: list
        A list of values of all the 3rd peak of the 2nd derivative for each pulse interval
    :return: mean_dist: float
        Mean value of the distance of each peak from the beginning of the pulse
    :return: dist: list:
        A list of all distances of each peak from the beginning of the pulse
    """
    third_peak_pos = []
    dist = []
    order = 5
    fc = 2.5

    filtered_signal = np.array(signal_processing.lowPassButterworthFilter(raw_signal, order, fc))
    first_derivative = np.gradient(filtered_signal, 1)
    second_derivative = np.gradient(first_derivative, 1)

    second_peak_pos = position_of_2nd_peak_of_2nd_derivative(raw_signal)[0]

    _, t_pulse_interval, t_pulse_pos = find_pulses_interval(raw_signal)

    for i in range(1, len(t_pulse_pos)):
        peaks, _ = find_peaks(np.array(second_derivative[t_pulse_pos[i - 1]:t_pulse_pos[i]]))

        if len(peaks) > 1:
            dist.append(peaks[1])
            third_peak_pos.append(t_pulse_pos[i - 1] + peaks[1])
        else:
            third_peak_pos.append(-1)  # there isn't peak

    sign = np.array(second_derivative)
    pos = [i for i in third_peak_pos if i != -1]

    if len(pos) == 0:
        return third_peak_pos, [], 0.0, []

    third_peak_value = sign[pos]

    mean_dist = np.mean(dist)  # mean of distance

    return third_peak_pos, third_peak_value, mean_dist, dist


def position_of_2nd_peak_of_2nd_derivative(raw_signal):
    """
    Calculate the position of the 2nd peak of the 2nd derivative t_b2Der

    :param raw_signal: list
        The raw PPG signal, without filtering
    :return: second_peak_pos: list
        A list of positions of all the 2nd peak of the 2nd derivative for each pulse interval
    :return: second_peak_value: list
        A list of values of all the 2nd peak of the 2nd derivative for each pulse interval
    :return: mean_dist: float
        Mean value of the distance of each peak from the beginning of the pulse
    :return: dist: list:
        A list of all distances of each peak from the beginning of the pulse
    """
    second_peak_pos = []
    dist = []
    order = 5
    fc = 2.5

    filtered_signal = np.array(signal_processing.lowPassButterworthFilter(raw_signal, order, fc))
    first_derivative = np.gradient(filtered_signal, 1)
    second_derivative = np.gradient(first_derivative, 1)

    first_peak_pos = position_of_1st_peak_of_2nd_derivative(raw_signal)[0]

    _, t_pulse_interval, t_pulse_pos = find_pulses_interval(raw_signal)

    for i in range(1, len(t_pulse_pos)):
        local_minimum = argrelextrema(np.array(second_derivative[t_pulse_pos[i - 1]:t_pulse_pos[i]]), np.less)[0]

        if len(local_minimum) > 0:
            dist.append(local_minimum[0])
            second_peak_pos.append(t_pulse_pos[i - 1] + local_minimum[0])
        else:
            second_peak_pos.append(-1)  # there isn't peak

    sign = np.array(second_derivative)
    pos = [i for i in second_peak_pos if i != -1]

    if len(pos) == 0:
        return second_peak_pos, [], 0.0, []

    second_peak_value = sign[pos]

    mean_dist = np.mean(dist)  # mean of distance

    return second_peak_pos, second_peak_value, mean_dist, dist


def position_of_1st_peak_of_2nd_derivative(raw_signal):
    """
    Calculate the position of the 1st peak of the 2nd derivative t_α2Der

    :param raw_signal: list
        The raw PPG signal, without filtering
    :return: first_peak_pos: list
        A list of positions of all the 1st peak of the 2nd derivative for each pulse interval
    :return: first_peak_value: list
        A list of values of all the 1st peak of the 2nd derivative for each pulse interval
    :return: mean_dist: float
        Mean value of the distance of each peak from the beginning of the pulse
    :return: dist: list:
        A list of all distances of each peak from the beginning of the pulse
    """
    first_peak_pos = []
    dist = []
    order = 5
    fc = 2.5

    filtered_signal = np.array(signal_processing.lowPassButterworthFilter(raw_signal, order, fc))
    first_derivative = np.gradient(filtered_signal, 1)
    second_derivative = np.gradient(first_derivative, 1)

    _, t_pulse_interval, t_pulse_pos = find_pulses_interval(raw_signal)

    for i in range(1, len(t_pulse_pos)):
        peaks, _ = find_peaks(np.array(second_derivative[t_pulse_pos[i - 1]:t_pulse_pos[i]]))

        if len(peaks) > 0:
            dist.append(peaks[0])
            first_peak_pos.append(t_pulse_pos[i - 1] + peaks[0])
        else:
            first_peak_pos.append(-1)

    sign = np.array(second_derivative)
    pos = [i for i in first_peak_pos if i != -1]

    if len(pos) == 0:
        return first_peak_pos, [], 0.0, []

    first_peak_value = sign[pos]

    mean_dist = np.mean(dist)  # mean of distance

    return first_peak_pos, first_peak_value, mean_dist, dist


def position_of_4th_peak_of_1st_derivative(raw_signal):
    """
    Calculate the position of the 4th peak of the 1st derivative t_e1Der

    :param raw_signal: list
        The raw PPG signal, without filtering
    :return: fourth_peak_pos: list
        A list of positions of all the 4th peak of the 1st derivative for each pulse interval
    :return: fourth_peak_value: list
        A list of values of all the 4th peak of the 1st derivative for each pulse interval
    :return: mean_dist: float
        Mean value of the distance of each peak from the beginning of the pulse
    :return: dist: list:
        A list of all distances of each peak from the beginning of the pulse
    """
    fourth_peak_pos = []
    dist = []  # distance from the beginning of the pulse
    order = 5
    fc = 2.5

    filtered_signal = np.array(signal_processing.lowPassButterworthFilter(raw_signal, order, fc))
    derivative = np.gradient(filtered_signal, 1)

    # third_peak_pos = position_of_3rd_peak_of_1st_derivative(raw_signal)[0]

    _, t_pulse_interval, t_pulse_pos = find_pulses_interval(raw_signal)

    for i in range(1, len(t_pulse_pos)):
        local_minimum = argrelextrema(np.array(derivative[t_pulse_pos[i - 1]:t_pulse_pos[i]]), np.less)[0]

        if len(local_minimum) > 1:
            dist.append(local_minimum[1])
            fourth_peak_pos.append(t_pulse_pos[i - 1] + local_minimum[1])
        else:
            fourth_peak_pos.append(-1)  # there isn't peak

    sign = np.array(derivative)
    pos = [i for i in fourth_peak_pos if i != -1]

    if len(pos) == 0:
        return fourth_peak_pos, [], 0.0, []

    fourth_peak_value = sign[pos]

    mean_dist = np.mean(dist)  # mean of distance

    return fourth_peak_pos, fourth_peak_value, mean_dist, dist


def position_of_3rd_peak_of_1st_derivative(raw_signal):
    """
    Calculate the position of the 3rd peak of the 1st derivative t_c1Der

    :param raw_signal: list
        The raw PPG signal, without filtering
    :return: third_peak_pos: list
        A list of positions of all the 3rd peak of the 1st derivative for each pulse interval
    :return: third_peak_value: list
        A list of values of all the 3rd peak of the 1st derivative for each pulse interval
    :return: mean_dist: float
        Mean value of the distance of each peak from the beginning of the pulse
    :return: dist: list:
        A list of all distances of each peak from the beginning of the pulse
    """
    third_peak_pos = []
    dist = []
    order = 5
    fc = 2.5

    filtered_signal = np.array(signal_processing.lowPassButterworthFilter(raw_signal, order, fc))
    derivative = np.gradient(filtered_signal, 1)

    second_peak_pos = position_of_2nd_peak_of_1st_derivative(raw_signal)[0]
    _, t_pulse_interval, t_pulse_pos = find_pulses_interval(raw_signal)

    for i in range(1, len(t_pulse_pos)):
        peaks, _ = find_peaks(np.array(derivative[t_pulse_pos[i - 1]:t_pulse_pos[i]]))

        if len(peaks) > 1:
            dist.append(peaks[1])
            third_peak_pos.append(t_pulse_pos[i - 1] + peaks[1])
        else:
            third_peak_pos.append(-1)  # there isn't peak

    sign = np.array(derivative)
    pos = [i for i in third_peak_pos if i != -1]

    if len(pos) == 0:
        return third_peak_pos, [], 0.0, []

    third_peak_value = sign[pos]

    mean_dist = np.mean(dist)  # mean of distance

    return third_peak_pos, third_peak_value, mean_dist, dist


def position_of_2nd_peak_of_1st_derivative(raw_signal):
    """
    Calculate the position of the 2nd peak of the 1st derivative t_b1Der

    :param raw_signal: list
        The raw PPG signal, without filtering
    :return: second_peak_pos: list
        A list of positions of all the 2nd peak of the 1st derivative for each pulse interval
    :return: second_peak_value: list
        A list of values of all the 2nd peak of the 1st derivative for each pulse interval
    :return: mean_dist: float
        Mean value of the distance of each peak from the beginning of the pulse
    :return: dist: list:
        A list of all distances of each peak from the beginning of the pulse
    """
    second_peak_pos = []
    dist = []  # distance from the beginning of the pulse
    order = 5
    fc = 2.5

    filtered_signal = np.array(signal_processing.lowPassButterworthFilter(raw_signal, order, fc))
    derivative = np.gradient(filtered_signal, 1)

    first_peak_pos = position_of_1st_peak_of_1st_derivative(raw_signal)[0]

    _, t_pulse_interval, t_pulse_pos = find_pulses_interval(raw_signal)

    for i in range(1, len(t_pulse_pos)):
        local_minimum = argrelextrema(np.array(derivative[t_pulse_pos[i - 1]:t_pulse_pos[i]]), np.less)[0]

        if len(local_minimum) > 0:
            dist.append(local_minimum[0])
            second_peak_pos.append(t_pulse_pos[i - 1] + local_minimum[0])
        else:
            second_peak_pos.append(-1)  # there isn't peak

    sign = np.array(derivative)
    pos = [i for i in second_peak_pos if i != -1]

    if len(pos) == 0:
        return second_peak_pos, [], 0.0, []

    second_peak_value = sign[pos]

    mean_dist = np.mean(dist)  # mean of distance

    return second_peak_pos, second_peak_value, mean_dist, dist


def position_of_1st_peak_of_1st_derivative(raw_signal):
    """
    Calculate the position of the 1st peak of the 1st derivative t_α1Der

    :param raw_signal: list
        The raw PPG signal, without filtering
    :return: first_peak_pos: list
        A list of positions of all the 1st peak of the 1st derivative for each pulse interval
    :return: first_peak_value: list
        A list of values of all the 1st peak of the 1st derivative for each pulse interval
    :return: mean_dist: float
        Mean value of the distance of each peak from the beginning of the pulse
    :return: dist: list:
        A list of all distances of each peak from the beginning of the pulse
    """

    first_peak_pos = []
    dist = []  # distance from the beginning of the pulse
    order = 5
    fc = 2.5

    filtered_signal = np.array(signal_processing.lowPassButterworthFilter(raw_signal, order, fc))
    derivative = np.gradient(filtered_signal, 1)

    _, t_pulse_interval, t_pulse_pos = find_pulses_interval(raw_signal)

    for i in range(1, len(t_pulse_pos)):
        peaks, _ = find_peaks(np.array(derivative[t_pulse_pos[i - 1]:t_pulse_pos[i]]))

        if len(peaks) > 0:
            dist.append(peaks[0])
            first_peak_pos.append(t_pulse_pos[i - 1] + peaks[0])
        else:
            first_peak_pos.append(-1)

    sign = np.array(derivative)
    pos = [i for i in first_peak_pos if i != -1]

    if len(pos) == 0:
        return first_peak_pos, [], 0.0, []

    first_peak_value = sign[pos]

    mean_dist = np.mean(dist)  # mean of distance

    return first_peak_pos, first_peak_value, mean_dist, dist


def find_peaktopeak_time_to_pulse_interval(raw_signal):
    """
        Calculates the time between systolic and diastolic peaks to pulse interval
        peaktopeak_time_to_pulse_interval = peaktopeaks_t⁄t_peaks

        :param raw_signal: list
            The raw PPG signal, without filtering
        :return: mean_ratio: float
            Mean systolic peak time to pulse interval
        :return: ratio: list:
            List containing the time of each systolic peak to pulse interval.
    """
    ratio = []

    _, t_peak_to_peak, peak_to_peak_pos = find_peak_to_peak_interval(raw_signal)
    _, t_pulse_interval, t_pulse_pos = find_pulses_interval(raw_signal)

    for i in range(1, len(t_pulse_pos)):
        for j in range(len(peak_to_peak_pos)):
            if t_pulse_pos[i - 1] < peak_to_peak_pos[j] < t_pulse_pos[i]:
                ratio.append(t_peak_to_peak[j] / t_pulse_interval[i - 1])

    if len(ratio) == 0:
        return 0.0, []

    return np.mean(ratio), ratio


def find_dicroticnotch_peak_time_to_pulse_interval(raw_signal):
    """
        Calculates the dicroticnotch peak time to pulse interval
        dicroticnotch_peak_time_to_pulse_interval = t_dn⁄t_peaks

        :param raw_signal: list
            The raw PPG signal, without filtering
        :return: mean_ratio: float
            Mean dicroticnotch peak time to pulse interval
        :return: ratio: list:
            List containing the time of each dicroticnotch peak to pulse interval.
        """
    ratio = []

    _, t_dicroticnotch, dicroticnotch_time_pos = find_dicroticnotch_peak_time(raw_signal)
    _, t_pulse_interval, t_pulse_pos = find_pulses_interval(raw_signal)

    for i in range(1, len(t_pulse_pos)):
        for j in range(len(dicroticnotch_time_pos)):
            if t_pulse_pos[i - 1] < dicroticnotch_time_pos[j] < t_pulse_pos[i]:
                ratio.append(t_dicroticnotch[j] / t_pulse_interval[i - 1])

    if len(ratio) == 0:
        return 0.0, []

    return np.mean(ratio), ratio


def find_diastolic_peak_time_to_pulse_interval(raw_signal):
    """
        Calculates the diastolic peak time to pulse interval
        diastolic_peak_time_to_pulse_interval = t_d⁄t_peaks

        :param raw_signal: list
            The raw PPG signal, without filtering
        :return: mean_ratio: float
            Mean diastolic peak time to pulse interval
        :return: ratio: list:
            List containing the time of each diastolic peak to pulse interval.
        """
    ratio = []

    _, t_diastolic, diastolic_time_pos = find_diastolic_peak_time(raw_signal)
    _, t_pulse_interval, t_pulse_pos = find_pulses_interval(raw_signal)

    for i in range(1, len(t_pulse_pos)):
        for j in range(len(diastolic_time_pos)):
            if t_pulse_pos[i - 1] < diastolic_time_pos[j] < t_pulse_pos[i]:
                ratio.append(t_diastolic[j] / t_pulse_interval[i - 1])

    if len(ratio) == 0:
        return 0.0, []

    return np.mean(ratio), ratio


def find_systolic_peak_time_to_pulse_interval(raw_signal):
    """
    Calculates the systolic peak time to pulse interval
    systolic_peak_time_to_pulse_interval = t_sp⁄t_peaks

    :param raw_signal: list
        The raw PPG signal, without filtering
    :return: mean_ratio: float
        Mean systolic peak time to pulse interval
    :return: ratio: list:
        List containing the time of each systolic peak to pulse interval.
    """
    ratio = []
    _, t_systolic, systolic_time_pos = find_systolic_peak_time(raw_signal)
    _, t_pulse_interval, t_pulse_pos = find_pulses_interval(raw_signal)

    for i in range(1, len(t_pulse_pos)):
        for j in range(len(systolic_time_pos)):
            if t_pulse_pos[i - 1] < systolic_time_pos[j] < t_pulse_pos[i]:
                ratio.append(t_systolic[j] / t_pulse_interval[i-1])

    if len(ratio) == 0:
        return 0.0, []

    mean_ratio = np.mean(ratio)

    return mean_ratio, ratio


def find_diastolic_peak_slope(raw_signal):
    """
        Calculate diastolic peak slope of PPG signal.
        diastolic_peak_slope = diastolic_p⁄(t_peaks-t_dnp)

        :param: list: raw_signal:
            The raw PPG signal, without filtering
        :return:
            float: slope
                Average slopes of the diastolic peaks of PPG signal
            list: slope_array
                The list contains the slope of each diastolic peak of the PPG signal.
        """
    slope_array = []

    diastolic_peaks_pos, diastolic_peak_value = find_diastolic_peaks(raw_signal)
    _, t_dicroticnotch, dicroticnotch_time_pos = find_dicroticnotch_peak_time(raw_signal)
    _, t_pulse_interval, t_pulse_pos = find_pulses_interval(raw_signal)

    if len(dicroticnotch_time_pos) == 0 or len(t_pulse_interval) == 0:
        return 0.0, []

    for i in range(1, len(t_pulse_pos)):
        for j in range(len(dicroticnotch_time_pos)):
            if t_pulse_pos[i - 1] < dicroticnotch_time_pos[j] < t_pulse_pos[i] and \
                    t_pulse_interval[i-1] - t_dicroticnotch[j] != 0:
                for k in range(len(diastolic_peaks_pos)):
                    if t_pulse_pos[i - 1] < diastolic_peaks_pos[k] < t_pulse_pos[i]:
                        slope_array.append(diastolic_peak_value[k] / abs(t_pulse_interval[i-1] - t_dicroticnotch[j]))

    if len(slope_array) == 0:
        return 0.0, []

    slope = np.mean(slope_array)

    return slope, slope_array


def find_systolic_peak_slope(raw_signal):
    """
    Calculate systolic peak slope of PPG signal.
    systolic_peak_slope = t_sp⁄systolic_p

    :param: list: raw_signal:
        The raw PPG signal, without filtering
    :return:
        float: slope
            Average slopes of the systolic peaks of PPG signal
        list: slope_array
            The list contains the slope of each systolic peak of the PPG signal.
    """

    slope_array = []

    systolic_peaks_pos, systolic_peak_value = find_systolic_peaks(raw_signal)
    _, t_systolic, systolic_time_pos = find_systolic_peak_time(raw_signal)

    if systolic_peaks_pos.size == 0:
        return 0.0, []

    for i in range(len(systolic_peaks_pos)):
        for j in range(len(systolic_time_pos)):
            if systolic_peaks_pos[i] == systolic_time_pos[j] and systolic_peak_value[i] != 0:
                slope_array.append(t_systolic[j] / systolic_peak_value[i])

    if len(slope_array) == 0:
        return 0.0, []

    slope = np.mean(slope_array)

    return slope, slope_array


def find_ratio_of_two_area(raw_signal):
    """
    Calculate find ratio of two area of PPG signal.
    that is, it calculates the ratio of area from start of pulse interval to dicroticnotch peaks
    and area from dicroticnotch peaks to end of pulse interval

    :param: list: raw_signal:
        The raw PPG signal, without filtering
    :return:
        float: np.mean(ratio)
            Average of all areas
        list: ratio
            A list of areas of PPG signal
    """

    dicroticnotch_peaks = find_dicroticnotch_peaks(raw_signal)[0]
    t_pulse_interval = find_pulses_interval(raw_signal)[2]

    ratio = []

    # find the ratio of diastolic to systolic peaks that belong in the same period
    for i in range(1, len(t_pulse_interval)):
        alpha1 = 0
        alpha2 = 0
        for dn in dicroticnotch_peaks:
            if t_pulse_interval[i - 1] < dn < t_pulse_interval[i]:
                for j in range(t_pulse_interval[i - 1], dn):
                    alpha1 += raw_signal[j]

                for k in range(dn, t_pulse_interval[i]):
                    alpha2 += raw_signal[k]

                ratio.append(alpha2/alpha1)

    if len(ratio) == 0:
        return 0.0, []

    return np.mean(ratio), ratio


def find_range_of_half_systolic_peak(raw_signal):
    """
    Calculate range of half systolic peak of PPG signal

    :param: list: raw_signal:
        The raw PPG signal, without filtering
    :return:
        float: np.mean(half_widths)
            Average of all half systolic peak intervals of PPG signal
        list: half_widths
            A list of half systolic peak intervals of PPG signal
    """
    order = 5
    fc = 2.5  # Cut-off frequency of the filter

    systolic_peaks = find_systolic_peaks(raw_signal)[0]

    filtered_signal = signal_processing.lowPassButterworthFilter(raw_signal, order, fc)
    half_widths = scipy.signal.peak_widths(filtered_signal, systolic_peaks, rel_height=0.5)[0]

    return np.mean(half_widths), half_widths


def find_peak_to_peak_interval(raw_signal):
    """
    Calculate peak to peak interval of PPG signal
    Peak to peak interval is the time between systolic and diastolic peaks

    :param: list: raw_signal:
        The raw PPG signal, without filtering
    :return:
        float: np.mean(peak_to_peak_interval)
            Average of all peak to peak intervals of PPG signal
        list: peak_to_peak_interval
            A list of peak to peak intervals of PPG signal
        list: peak_to_peak_interval_pos
            A list of peaks positions of PPG signal (systolic and diastolic)
    """
    count = 0
    # from systolic to diastolic interval
    diastolic_peaks = find_diastolic_peaks(raw_signal)[0]
    systolic_peaks = find_systolic_peaks(raw_signal)[0]
    peak_to_peak_interval = []
    peak_to_peak_interval_pos = []

    size = len(systolic_peaks) + len(diastolic_peaks)
    sort_array = np.zeros((2, size))
    i = 0
    j = 0
    k = 0

    # 0 -> systolic peaks
    # 1 -> diastolic peaks
    while i < len(systolic_peaks) and j < len(diastolic_peaks):

        if systolic_peaks[i] < diastolic_peaks[j]:
            sort_array[0][k] = 0
            sort_array[1][k] = systolic_peaks[i]
            k = k + 1
            i = i + 1
        else:
            sort_array[0][k] = 1
            sort_array[1][k] = diastolic_peaks[j]
            k = k + 1
            j = j + 1

    while i < len(systolic_peaks):
        sort_array[0][k] = 0
        sort_array[1][k] = systolic_peaks[i]
        k = k + 1
        i = i + 1

    while j < len(diastolic_peaks):
        sort_array[0][k] = 1
        sort_array[1][k] = diastolic_peaks[j]
        k = k + 1
        j = j + 1

    for index in range(len(sort_array[0]) - 1):
        if sort_array[0][index] - sort_array[0][index + 1] == -1:
            peak_to_peak_interval.append(sort_array[1][index + 1] - sort_array[1][index])
            peak_to_peak_interval_pos.append(systolic_peaks[count])
            count += 1

    if not peak_to_peak_interval:
        return 0.0, [], []

    return np.mean(peak_to_peak_interval), peak_to_peak_interval, peak_to_peak_interval_pos


def find_dicroticnotch_peak_time(raw_signal):
    """
    Calculate the dicroticnotch peak time of PPG signal
    Time dicroticnotch peak is the time from start of pulse interval to dicroticnotch peak

    :param: list: raw_signal:
        The raw PPG signal, without filtering
    :return:
        float: np.mean(diastolic_peak_time)
            Average of all diastolic peak times of PPG signal
        list: dicroticnotch_peak_time
            A list of dicroticnotch peak times of PPG signal
        list: dicroticnotch_peak_pos
            A list of dicroticnotch peak positions of PPG signal
    """
    order = 5
    fc = 2.5
    count = 0

    dicroticnotch_peak_time = []
    dicroticnotch_peak_pos = []

    dicroticnotch_peaks = find_dicroticnotch_peaks(raw_signal)[0]

    filtered_signal = signal_processing.lowPassButterworthFilter(raw_signal, order, fc)
    local_minimum = argrelextrema(filtered_signal, np.less)[0]

    size = len(dicroticnotch_peaks) + len(local_minimum)
    sort_array = np.zeros((2, size))
    i = 0
    j = 0
    k = 0

    # join and sort the local minimum and dicroticnotch arrays
    # and find the difference between local minimum and the next dicroticnotch
    # 0 -> local_minimum
    # 1 -> systolic peaks
    while i < len(local_minimum) and j < len(dicroticnotch_peaks):

        if local_minimum[i] < dicroticnotch_peaks[j]:
            sort_array[0][k] = 0
            sort_array[1][k] = local_minimum[i]
            k = k + 1
            i = i + 1
        else:
            sort_array[0][k] = 1
            sort_array[1][k] = dicroticnotch_peaks[j]
            k = k + 1
            j = j + 1

    while i < len(local_minimum):
        sort_array[0][k] = 0
        sort_array[1][k] = local_minimum[i]
        k = k + 1
        i = i + 1

    while j < len(dicroticnotch_peaks):
        sort_array[0][k] = 1
        sort_array[1][k] = dicroticnotch_peaks[j]
        k = k + 1
        j = j + 1

    for index in range(len(sort_array[0]) - 1):
        if sort_array[0][index] - sort_array[0][index + 1] == -1:
            dicroticnotch_peak_time.append(sort_array[1][index + 1] - sort_array[1][index])
            dicroticnotch_peak_pos.append(dicroticnotch_peaks[count])
            count += 1

    if not dicroticnotch_peak_time:
        return 0.0, [], []

    return np.mean(dicroticnotch_peak_time), dicroticnotch_peak_time, dicroticnotch_peak_pos


def find_diastolic_peak_time(raw_signal):
    """
    Calculate the diastolic peak time of PPG signal
    Time diastolic peak is the time from start of pulse interval to diastolic peak

    :param: list: raw_signal:
        The raw PPG signal, without filtering
    :return:
        float: np.mean(diastolic_peak_time)
            Average of all diastolic peak times of PPG signal
        list: diastolic_peak_time
            A list of diastolic peak times of PPG signal
        list: diastolic_peak_pos
            A list of diastolic peak positions of PPG signal
    """

    order = 5
    fc = 2.5
    count = 0
    diastolic_peak_time = []
    diastolic_peak_pos = []

    diastolic_peaks = find_diastolic_peaks(raw_signal)[0]

    filtered_signal = signal_processing.lowPassButterworthFilter(raw_signal, order, fc)
    local_minimum = argrelextrema(filtered_signal, np.less)[0]

    size = len(diastolic_peaks) + len(local_minimum)
    sort_array = np.zeros((2, size))
    i = 0
    j = 0
    k = 0

    # join and sort the local minimum and diastolic peaks arrays
    # and find the difference between local minimum and the next diastolic peak
    # 0 -> local_minimum
    # 1 -> systolic peaks
    while i < len(local_minimum) and j < len(diastolic_peaks):

        if local_minimum[i] < diastolic_peaks[j]:
            sort_array[0][k] = 0
            sort_array[1][k] = local_minimum[i]
            k = k + 1
            i = i + 1
        else:
            sort_array[0][k] = 1
            sort_array[1][k] = diastolic_peaks[j]
            k = k + 1
            j = j + 1

    while i < len(local_minimum):
        sort_array[0][k] = 0
        sort_array[1][k] = local_minimum[i]
        k = k + 1
        i = i + 1

    while j < len(diastolic_peaks):
        sort_array[0][k] = 1
        sort_array[1][k] = diastolic_peaks[j]
        k = k + 1
        j = j + 1

    for index in range(len(sort_array[0]) - 1):
        if sort_array[0][index] - sort_array[0][index + 1] == -1:
            diastolic_peak_time.append(sort_array[1][index + 1] - sort_array[1][index])
            diastolic_peak_pos.append(diastolic_peaks[count])
            count += 1

    if len(diastolic_peak_time) == 0:
        return 0.0, [], []

    return np.mean(diastolic_peak_time), diastolic_peak_time, diastolic_peak_pos


def find_systolic_peak_time(raw_signal):
    """
    Calculate the systolic peak time of PPG signal
    Time systolic peak is the time from start of pulse interval to systolic peak

    :param: list: raw_signal:
        The raw PPG signal, without filtering
    :return:
        float: np.mean(systolic_peak_time)
            Average of all systolic peak times of PPG signal
        list: systolic_peak_time
            A list of systolic peak times of PPG signal
        list: systolic_peak_pos
            A list of systolic peak positions of PPG signal
    """

    order = 5
    fc = 2.5
    count = 0
    systolic_peak_time = []
    systolic_peak_pos = []

    systolic_peaks = find_systolic_peaks(raw_signal)[0]

    filtered_signal = signal_processing.lowPassButterworthFilter(raw_signal, order, fc)
    local_minimum = argrelextrema(filtered_signal, np.less)[0]

    size = len(systolic_peaks) + len(local_minimum)
    sort_array = np.zeros((2, size))
    i = 0
    j = 0
    k = 0

    # join and sort the local minimum and systolic peaks arrays
    # and find the difference between local minimum and the next systolic peak
    # 0 -> local_minimum
    # 1 -> systolic peaks
    while i < len(local_minimum) and j < len(systolic_peaks):

        if local_minimum[i] < systolic_peaks[j]:
            sort_array[0][k] = 0
            sort_array[1][k] = local_minimum[i]
            k = k + 1
            i = i + 1
        else:
            sort_array[0][k] = 1
            sort_array[1][k] = systolic_peaks[j]
            k = k + 1
            j = j + 1

    while i < len(local_minimum):
        sort_array[0][k] = 0
        sort_array[1][k] = local_minimum[i]
        k = k + 1
        i = i + 1

    while j < len(systolic_peaks):
        sort_array[0][k] = 1
        sort_array[1][k] = systolic_peaks[j]
        k = k + 1
        j = j + 1

    for index in range(len(sort_array[0]) - 1):
        if sort_array[0][index] - sort_array[0][index + 1] == -1:
            systolic_peak_time.append(sort_array[1][index + 1] - sort_array[1][index])
            systolic_peak_pos.append(systolic_peaks[count])
            count += 1

    if not systolic_peak_time:
        return 0.0, [], []

    return np.mean(systolic_peak_time), systolic_peak_time, systolic_peak_pos


def find_pulses_interval(raw_signal):
    """
    Calculate the pulse interval of PPG signal

    :param: list: raw_signal:
        The raw PPG signal, without filtering
    :return:
        float: np.mean(tpeaks)
            Average of all pulse intervals of PPG signal
        list: tpeaks
            A list of pulse intervals of PPG signal
        list: pulse_pos
            A list of position of start and end of each pulse interval
    """
    order = 5
    fc = 2.5

    filtered_signal = signal_processing.lowPassButterworthFilter(raw_signal, order, fc)
    # find local minimum of signal
    local_minimum = argrelextrema(filtered_signal, np.less)[0]
    pulse_pos = np.append(local_minimum, len(raw_signal) - 1)

    tpeaks = []
    # find the difference between two local minimum
    for i in range(len(pulse_pos) - 1):
        tpeaks.append(pulse_pos[i + 1] - pulse_pos[i])

    return np.mean(tpeaks), tpeaks, pulse_pos


def ratio_of_diastolic_sub_dicroticnotch_to_systolic_peaks(raw_signal):
    """
    ratio_of_diastolic_sub_dicroticnotch_to_systolic_peaks = (diastolic_p - dicroticnotch_p) / systolic_p
    and calculated for each period of PPG signal

    :param: list: raw_signal:
        The raw PPG signal, without filtering
    :return:
        float: np.mean(augmentation_index)
            Average of all augmentations indexes in PPG signal

        list: augmentation_index
            An array of augmentations indexes for each period of PPG signal
    """

    systolic_peaks = find_systolic_peaks(raw_signal)[0]
    diastolic_peaks = find_diastolic_peaks(raw_signal)[0]
    dicroticnotch = find_dicroticnotch_peaks(raw_signal)[0]
    t_pulse_interval = find_pulses_interval(raw_signal)[2]

    augmentation_index = []

    # find the ratio of diastolic to systolic peaks that belong in the same period
    for i in range(1, len(t_pulse_interval)):
        for s in systolic_peaks:
            if t_pulse_interval[i - 1] < s < t_pulse_interval[i] and raw_signal[s] != 0:
                for dn in dicroticnotch:
                    if t_pulse_interval[i - 1] < dn < t_pulse_interval[i] and dn > s:
                        for d in diastolic_peaks:
                            if t_pulse_interval[i - 1] < d < t_pulse_interval[i] and d > dn:
                                augmentation_index.append((raw_signal[d] - raw_signal[dn]) / raw_signal[s])

    # if no systolic or dicroticnotch peak is detected in this period return 0.0
    if len(augmentation_index) == 0:
        return 0.0, []

    return np.mean(augmentation_index), augmentation_index


def ratio_of_dicroticnotch_to_systolic_peaks(raw_signal):
    """
    ratio_of_dicroticnotch_to_systolic_peaks = dicroticnotch_p/systolic_p
    and calculated for each period of PPG signal

    :param: list: raw_signal:
        The raw PPG signal, without filtering
    :return:
        float: np.mean(augmentation_index)
            Average of all augmentations indexes in PPG signal

        list: augmentation_index
            An array of augmentations indexes for each period of PPG signal
    """
    dicroticnotch = find_dicroticnotch_peaks(raw_signal)[0]
    systolic_peaks = find_systolic_peaks(raw_signal)[0]
    t_pulse_interval = find_pulses_interval(raw_signal)[2]

    augmentation_index = []

    # find the ratio of diastolic to systolic peaks that belong in the same period
    for i in range(1, len(t_pulse_interval)):
        for s in systolic_peaks:
            if t_pulse_interval[i - 1] < s < t_pulse_interval[i] and raw_signal[s] != 0:
                for dn in dicroticnotch:
                    if t_pulse_interval[i - 1] < dn < t_pulse_interval[i] and dn > s:
                        augmentation_index.append(raw_signal[dn] / raw_signal[s])

    # if no systolic or dicroticnotch peak is detected in this period return 0.0
    if len(augmentation_index) == 0:
        return 0.0, []

    return np.mean(augmentation_index), augmentation_index


def find_relative_augmentation_index(raw_signal):
    """
    relative augmentation index = (systolic_p - diastolic_p) / systolic_p
    and calculated for each period of PPG signal

    :param: list: raw_signal:
        The raw PPG signal, without filtering
    :return:
        float: np.mean(augmentation_index)
            Average of all augmentations indexes in PPG signal

        list: augmentation_index
            An array of augmentations indexes for each period of PPG signal
    """

    diastolic_peaks = find_diastolic_peaks(raw_signal)[0]
    systolic_peaks = find_systolic_peaks(raw_signal)[0]
    t_pulse_interval = find_pulses_interval(raw_signal)[2]

    augmentation_index = []

    # find the ratio of diastolic to systolic peaks that belong in the same period
    for i in range(1, len(t_pulse_interval)):
        for s in systolic_peaks:
            if t_pulse_interval[i - 1] < s < t_pulse_interval[i] and raw_signal[s] != 0:
                for d in diastolic_peaks:
                    if t_pulse_interval[i - 1] < d < t_pulse_interval[i] and d > s:
                        augmentation_index.append(abs(raw_signal[s] - raw_signal[d]) / raw_signal[s])

    # if no systolic or diastolic peak is detected in this period return 0.0
    if len(augmentation_index) == 0:
        return 0.0, []

    return np.mean(augmentation_index), augmentation_index


def find_augmentation_index(raw_signal):
    """
    augmentation_index =  diastolic_p/ systolic_p
    and calculated for each period of PPG signal
    :param: list: raw_signal:
        The raw PPG signal, without filtering
    :return:
        float: np.mean(augmentation_index)
            Average of all augmentations indexes in PPG signal

        float: augmentation_index
            An array of augmentations indexes for each period of PPG signal
    """
    diastolic_peaks = find_diastolic_peaks(raw_signal)[0]
    systolic_peaks = find_systolic_peaks(raw_signal)[0]
    t_pulse_interval = find_pulses_interval(raw_signal)[2]

    augmentation_index = []

    # find the ratio of diastolic to systolic peaks that belong in the same period
    for i in range(1, len(t_pulse_interval)):
        for s in systolic_peaks:
            if t_pulse_interval[i - 1] < s < t_pulse_interval[i] and raw_signal[s] != 0:
                for d in diastolic_peaks:
                    if t_pulse_interval[i - 1] < d < t_pulse_interval[i] and d > s:
                        augmentation_index.append(raw_signal[d] / raw_signal[s])

    # if no systolic or diastolic peak is detected in this period return 0.0
    if len(augmentation_index) == 0:
        return 0.0, []

    return np.mean(augmentation_index), augmentation_index


def find_dicroticnotch_peaks(raw_signal):
    """
    Calculate the dicroticnotch peaks in PPG signal,
    Dicroticnotch are the local minimum between systolic and diastolic peaks

    :param: list: raw_signal:
        The raw PPG signal, without filtering
    :return:
        list: dicroticnotch_peak
            Position of dicroticnotch peaks in PPG signal
        list: value_of_dicroticnotch
            Value of dicroticnotch peaks in PPG signal
    """
    dicroticnotch_peak = []
    r = np.array(raw_signal)

    pos_of_systolic_peaks = find_systolic_peaks(raw_signal)[0]
    pos_of_diastolic_peaks = find_diastolic_peaks(raw_signal)[0]

    # find the local minimum of signal
    local_minimum = argrelextrema(r, np.less)[0]

    size = len(pos_of_systolic_peaks) + len(pos_of_diastolic_peaks)
    sort_array = np.zeros((2, size))
    i = 0
    j = 0
    k = 0

    # find the minimum between systolic and diastolic peaks
    # 0 -> systolic peaks
    # 1 -> diastolic peaks
    while i < len(pos_of_systolic_peaks) and j < len(pos_of_diastolic_peaks):

        if pos_of_systolic_peaks[i] < pos_of_diastolic_peaks[j]:
            sort_array[0][k] = 0
            sort_array[1][k] = pos_of_systolic_peaks[i]
            k = k + 1
            i = i + 1
        else:
            sort_array[0][k] = 1
            sort_array[1][k] = pos_of_diastolic_peaks[j]
            k = k + 1
            j = j + 1

    while i < len(pos_of_systolic_peaks):
        sort_array[0][k] = 0
        sort_array[1][k] = pos_of_systolic_peaks[i]
        k = k + 1
        i = i + 1

    while j < len(pos_of_diastolic_peaks):
        sort_array[0][k] = 1
        sort_array[1][k] = pos_of_diastolic_peaks[j]
        k = k + 1
        j = j + 1

    for i in range(len(local_minimum)):
        for index in range(len(sort_array[0]) - 1):
            if sort_array[0][index] - sort_array[0][index + 1] == -1 and (
                    sort_array[1][index] <= local_minimum[i] <= sort_array[1][index + 1]):
                dicroticnotch_peak.append(local_minimum[i])

    value_of_dicroticnotch = r[dicroticnotch_peak]

    # return position ( time ) anf value of dicroticnotch
    return dicroticnotch_peak, value_of_dicroticnotch


def find_diastolic_peaks(raw_signal):
    """
    Calculate the diastolic peaks in PPG signal
    Diastolic peaks are the peaks of the first derivative that are close to zero

    :param: list: raw_signal:
        The raw PPG signal, without filtering
    :return:
        list: pos_of_peaks
            Position of diastolic peaks in PPG signal
        list: value_of_peaks
            Value of diastolic peaks in PPG signal
    """
    order = 5
    fc = 2.5
    r = np.array(raw_signal)

    filtered_signal = signal_processing.lowPassButterworthFilter(raw_signal, order, fc)

    # first derivation of signal
    derivative = np.gradient(filtered_signal, 1)

    mov_avg = signal_processing.moving_average(derivative).to_numpy().flatten()
    all_peaks, _ = find_peaks(derivative)

    # find peaks above the moving average function in the first derivation of signal
    upper_peaks, _ = find_peaks(derivative, height=mov_avg)
    # diastolic peaks are the peaks below the moving average
    pos_of_peaks = np.setdiff1d(all_peaks, upper_peaks)

    value_of_peaks = r[pos_of_peaks]

    # return position ( time ) anf value of diastolic peaks
    return pos_of_peaks, value_of_peaks


def find_systolic_peaks(raw_signal):
    """
    Calculate the systolic peaks in PPG signal.
    Systolic peaks are the peaks of the filtered signal above moving average

    :param raw_signal: list
        The raw PPG signal, without filtering
    :return:
        list: pos_of_peaks
            Position of systolic peaks in PPG signal
        list: value_of_peaks
            Value of systolic peaks in PPG signal
    """

    order = 5
    fc = 2.5  # Cut-off frequency of the filter

    r = np.array(raw_signal)

    smooth_signal = signal_processing.lowPassButterworthFilter(r, order, fc)
    moving_average_signal = signal_processing.moving_average(smooth_signal).to_numpy().flatten()

    # find that exist above the moving average function in the filtered signal
    pos_of_peaks, _ = find_peaks(smooth_signal, height=moving_average_signal)
    # calculate the value of peaks
    value_of_peaks = r[pos_of_peaks]

    # return position ( time ) anf value of systolic peaks
    return pos_of_peaks, value_of_peaks
