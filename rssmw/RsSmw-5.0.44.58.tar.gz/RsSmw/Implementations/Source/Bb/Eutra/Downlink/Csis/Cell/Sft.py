from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sft:
	"""Sft commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sft", core, parent)

	def get(self, cellNull=repcap.CellNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CSIS:[CELL<CH0>]:SFT \n
		Snippet: value: int = driver.source.bb.eutra.downlink.csis.cell.sft.get(cellNull = repcap.CellNull.Default) \n
		Queires the parameter subframe configuration period TCSI-RS for cell-specific CSI-RS. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: csi_rs_period: integer Range: 5 to 80"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:CSIS:CELL{cellNull_cmd_val}:SFT?')
		return Conversions.str_to_int(response)
