from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sfi:
	"""Sfi commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sfi", core, parent)

	def set(self, csi_rs_sf_conf: int, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CSIS:[CELL<CH0>]:SFI \n
		Snippet: driver.source.bb.eutra.downlink.csis.cell.sfi.set(csi_rs_sf_conf = 1, cellNull = repcap.CellNull.Default) \n
		Sets the parameter ICSI-RS for cell-specific CSI-RS. \n
			:param csi_rs_sf_conf: integer Range: 0 to 154
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(csi_rs_sf_conf)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:CSIS:CELL{cellNull_cmd_val}:SFI {param}')

	def get(self, cellNull=repcap.CellNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CSIS:[CELL<CH0>]:SFI \n
		Snippet: value: int = driver.source.bb.eutra.downlink.csis.cell.sfi.get(cellNull = repcap.CellNull.Default) \n
		Sets the parameter ICSI-RS for cell-specific CSI-RS. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: csi_rs_sf_conf: integer Range: 0 to 154"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:CSIS:CELL{cellNull_cmd_val}:SFI?')
		return Conversions.str_to_int(response)
