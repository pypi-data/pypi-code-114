from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NzsCid:
	"""NzsCid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nzsCid", core, parent)

	def set(self, scrambling_id: int, cellNull=repcap.CellNull.Default, csiRefSignal=repcap.CsiRefSignal.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:DRS:CELL<CH0>:CSIRs<ST>:NZSCid \n
		Snippet: driver.source.bb.v5G.downlink.drs.cell.csirs.nzsCid.set(scrambling_id = 1, cellNull = repcap.CellNull.Default, csiRefSignal = repcap.CsiRefSignal.Default) \n
		No command help available \n
			:param scrambling_id: No help available
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param csiRefSignal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Csirs')
		"""
		param = Conversions.decimal_value_to_str(scrambling_id)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		csiRefSignal_cmd_val = self._cmd_group.get_repcap_cmd_value(csiRefSignal, repcap.CsiRefSignal)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:DRS:CELL{cellNull_cmd_val}:CSIRs{csiRefSignal_cmd_val}:NZSCid {param}')

	def get(self, cellNull=repcap.CellNull.Default, csiRefSignal=repcap.CsiRefSignal.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:DRS:CELL<CH0>:CSIRs<ST>:NZSCid \n
		Snippet: value: int = driver.source.bb.v5G.downlink.drs.cell.csirs.nzsCid.get(cellNull = repcap.CellNull.Default, csiRefSignal = repcap.CsiRefSignal.Default) \n
		No command help available \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param csiRefSignal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Csirs')
			:return: scrambling_id: No help available"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		csiRefSignal_cmd_val = self._cmd_group.get_repcap_cmd_value(csiRefSignal, repcap.CsiRefSignal)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:DRS:CELL{cellNull_cmd_val}:CSIRs{csiRefSignal_cmd_val}:NZSCid?')
		return Conversions.str_to_int(response)
