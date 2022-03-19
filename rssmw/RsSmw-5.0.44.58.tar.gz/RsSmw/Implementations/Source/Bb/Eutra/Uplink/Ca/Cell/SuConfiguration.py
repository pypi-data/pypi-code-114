from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SuConfiguration:
	"""SuConfiguration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("suConfiguration", core, parent)

	def set(self, ulca_srs_subf_conf: int, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:CA:CELL<CH0>:SUConfiguration \n
		Snippet: driver.source.bb.eutra.uplink.ca.cell.suConfiguration.set(ulca_srs_subf_conf = 1, cellNull = repcap.CellNull.Default) \n
		Sets the SRS subframe configuration per component carrier. \n
			:param ulca_srs_subf_conf: integer Range: 0 to 15
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(ulca_srs_subf_conf)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:CA:CELL{cellNull_cmd_val}:SUConfiguration {param}')

	def get(self, cellNull=repcap.CellNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:CA:CELL<CH0>:SUConfiguration \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ca.cell.suConfiguration.get(cellNull = repcap.CellNull.Default) \n
		Sets the SRS subframe configuration per component carrier. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: ulca_srs_subf_conf: integer Range: 0 to 15"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:CA:CELL{cellNull_cmd_val}:SUConfiguration?')
		return Conversions.str_to_int(response)
