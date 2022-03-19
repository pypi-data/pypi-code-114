from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Config:
	"""Config commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("config", core, parent)

	def set(self, csi_rs_config: int, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CSIS:[CELL<CH0>]:CONFig \n
		Snippet: driver.source.bb.eutra.downlink.csis.cell.config.set(csi_rs_config = 1, cellNull = repcap.CellNull.Default) \n
		Defines the CSI-RS configuration used for the current cell and for which the UE assumes non-zero transmission power. \n
			:param csi_rs_config: integer Range: 0 to 31
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(csi_rs_config)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:CSIS:CELL{cellNull_cmd_val}:CONFig {param}')

	def get(self, cellNull=repcap.CellNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CSIS:[CELL<CH0>]:CONFig \n
		Snippet: value: int = driver.source.bb.eutra.downlink.csis.cell.config.get(cellNull = repcap.CellNull.Default) \n
		Defines the CSI-RS configuration used for the current cell and for which the UE assumes non-zero transmission power. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: csi_rs_config: integer Range: 0 to 31"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:CSIS:CELL{cellNull_cmd_val}:CONFig?')
		return Conversions.str_to_int(response)
