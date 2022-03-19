from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nap:
	"""Nap commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nap", core, parent)

	def set(self, csi_rs_num_ap: enums.CsiRsNumAp, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CSIS:[CELL<CH0>]:NAP \n
		Snippet: driver.source.bb.eutra.downlink.csis.cell.nap.set(csi_rs_num_ap = enums.CsiRsNumAp.AP1, cellNull = repcap.CellNull.Default) \n
		Defines the number of antenna ports the CSI-RS are transmitted on. \n
			:param csi_rs_num_ap: AP1| AP2| AP4| AP8
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(csi_rs_num_ap, enums.CsiRsNumAp)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:CSIS:CELL{cellNull_cmd_val}:NAP {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Default) -> enums.CsiRsNumAp:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CSIS:[CELL<CH0>]:NAP \n
		Snippet: value: enums.CsiRsNumAp = driver.source.bb.eutra.downlink.csis.cell.nap.get(cellNull = repcap.CellNull.Default) \n
		Defines the number of antenna ports the CSI-RS are transmitted on. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: csi_rs_num_ap: AP1| AP2| AP4| AP8"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:CSIS:CELL{cellNull_cmd_val}:NAP?')
		return Conversions.str_to_scalar_enum(response, enums.CsiRsNumAp)
