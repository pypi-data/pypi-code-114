from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StsFrame:
	"""StsFrame commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stsFrame", core, parent)

	def set(self, starting_sf: int, cellNull=repcap.CellNull.Default, burstNull=repcap.BurstNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:LAA:CELL<CH0>:BURSt<ST0>:STSFrame \n
		Snippet: driver.source.bb.eutra.downlink.laa.cell.burst.stsFrame.set(starting_sf = 1, cellNull = repcap.CellNull.Default, burstNull = repcap.BurstNull.Default) \n
		Sets the first subframe of the LAA bust. \n
			:param starting_sf: integer Range: 0 to 39
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param burstNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Burst')
		"""
		param = Conversions.decimal_value_to_str(starting_sf)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		burstNull_cmd_val = self._cmd_group.get_repcap_cmd_value(burstNull, repcap.BurstNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:LAA:CELL{cellNull_cmd_val}:BURSt{burstNull_cmd_val}:STSFrame {param}')

	def get(self, cellNull=repcap.CellNull.Default, burstNull=repcap.BurstNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:LAA:CELL<CH0>:BURSt<ST0>:STSFrame \n
		Snippet: value: int = driver.source.bb.eutra.downlink.laa.cell.burst.stsFrame.get(cellNull = repcap.CellNull.Default, burstNull = repcap.BurstNull.Default) \n
		Sets the first subframe of the LAA bust. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param burstNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Burst')
			:return: starting_sf: integer Range: 0 to 39"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		burstNull_cmd_val = self._cmd_group.get_repcap_cmd_value(burstNull, repcap.BurstNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:LAA:CELL{cellNull_cmd_val}:BURSt{burstNull_cmd_val}:STSFrame?')
		return Conversions.str_to_int(response)
