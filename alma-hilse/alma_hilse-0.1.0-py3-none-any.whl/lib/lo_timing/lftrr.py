import struct
import sys
import math
try:
    from CCL.AmbManager import AmbManager
    import ControlExceptions
except ModuleNotFoundError:
    print("Failed to import CCL.AmbManager or ControlExceptions")

# # Following PYTHONPATH runtime modification is temporary. This should be done with proper package installation (TODO).
# sys.path.insert(1, "/users/jortiz/dev/hilse/venv/lib/python3.6/site-packages")

from rich.table import Table
from rich.console import Console
from rich.text import Text
# import typer

## Definitions
# LFTRR/LORR CAN bus definitions
CAN_CHANNEL = 1
CAN_NODE = 0x22

# Monitor point definitions
RCA_STATUS = 0x00001
RCA_RX_OPT_PWR = 0x00007
RCA_TE_LENGTH = 0x00011
RCA_TE_OFFSET_COUNTER = 0x00012

# Status monitor point bit definitions
# Byte 1
FLAG_DCM_LOCKED = 0b1
FLAG_12V_OUT_OF_RANGE = 0b10
FLAG_15V_OUT_OF_RANGE = 0b100
FLAG_RX_OPT_PWR_ERROR = 0b1000
FLAG_2GHZ_UNLOCKED = 0b10000 # clear with CLEAR_FLAGS
FLAG_125MHZ_UNLOCKED = 0b100000 # clear with CLEAR_FLAGS
# Byte 2
FLAG_TE_SHORT = 0b1 # clear with CLEAR_FLAGS
FLAG_TE_LONG = 0b10 # clear with CLEAR_FLAGS

# Control points definitions
RCA_RESYNC_TE = 0x00081
RCA_CLEAR_FLAGS = 0x00082

# # Command-line application commands and subcommands based in Typer
# app = typer.Typer(add_completion=True)

# @app.callback()
# def callback():
#     """
#     Obtain basic status of HILSE LFTRR device and issue resync command.

#     Referring to the status, a stripped down version of the LORR status is presented,
#     focusing only on variables relevant to HILSE.

#     Usage:

#     \b
#     hil_lftrr.py        # Display LFTRR status
#     hil_lftrr.py status # Display LFTRR status
#     hil_lftrr.py resync # Resync TE to central reference
#     hil_lftrr.py clear  # Clear TE and PLL error flags

#     """


# @app.command(short_help='LFTRR healthcheck')
def status():
    '''General healthcheck of the LFTRR, limited to relevant variables for HILSE'''

    try:
        mgr = AmbManager('DMC')
    except:
        print()
        print("Failed to instantiate DMC AmbManager")
        print()
        return

    table = Table(title='HILSE LFTRR STATUS')
    table.add_column('Parameter', justify='right')
    table.add_column('Value', justify='right')

    # Received optical power
    try:
        monitor = mgr.monitor(CAN_CHANNEL, CAN_NODE, RCA_RX_OPT_PWR)
    except ControlExceptions.CAMBErrorEx:
        raise Exception(f"Node {hex(CAN_NODE)} not found on CAN bus")

    power_raw = struct.unpack(">H", monitor[0])
    power_mw = power_raw[0] * 20/4095
    power_dbm = 10 * math.log10(power_mw)

    good_power = True
    if power_dbm < -15:
        good_power = False
    if power_dbm > +5:
        good_power = False

    table.add_row(
        "Rx optical power",
        f"[green]{power_dbm:.2f}[/green] \[dBm]" if good_power else f"[red]{power_dbm:.2f}[/red] \[dBm]"
    )

    # TE length
    monitor = mgr.monitor(CAN_CHANNEL, CAN_NODE, RCA_TE_LENGTH)
    te_length = struct.unpack('>I', b'\0' + monitor[0])[0]

    table.add_row(
        "TE length",
        f"[green]{te_length}[/green]" if te_length == 5999999 else f"[red]{te_length}[/red]"
    )

    # TE offset
    monitor = mgr.monitor(CAN_CHANNEL, CAN_NODE, RCA_TE_OFFSET_COUNTER)
    te_offset = struct.unpack('>I', b'\0' + monitor[0])[0]

    table.add_row(
        "TE offset",
        f"[green]{te_offset}[/green]" if te_offset == 2 else f"[red]{te_offset}[/red]"
    )

    # STATUS bits
    monitor = mgr.monitor(CAN_CHANNEL, CAN_NODE, RCA_STATUS)
    status = struct.unpack('2B', monitor[0])

    flag_dcm_locked = 1 * bool(status[0] & FLAG_DCM_LOCKED)
    flag_12v_out_of_range = 1 * bool(status[0] & FLAG_12V_OUT_OF_RANGE)
    flag_15v_out_of_range = 1 * bool(status[0] & FLAG_15V_OUT_OF_RANGE)
    flag_rx_opt_pwr_error = 1 * bool(status[0] & FLAG_RX_OPT_PWR_ERROR)
    flag_2ghz_unlocked = 1 * bool(status[0] & FLAG_2GHZ_UNLOCKED)
    flag_125mhz_unlocked = 1 * bool(status[0] & FLAG_125MHZ_UNLOCKED)
    flag_te_short = 1 * bool(status[1] & FLAG_TE_SHORT)
    flag_te_long = 1 * bool(status[1] & FLAG_TE_LONG)

    flags = []
    if not flag_dcm_locked:
        flags.append("DCM unlocked")
    if flag_12v_out_of_range:
        flags.append("12V out of range")
    if flag_15v_out_of_range:
        flags.append("15V out of range")
    if flag_rx_opt_pwr_error:
        flags.append("Rx optical signal not detected")
    if flag_2ghz_unlocked:
        flags.append("2 GHz unlocked")
    if flag_125mhz_unlocked:
        flags.append("125 MHz unlocked")
    if flag_te_short:
        flags.append("TE short detected")
    if flag_te_long:
        flags.append("TE long detected")

    table.add_row(
        "125 MHz",
        f"[green]Locked[/green]" if not flag_125mhz_unlocked else f"[red]Unlocked[/red]"
    )

    table.add_row(
        "Error flags",
        "[red]" + "\n".join(flags) + "[/red]"
    )
    console = Console()
    print()
    console.print(table)
    print()

    print("Run 'alma-hilse timing resync' to sync to central reference and clear flags")
    print()

# @app.command("resync", short_help='Resync TE to central reference')
def resync_te():
    try:
        mgr = AmbManager('DMC')
    except:
        print("Failed to instantiate DMC AmbManager")

    clear_flags()
    mgr.command(CAN_CHANNEL, CAN_NODE, RCA_RESYNC_TE, struct.pack('1B', 0x01))
    print("Resync command was sent")
    status()

# @app.command("clear", short_help='Clear TE and PLL error flags')
def clear_flags():
    try:
        mgr = AmbManager('DMC')
    except:
        print("Failed to instantiate DMC AmbManager")

    mgr.command(CAN_CHANNEL, CAN_NODE, RCA_CLEAR_FLAGS, struct.pack('1B', 0x01))

    print("Clear flags command was sent")

# def main():
#     if len(sys.argv) == 1:
#         status()
#     else:
#         app()

# if __name__ == "__main__":
#     main()

