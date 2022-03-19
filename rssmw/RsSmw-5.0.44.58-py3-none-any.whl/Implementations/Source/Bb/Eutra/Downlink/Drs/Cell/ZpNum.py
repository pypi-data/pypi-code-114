from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ZpNum:
	"""ZpNum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("zpNum", core, parent)

	def set(self, num_zero_pwr_conf: int, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DRS:CELL<CH0>:ZPNum \n
		Snippet: driver.source.bb.eutra.downlink.drs.cell.zpNum.set(num_zero_pwr_conf = 1, cellNull = repcap.CellNull.Default) \n
		Enables up to 5 ZeroTxPower CSI-RS within the DRS period. \n
			:param num_zero_pwr_conf: integer Range: 0 to 5
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(num_zero_pwr_conf)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:DRS:CELL{cellNull_cmd_val}:ZPNum {param}')

	def get(self, cellNull=repcap.CellNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DRS:CELL<CH0>:ZPNum \n
		Snippet: value: int = driver.source.bb.eutra.downlink.drs.cell.zpNum.get(cellNull = repcap.CellNull.Default) \n
		Enables up to 5 ZeroTxPower CSI-RS within the DRS period. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: num_zero_pwr_conf: integer Range: 0 to 5"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:DRS:CELL{cellNull_cmd_val}:ZPNum?')
		return Conversions.str_to_int(response)
