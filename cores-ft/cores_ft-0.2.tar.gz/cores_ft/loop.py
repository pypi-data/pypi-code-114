from itertools import cycle
from time import sleep

from .get_info import read_cpuinfo, get_lm_sensors_info
from .screen import clear_screen
from .output_msg import mount_msg_output


def loop_event():
    clear_screen()
    symb = cycle(('|', '/', '-', '\\'))

    while True:
        print(f'Monitoring CPUs: {next(symb)}\n')

        freq = read_cpuinfo()

        temp = get_lm_sensors_info()

        msg = mount_msg_output(freq, temp)

        print(msg)

        print('\nType ctr+z or ctr+c to stop !')

        sleep(1.0)
        clear_screen()
