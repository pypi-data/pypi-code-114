from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nidcsi:
	"""Nidcsi commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nidcsi", core, parent)

	def set(self, ca_ni_dcsi: int, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:CA:CELL<CH0>:NIDCsi \n
		Snippet: driver.source.bb.v5G.downlink.ca.cell.nidcsi.set(ca_ni_dcsi = 1, cellNull = repcap.CellNull.Default) \n
		Sets the scrambling identity NIDCSI used to generate the CSI-RS signal. \n
			:param ca_ni_dcsi: integer Range: 0 to 503
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(ca_ni_dcsi)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:CA:CELL{cellNull_cmd_val}:NIDCsi {param}')

	def get(self, cellNull=repcap.CellNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:CA:CELL<CH0>:NIDCsi \n
		Snippet: value: int = driver.source.bb.v5G.downlink.ca.cell.nidcsi.get(cellNull = repcap.CellNull.Default) \n
		Sets the scrambling identity NIDCSI used to generate the CSI-RS signal. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: ca_ni_dcsi: integer Range: 0 to 503"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:CA:CELL{cellNull_cmd_val}:NIDCsi?')
		return Conversions.str_to_int(response)
