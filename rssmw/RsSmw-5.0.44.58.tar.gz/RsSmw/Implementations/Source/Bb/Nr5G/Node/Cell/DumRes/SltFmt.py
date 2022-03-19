from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SltFmt:
	"""SltFmt commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sltFmt", core, parent)

	def set(self, slot_fmt: int, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:DUMRes:SLTFmt \n
		Snippet: driver.source.bb.nr5G.node.cell.dumRes.sltFmt.set(slot_fmt = 1, cellNull = repcap.CellNull.Nr0) \n
		No command help available \n
			:param slot_fmt: No help available
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.decimal_value_to_str(slot_fmt)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:DUMRes:SLTFmt {param}')

	def get(self, cellNull=repcap.CellNull.Nr0) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:DUMRes:SLTFmt \n
		Snippet: value: int = driver.source.bb.nr5G.node.cell.dumRes.sltFmt.get(cellNull = repcap.CellNull.Nr0) \n
		No command help available \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: slot_fmt: No help available"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:DUMRes:SLTFmt?')
		return Conversions.str_to_int(response)
