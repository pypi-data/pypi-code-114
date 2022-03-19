from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, scs_offset: float, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:TXBW:S60K:OFFSet \n
		Snippet: driver.source.bb.nr5G.node.cell.txbw.s60K.offset.set(scs_offset = 1.0, cellNull = repcap.CellNull.Nr0) \n
		Sets the offset between the usable RB and the common RBs. \n
			:param scs_offset: float Range: 0 to 9
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.decimal_value_to_str(scs_offset)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:TXBW:S60K:OFFSet {param}')

	def get(self, cellNull=repcap.CellNull.Nr0) -> float:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:TXBW:S60K:OFFSet \n
		Snippet: value: float = driver.source.bb.nr5G.node.cell.txbw.s60K.offset.get(cellNull = repcap.CellNull.Nr0) \n
		Sets the offset between the usable RB and the common RBs. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: scs_offset: float Range: 0 to 9"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:TXBW:S60K:OFFSet?')
		return Conversions.str_to_float(response)
