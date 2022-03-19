from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TaOffset:
	"""TaOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("taOffset", core, parent)

	def set(self, timing_adj_offset: enums.TimingAdjustmentOffsetAll, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:[TMPH]:TAOFfset \n
		Snippet: driver.source.bb.nr5G.node.cell.tmph.taOffset.set(timing_adj_offset = enums.TimingAdjustmentOffsetAll.N0, cellNull = repcap.CellNull.Nr0) \n
		Sets an offset (NTA offset) to the timing advance value for UL/DL switching synchronization as specified in . The NTA
		offset values can be set as specified in . \n
			:param timing_adj_offset: N0| N13792| N25600| N39936
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.enum_scalar_to_str(timing_adj_offset, enums.TimingAdjustmentOffsetAll)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:TMPH:TAOFfset {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Nr0) -> enums.TimingAdjustmentOffsetAll:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:[TMPH]:TAOFfset \n
		Snippet: value: enums.TimingAdjustmentOffsetAll = driver.source.bb.nr5G.node.cell.tmph.taOffset.get(cellNull = repcap.CellNull.Nr0) \n
		Sets an offset (NTA offset) to the timing advance value for UL/DL switching synchronization as specified in . The NTA
		offset values can be set as specified in . \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: timing_adj_offset: N0| N13792| N25600| N39936"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:TMPH:TAOFfset?')
		return Conversions.str_to_scalar_enum(response, enums.TimingAdjustmentOffsetAll)
