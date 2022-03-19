from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnsFrame:
	"""EnsFrame commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ensFrame", core, parent)

	def get(self, cellNull=repcap.CellNull.Default, burstNull=repcap.BurstNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:LAA:CELL<CH0>:BURSt<ST0>:ENSFrame \n
		Snippet: value: int = driver.source.bb.eutra.downlink.laa.cell.burst.ensFrame.get(cellNull = repcap.CellNull.Default, burstNull = repcap.BurstNull.Default) \n
		Queries the number of the last subframe of the LAA burst. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param burstNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Burst')
			:return: ending_sub_frame: integer Range: 0 to 39"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		burstNull_cmd_val = self._cmd_group.get_repcap_cmd_value(burstNull, repcap.BurstNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:LAA:CELL{cellNull_cmd_val}:BURSt{burstNull_cmd_val}:ENSFrame?')
		return Conversions.str_to_int(response)
