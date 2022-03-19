from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tdelay:
	"""Tdelay commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tdelay", core, parent)

	def set(self, time_delay: int, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:CA:CELL<CH0>:TDELay \n
		Snippet: driver.source.bb.eutra.uplink.ca.cell.tdelay.set(time_delay = 1, cellNull = repcap.CellNull.Default) \n
		Sets the time delay of the SCell relative to the PCell. \n
			:param time_delay: integer Range: 0 to 7E5
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(time_delay)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:CA:CELL{cellNull_cmd_val}:TDELay {param}')

	def get(self, cellNull=repcap.CellNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:CA:CELL<CH0>:TDELay \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ca.cell.tdelay.get(cellNull = repcap.CellNull.Default) \n
		Sets the time delay of the SCell relative to the PCell. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: time_delay: integer Range: 0 to 7E5"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:CA:CELL{cellNull_cmd_val}:TDELay?')
		return Conversions.str_to_int(response)
