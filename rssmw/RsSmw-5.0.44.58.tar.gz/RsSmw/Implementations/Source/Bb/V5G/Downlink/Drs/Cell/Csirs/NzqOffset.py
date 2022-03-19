from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NzqOffset:
	"""NzqOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nzqOffset", core, parent)

	def set(self, non_zero_pq_offs: enums.V5GcSiRsNzpqOffset, cellNull=repcap.CellNull.Default, csiRefSignal=repcap.CsiRefSignal.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:DRS:CELL<CH0>:CSIRs<ST>:NZQoffset \n
		Snippet: driver.source.bb.v5G.downlink.drs.cell.csirs.nzqOffset.set(non_zero_pq_offs = enums.V5GcSiRsNzpqOffset.M1, cellNull = repcap.CellNull.Default, csiRefSignal = repcap.CsiRefSignal.Default) \n
		No command help available \n
			:param non_zero_pq_offs: No help available
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param csiRefSignal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Csirs')
		"""
		param = Conversions.enum_scalar_to_str(non_zero_pq_offs, enums.V5GcSiRsNzpqOffset)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		csiRefSignal_cmd_val = self._cmd_group.get_repcap_cmd_value(csiRefSignal, repcap.CsiRefSignal)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:DRS:CELL{cellNull_cmd_val}:CSIRs{csiRefSignal_cmd_val}:NZQoffset {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Default, csiRefSignal=repcap.CsiRefSignal.Default) -> enums.V5GcSiRsNzpqOffset:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:DRS:CELL<CH0>:CSIRs<ST>:NZQoffset \n
		Snippet: value: enums.V5GcSiRsNzpqOffset = driver.source.bb.v5G.downlink.drs.cell.csirs.nzqOffset.get(cellNull = repcap.CellNull.Default, csiRefSignal = repcap.CsiRefSignal.Default) \n
		No command help available \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param csiRefSignal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Csirs')
			:return: non_zero_pq_offs: No help available"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		csiRefSignal_cmd_val = self._cmd_group.get_repcap_cmd_value(csiRefSignal, repcap.CsiRefSignal)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:DRS:CELL{cellNull_cmd_val}:CSIRs{csiRefSignal_cmd_val}:NZQoffset?')
		return Conversions.str_to_scalar_enum(response, enums.V5GcSiRsNzpqOffset)
