import psutil
import os
import time
import sys
from colorama import Fore, Style

def poll_mem_util():
    total_blocks = os.get_terminal_size().columns
    bar_blocks = total_blocks - 9   #" 100.0%" is 7 chars long, [] is 2 chars long

    mem_stats = psutil.virtual_memory()
    mem_total = mem_stats.total
    mem_used = mem_stats.used

    mem_percent = mem_used / mem_total
    color = percent_to_color(mem_percent)
    used_blocks = int(mem_percent * bar_blocks)

    output_string = f"[{color}{'=' * used_blocks}{Style.RESET_ALL}{' ' * (bar_blocks - used_blocks)}]"
    output_string += f"{mem_percent:.1%}\r".rjust(7)

    sys.stdout.write(output_string)

def percent_to_color(percent):
    if percent > 0.8:
        return Fore.RED
    elif percent > 0.6:
        return Fore.YELLOW
    else:
        return Fore.GREEN

def show_mem_util():
    try:
        while True:
            poll_mem_util()
            time.sleep(1)
    except KeyboardInterrupt:
        print()
        quit()

if __name__ == "__main__":
    show_mem_util()