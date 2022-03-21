import math
import struct
try:
    from CCL.AmbManager import AmbManager
    import ControlExceptions
except ModuleNotFoundError:
    print("Failed to import CCL.AmbManager or ControlExceptions")

from rich.table import Table
from rich.console import Console

## Definitions
# DRXs CAN bus definitions
CAN_CHANNEL_DRX0 = 2
CAN_NODE_DRX0 = 0x100
CAN_CHANNEL_DRX1 = 2
CAN_NODE_DRX1 = 0x101

# Monitor point definitions
RCA_GET_SIGNAL_AVG_D = 0x03102
RCA_GET_SIGNAL_AVG_C = 0x03202
RCA_GET_SIGNAL_AVG_B = 0x03302
RCA_GET_PARITY_COUNTER_D = 0x1502
RCA_GET_PARITY_COUNTER_C = 0x2502
RCA_GET_PARITY_COUNTER_B = 0x3502

def get_drx_status():
    '''HILSE correlator DRXs 0 and 1 average bits power'''

    try:
        mgr = AmbManager('DMC')
    except:
        print()
        print("Failed to instantiate DMC AmbManager")
        print()
        return

    table = Table(title='HILSE CORR DRXs status')
    table.add_column('DRX/bit', justify='right')
    table.add_column('Avg pwr \[nW]', justify='right')
    table.add_column('Avg pwr \[dBm]', justify='right')
    table.add_column('Parity counter \[]', justify='right')

    # Received optical power and parity counter per bit
    for channel, node, rca_pwr, rca_parity, label in [
        (CAN_CHANNEL_DRX0, CAN_NODE_DRX0, RCA_GET_SIGNAL_AVG_D, RCA_GET_PARITY_COUNTER_D, "DRX0 bit D"),
        (CAN_CHANNEL_DRX0, CAN_NODE_DRX0, RCA_GET_SIGNAL_AVG_C, RCA_GET_PARITY_COUNTER_C, "DRX0 bit C"),
        (CAN_CHANNEL_DRX0, CAN_NODE_DRX0, RCA_GET_SIGNAL_AVG_B, RCA_GET_PARITY_COUNTER_B, "DRX0 bit B"),
        (CAN_CHANNEL_DRX1, CAN_NODE_DRX1, RCA_GET_SIGNAL_AVG_D, RCA_GET_PARITY_COUNTER_D, "DRX1 bit D"),
        (CAN_CHANNEL_DRX1, CAN_NODE_DRX1, RCA_GET_SIGNAL_AVG_C, RCA_GET_PARITY_COUNTER_C, "DRX1 bit C"),
        (CAN_CHANNEL_DRX1, CAN_NODE_DRX1, RCA_GET_SIGNAL_AVG_B, RCA_GET_PARITY_COUNTER_B, "DRX1 bit B"),
    ]:
        try:
            monitor = mgr.monitor(channel, node, rca_pwr)
        except ControlExceptions.CAMBErrorEx:
            raise Exception(f"Node {hex(node)} not found on CAN bus")

        power_nw = int.from_bytes(monitor[0], 'big', signed=True)
        power_dbm = 10 * math.log10(power_nw / 1e6)

        good_power = True
        if power_dbm < -15:
            good_power = False
        if power_dbm > -3:
            good_power = False

        try:
            monitor = mgr.monitor(channel, node, rca_parity)
        except ControlExceptions.CAMBErrorEx:
            raise Exception(f"Node {hex(node)} not found on CAN bus")

        parity_counter = struct.unpack('>Q', monitor[0])[0]

        table.add_row(
            label,
            f"{power_nw}",
            f"[green]{power_dbm:.2f}[/green]" if good_power else f"[red]{power_dbm:.2f}[/red]",
            str(parity_counter)
        )

    console = Console()
    print()
    console.print(table)
    print()