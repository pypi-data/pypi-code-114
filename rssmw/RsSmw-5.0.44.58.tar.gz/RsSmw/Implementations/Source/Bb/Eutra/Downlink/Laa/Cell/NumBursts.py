from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NumBursts:
	"""NumBursts commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("numBursts", core, parent)

	def set(self, number_of_bursts: int, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:LAA:CELL<CH0>:NUMBursts \n
		Snippet: driver.source.bb.eutra.downlink.laa.cell.numBursts.set(number_of_bursts = 1, cellNull = repcap.CellNull.Default) \n
		Set the number of LAA bursts. \n
			:param number_of_bursts: integer Range: 0 to 10
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(number_of_bursts)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:LAA:CELL{cellNull_cmd_val}:NUMBursts {param}')

	def get(self, cellNull=repcap.CellNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:LAA:CELL<CH0>:NUMBursts \n
		Snippet: value: int = driver.source.bb.eutra.downlink.laa.cell.numBursts.get(cellNull = repcap.CellNull.Default) \n
		Set the number of LAA bursts. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: number_of_bursts: integer Range: 0 to 10"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:LAA:CELL{cellNull_cmd_val}:NUMBursts?')
		return Conversions.str_to_int(response)
