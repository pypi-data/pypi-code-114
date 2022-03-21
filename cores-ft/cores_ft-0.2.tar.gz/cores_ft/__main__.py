import os
from .loop import loop_event


def main():
    try:
        loop_event()
    except KeyboardInterrupt:
        os.system('clear')
        print('Stop the monitoring.')


main()
