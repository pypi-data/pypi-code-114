from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scid:
	"""Scid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scid", core, parent)

	def set(self, scrambling_id: int, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CSIS:[CELL<CH0>]:SCID \n
		Snippet: driver.source.bb.eutra.downlink.csis.cell.scid.set(scrambling_id = 1, cellNull = repcap.CellNull.Default) \n
		Sets the additional scrambling identity n_ID used to generate the NonZeroTxPower CSI-RS. \n
			:param scrambling_id: integer Range: 0 to 503
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(scrambling_id)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:CSIS:CELL{cellNull_cmd_val}:SCID {param}')

	def get(self, cellNull=repcap.CellNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CSIS:[CELL<CH0>]:SCID \n
		Snippet: value: int = driver.source.bb.eutra.downlink.csis.cell.scid.get(cellNull = repcap.CellNull.Default) \n
		Sets the additional scrambling identity n_ID used to generate the NonZeroTxPower CSI-RS. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: scrambling_id: integer Range: 0 to 503"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:CSIS:CELL{cellNull_cmd_val}:SCID?')
		return Conversions.str_to_int(response)
