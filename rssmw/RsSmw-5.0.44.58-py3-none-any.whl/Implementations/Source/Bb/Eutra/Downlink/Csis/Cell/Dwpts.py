from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dwpts:
	"""Dwpts commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dwpts", core, parent)

	def set(self, dwpts: bool, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CSIS:[CELL<CH0>]:DWPTs \n
		Snippet: driver.source.bb.eutra.downlink.csis.cell.dwpts.set(dwpts = False, cellNull = repcap.CellNull.Default) \n
		Enables transmission of the CSI-RS in the Downlink Pilot Time Slot (DwPTS) parts of the TDD frame. \n
			:param dwpts: 1| ON| 0| OFF
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.bool_to_str(dwpts)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:CSIS:CELL{cellNull_cmd_val}:DWPTs {param}')

	def get(self, cellNull=repcap.CellNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CSIS:[CELL<CH0>]:DWPTs \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.csis.cell.dwpts.get(cellNull = repcap.CellNull.Default) \n
		Enables transmission of the CSI-RS in the Downlink Pilot Time Slot (DwPTS) parts of the TDD frame. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: dwpts: 1| ON| 0| OFF"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:CSIS:CELL{cellNull_cmd_val}:DWPTs?')
		return Conversions.str_to_bool(response)
