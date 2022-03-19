from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup
from .............Internal import Conversions
from .............Internal.RepeatedCapability import RepeatedCapability
from ............. import enums
from ............. import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApSelect:
	"""ApSelect commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: AntennaPortNull, default value after init: AntennaPortNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("apSelect", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_antennaPortNull_get', 'repcap_antennaPortNull_set', repcap.AntennaPortNull.Nr0)

	def repcap_antennaPortNull_set(self, antennaPortNull: repcap.AntennaPortNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to AntennaPortNull.Default
		Default value after init: AntennaPortNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(antennaPortNull)

	def repcap_antennaPortNull_get(self) -> repcap.AntennaPortNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, pdsch_ap_sel: enums.Nr5GpdschAp, cellNull=repcap.CellNull.Default, subframeNull=repcap.SubframeNull.Default, userNull=repcap.UserNull.Default, bwPartNull=repcap.BwPartNull.Default, allocationNull=repcap.AllocationNull.Default, antennaPortNull=repcap.AntennaPortNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SCHed:CELL<CH0>:SUBF<ST0>:USER<DIR0>:BWPart<GR0>:ALLoc<USER0>:PDSCh:[DMRS]:APSelect<S2US0> \n
		Snippet: driver.source.bb.nr5G.scheduling.cell.subf.user.bwPart.alloc.pdsch.dmrs.apSelect.set(pdsch_ap_sel = enums.Nr5GpdschAp.AP1000, cellNull = repcap.CellNull.Default, subframeNull = repcap.SubframeNull.Default, userNull = repcap.UserNull.Default, bwPartNull = repcap.BwPartNull.Default, allocationNull = repcap.AllocationNull.Default, antennaPortNull = repcap.AntennaPortNull.Default) \n
		Each layer of a PDSCH allocation is mapped to a certain antenna port. By the command the antenna ports are selected which
		are used for the transmission of the PDSCH allocation. \n
			:param pdsch_ap_sel: AP1000| AP1001| AP1002| AP1003| AP1004| AP1005| AP1006| AP1007| AP1008| AP1009| AP1010| AP1011
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'BwPart')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:param antennaPortNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'ApSelect')
		"""
		param = Conversions.enum_scalar_to_str(pdsch_ap_sel, enums.Nr5GpdschAp)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		antennaPortNull_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPortNull, repcap.AntennaPortNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:SCHed:CELL{cellNull_cmd_val}:SUBF{subframeNull_cmd_val}:USER{userNull_cmd_val}:BWPart{bwPartNull_cmd_val}:ALLoc{allocationNull_cmd_val}:PDSCh:DMRS:APSelect{antennaPortNull_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Default, subframeNull=repcap.SubframeNull.Default, userNull=repcap.UserNull.Default, bwPartNull=repcap.BwPartNull.Default, allocationNull=repcap.AllocationNull.Default, antennaPortNull=repcap.AntennaPortNull.Default) -> enums.Nr5GpdschAp:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SCHed:CELL<CH0>:SUBF<ST0>:USER<DIR0>:BWPart<GR0>:ALLoc<USER0>:PDSCh:[DMRS]:APSelect<S2US0> \n
		Snippet: value: enums.Nr5GpdschAp = driver.source.bb.nr5G.scheduling.cell.subf.user.bwPart.alloc.pdsch.dmrs.apSelect.get(cellNull = repcap.CellNull.Default, subframeNull = repcap.SubframeNull.Default, userNull = repcap.UserNull.Default, bwPartNull = repcap.BwPartNull.Default, allocationNull = repcap.AllocationNull.Default, antennaPortNull = repcap.AntennaPortNull.Default) \n
		Each layer of a PDSCH allocation is mapped to a certain antenna port. By the command the antenna ports are selected which
		are used for the transmission of the PDSCH allocation. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'BwPart')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:param antennaPortNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'ApSelect')
			:return: pdsch_ap_sel: AP1000| AP1001| AP1002| AP1003| AP1004| AP1005| AP1006| AP1007| AP1008| AP1009| AP1010| AP1011"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		antennaPortNull_cmd_val = self._cmd_group.get_repcap_cmd_value(antennaPortNull, repcap.AntennaPortNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:SCHed:CELL{cellNull_cmd_val}:SUBF{subframeNull_cmd_val}:USER{userNull_cmd_val}:BWPart{bwPartNull_cmd_val}:ALLoc{allocationNull_cmd_val}:PDSCh:DMRS:APSelect{antennaPortNull_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.Nr5GpdschAp)

	def clone(self) -> 'ApSelect':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ApSelect(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
