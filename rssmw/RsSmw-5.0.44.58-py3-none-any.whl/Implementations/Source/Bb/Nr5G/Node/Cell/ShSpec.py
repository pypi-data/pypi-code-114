from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ShSpec:
	"""ShSpec commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("shSpec", core, parent)

	def set(self, shared_spec: bool, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:SHSPec \n
		Snippet: driver.source.bb.nr5G.node.cell.shSpec.set(shared_spec = False, cellNull = repcap.CellNull.Nr0) \n
		Turns shared spectrum access on and off. \n
			:param shared_spec: 1| ON| 0| OFF
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.bool_to_str(shared_spec)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:SHSPec {param}')

	def get(self, cellNull=repcap.CellNull.Nr0) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:SHSPec \n
		Snippet: value: bool = driver.source.bb.nr5G.node.cell.shSpec.get(cellNull = repcap.CellNull.Nr0) \n
		Turns shared spectrum access on and off. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: shared_spec: No help available"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:SHSPec?')
		return Conversions.str_to_bool(response)
