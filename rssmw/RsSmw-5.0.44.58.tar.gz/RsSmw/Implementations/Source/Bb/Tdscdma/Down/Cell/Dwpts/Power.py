from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def set(self, power: float, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:DWPTs:POWer \n
		Snippet: driver.source.bb.tdscdma.down.cell.dwpts.power.set(power = 1.0, cell = repcap.Cell.Default) \n
		Sets the power of the downlink/uplink pilot time slot. \n
			:param power: float Range: -80 to 10
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(power)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:DWPTs:POWer {param}')

	def get(self, cell=repcap.Cell.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:DWPTs:POWer \n
		Snippet: value: float = driver.source.bb.tdscdma.down.cell.dwpts.power.get(cell = repcap.Cell.Default) \n
		Sets the power of the downlink/uplink pilot time slot. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: power: float Range: -80 to 10"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:DWPTs:POWer?')
		return Conversions.str_to_float(response)
