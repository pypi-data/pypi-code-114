from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ...........Internal.RepeatedCapability import RepeatedCapability
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ndmrs:
	"""Ndmrs commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: LayerNull, default value after init: LayerNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ndmrs", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_layerNull_get', 'repcap_layerNull_set', repcap.LayerNull.Nr0)

	def repcap_layerNull_set(self, layerNull: repcap.LayerNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to LayerNull.Default
		Default value after init: LayerNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(layerNull)

	def repcap_layerNull_get(self) -> repcap.LayerNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def get(self, cellNull=repcap.CellNull.Default, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default, layerNull=repcap.LayerNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:[CELL<CCIDX>]:[SUBF<ST0>]:ALLoc<CH0>:PUSCh:DRS:NDMRs<LAYER> \n
		Snippet: value: int = driver.source.bb.eutra.uplink.cell.subf.alloc.pusch.drs.ndmrs.get(cellNull = repcap.CellNull.Default, subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default, layerNull = repcap.LayerNull.Default) \n
		Queries the parameter n(2) _DMRS,λ (Layer λ) . \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:param layerNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Ndmrs')
			:return: ndmrs: integer Range: 0 to 11"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		layerNull_cmd_val = self._cmd_group.get_repcap_cmd_value(layerNull, repcap.LayerNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:CELL{cellNull_cmd_val}:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:PUSCh:DRS:NDMRs{layerNull_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Ndmrs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ndmrs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
