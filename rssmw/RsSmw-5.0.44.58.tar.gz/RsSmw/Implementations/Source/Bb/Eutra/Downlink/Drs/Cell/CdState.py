from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CdState:
	"""CdState commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cdState", core, parent)

	def set(self, csi_rs_state: bool, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DRS:CELL<CH0>:CDSTate \n
		Snippet: driver.source.bb.eutra.downlink.drs.cell.cdState.set(csi_rs_state = False, cellNull = repcap.CellNull.Default) \n
		Enables defining the CSI-RS part of the DRS. \n
			:param csi_rs_state: 1| ON| 0| OFF
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.bool_to_str(csi_rs_state)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:DRS:CELL{cellNull_cmd_val}:CDSTate {param}')

	def get(self, cellNull=repcap.CellNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DRS:CELL<CH0>:CDSTate \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.drs.cell.cdState.get(cellNull = repcap.CellNull.Default) \n
		Enables defining the CSI-RS part of the DRS. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: csi_rs_state: 1| ON| 0| OFF"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:DRS:CELL{cellNull_cmd_val}:CDSTate?')
		return Conversions.str_to_bool(response)
