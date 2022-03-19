from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UdConf:
	"""UdConf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("udConf", core, parent)

	def set(self, ulca_tdd_ul_dl_conf: int, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:CA:CELL<CH0>:UDConf \n
		Snippet: driver.source.bb.eutra.uplink.ca.cell.udConf.set(ulca_tdd_ul_dl_conf = 1, cellNull = repcap.CellNull.Default) \n
		Sets the Uplink-Downlink Configuration number. \n
			:param ulca_tdd_ul_dl_conf: integer Range: 0 to 6
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(ulca_tdd_ul_dl_conf)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:CA:CELL{cellNull_cmd_val}:UDConf {param}')

	def get(self, cellNull=repcap.CellNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:CA:CELL<CH0>:UDConf \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ca.cell.udConf.get(cellNull = repcap.CellNull.Default) \n
		Sets the Uplink-Downlink Configuration number. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: ulca_tdd_ul_dl_conf: integer Range: 0 to 6"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:CA:CELL{cellNull_cmd_val}:UDConf?')
		return Conversions.str_to_int(response)
