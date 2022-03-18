from scipy import signal
import pandas as pd
import datetime
import csv


def moving_average(raw_signal):
    """
    find moving average using pandas library

    :param raw_signal: list
        A list of data (signal)
    :return: result :list
        The moving average signal
    """
    fs = len(raw_signal) / 10
    window_size = int(fs * 0.75)

    result = pd.DataFrame(raw_signal).rolling(window=window_size, min_periods=1).mean()

    return result


def lowPassButterworthFilter(data, order, fc):
    """
    Butterworth Filter using scipy.signal library

    :param data: list
        A list of records
    :param order: int
        The order of the filter.
    :param fc: float
        The cut-off frequency of filter
    :return: smooth_data: list
        A list with filtered data
    """
    fs = len(data) / 10
    nyq = 0.5 * fs
    normal_cutoff = fc / nyq  # Normalize the frequency

    b, a = signal.butter(order, normal_cutoff)
    smooth_data = signal.filtfilt(b, a, data)

    return smooth_data


# create Windows size 10 sec
def createWindows(dataset):
    """
    Create 10-second windows

    :param: list dataset:
        A list of records
    :return: list window:
        A list containing recordings of 10 consecutive seconds
    """
    windows = []

    # convert str to datatime (time)
    start_date_time = datetime.datetime.strptime(dataset[0][1], '%Y-%m-%d %H:%M:%S')
    window = dataset[0][2]  # append the fist row to the "window" array

    i = 1
    count = 1
    while i < len(dataset):
        # convert str to datatime (time) for the next record
        current_date_time = datetime.datetime.strptime(dataset[i][1], '%Y-%m-%d %H:%M:%S')
        # find the difference between the next and preview record
        sub = current_date_time - start_date_time

        if count == 10:  # create time Windows 10 sec
            windows.append(window)
            window = dataset[i][2]
            count = 1
        else:
            # if sub.seconds == 1 or sub.seconds == 0:  # if the different equals to 1 or 0 sec then append the record
            if sub.seconds == 1:  # if the different equals to 1sec then append the record
                window += dataset[i][2]
                count += 1
            else:
                window = dataset[i][2]
                count = 1

        start_date_time = current_date_time
        i += 1

    return windows


def datasets(rows, column):
    """
    Divides the data into 6 data sets according to the number of zeros present in each record.

    :param: list: rows:
        Α 2D list that contains the rows and columns of the data file
    :param: int: column:
        The column number we are interested in (the column that contains the PPG signal array)
    :return: list: datasetMoreThan10
        Return a datasets that contains up to 10 zero values
    :return: list: datasetMoreThan15
        Return a datasets that contains up to 15 zero values
    :return: list: datasetMoreThan20
        Return a datasets that contains up to 20 zero values
    :return: list: datasetMoreThan25
        Return a datasets that contains up to 25 zero values
    :return: list: datasetMoreThan30
        Return a datasets that contains up to 30 zero values
    """

    datasetMoreThan10 = []
    datasetMoreThan15 = []
    datasetMoreThan20 = []
    datasetMoreThan25 = []
    datasetMoreThan30 = []
    datasetMoreThan35 = []

    for row in rows:
        data = row[column]

        zeroCounter = 0
        for i in data:  # calculate number of zero for each record
            if i == 0:
                zeroCounter += 1

        # create dataset according to the number of zeros
        if zeroCounter <= 10:
            datasetMoreThan10.append(row)
        if zeroCounter <= 15:
            datasetMoreThan15.append(row)
        if zeroCounter <= 20:
            datasetMoreThan20.append(row)
        if zeroCounter <= 25:
            datasetMoreThan25.append(row)
        if zeroCounter <= 30:
            datasetMoreThan30.append(row)
        if zeroCounter <= 35:
            datasetMoreThan35.append(row)

    return datasetMoreThan10, datasetMoreThan15, datasetMoreThan20, datasetMoreThan25, datasetMoreThan30, datasetMoreThan35


def gender_segregation(entries):
    """
    Divides the data set into males and females
    :param entries: list
        A list of data
    :return: female: list
        Contain the records of the data set concerning females
    :return: male: list
        Contain the records of the data set concerning males
    """
    females = []
    males = []

    for en in entries:
        if en[10] == "Female":
            females.append(en)
        elif en[10] == "Male":
            males.append(en)

    return females, males


def readCSVdata(filename):
    """
    Read CSV files and convert to an array of data

    :param: string: filename:
        The path of file
    :return: list:  file_rows
        A list with rows and columns of file
    """
    # read csv file and return an array containing its rows
    column = 2

    with open(filename, 'r') as csvfile:
        has_header = csv.Sniffer().has_header(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.reader(csvfile)
        if has_header:
            next(reader)  # ignore header

        reader = csv.reader(csvfile)
        file_rows = []

        for row in reader:
            row[column] = list(map(int, row[column][1:-1].split(',')))  # convert ppg array from str to list
            file_rows.append(row)  # append row to array

    return file_rows


def createFileForEachPatient(filename):
    """
    Creates files that each contain the records for each patient

    :param filename: string
        The path of file
    """
    data = pd.read_csv(filename)

    id = 0
    # create a new file for each patient
    # for (patient), group in data.groupby(['patient_id']):
    for group in data.groupby(['patient_id']):
        id += 1
        group.to_csv(f'Patient_{id}.csv', index=False)


def readFileForEachPatient(filename):
    """
    Create a 2D list each row contains the corresponding patient's records

    :param filename: string
        The path of file
    :return: patients_array : list
        A list with records of each patient
    """
    patients_array = []
    createFileForEachPatient(filename)

    for i in range(1, 76):
        patients_array.append(readCSVdata("Patient_" + str(i) + ".csv"))

    return patients_array
