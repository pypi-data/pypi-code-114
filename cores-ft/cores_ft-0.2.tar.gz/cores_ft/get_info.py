import os


def read_cpuinfo():
    # read freq from /proc/cpuinfo

    with open('/proc/cpuinfo') as f:
        lines = f.readlines()

    i, freq = 0, {}
    for lin in lines:
        cols = lin.split(':')
        if cols[0].startswith('cpu MHz'):
            freq[f'core_{i}'] = float(cols[1])/1000
            i += 1

    return freq


def get_lm_sensors_info():
    # get temp using sensors
    os.system('sensors > tmp')
    with open('tmp') as f:
        lines = f.readlines()

    i, temp = 0, {}
    for lin in lines:
        cols = lin.split(':')
        if cols[0].startswith('Core'):
            temp[f'core_{i}'] = cols[1].split()[0]
            i += 1
    os.system('rm tmp')

    return temp
