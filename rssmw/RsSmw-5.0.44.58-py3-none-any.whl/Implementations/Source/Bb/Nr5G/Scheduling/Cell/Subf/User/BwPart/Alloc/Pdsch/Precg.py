from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import enums
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Precg:
	"""Precg commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("precg", core, parent)

	def set(self, user_alloc_pdschp: enums.DlpRbBundlingGranularity, cellNull=repcap.CellNull.Default, subframeNull=repcap.SubframeNull.Default, userNull=repcap.UserNull.Default, bwPartNull=repcap.BwPartNull.Default, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SCHed:CELL<CH0>:SUBF<ST0>:USER<DIR0>:BWPart<GR0>:ALLoc<USER0>:PDSCh:PRECg \n
		Snippet: driver.source.bb.nr5G.scheduling.cell.subf.user.bwPart.alloc.pdsch.precg.set(user_alloc_pdschp = enums.DlpRbBundlingGranularity.N2, cellNull = repcap.CellNull.Default, subframeNull = repcap.SubframeNull.Default, userNull = repcap.UserNull.Default, bwPartNull = repcap.BwPartNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		For PDSCH allocations, the precoding granularity can be adjusted. Precondition is that the precoding for the PDSCH is
		enabled under 'User/BWP Settings > DL BWP Config > PDSCH > General Settings > Static Bundle Size'. \n
			:param user_alloc_pdschp: N2| N4| WIDeband N2 Precoding granularity is set to N2. N4 Precoding granularity is set to N4. This setting is not available if: - [:SOURcehw]:BB:NR5G:UBWP:USERch0:CELLst0:DL:BWPdir0:PDSCh:VPINter equals 2 or - [:SOURcehw]:BB:NR5G:UBWP:USERch0:CELLst0:DL:BWPdir0:PDSCh:RBGSize equals Config1 and BWP size ≤ 36 RBs WIDeband Precoding granularity is set to wideband.
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'BwPart')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(user_alloc_pdschp, enums.DlpRbBundlingGranularity)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:SCHed:CELL{cellNull_cmd_val}:SUBF{subframeNull_cmd_val}:USER{userNull_cmd_val}:BWPart{bwPartNull_cmd_val}:ALLoc{allocationNull_cmd_val}:PDSCh:PRECg {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Default, subframeNull=repcap.SubframeNull.Default, userNull=repcap.UserNull.Default, bwPartNull=repcap.BwPartNull.Default, allocationNull=repcap.AllocationNull.Default) -> enums.DlpRbBundlingGranularity:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SCHed:CELL<CH0>:SUBF<ST0>:USER<DIR0>:BWPart<GR0>:ALLoc<USER0>:PDSCh:PRECg \n
		Snippet: value: enums.DlpRbBundlingGranularity = driver.source.bb.nr5G.scheduling.cell.subf.user.bwPart.alloc.pdsch.precg.get(cellNull = repcap.CellNull.Default, subframeNull = repcap.SubframeNull.Default, userNull = repcap.UserNull.Default, bwPartNull = repcap.BwPartNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		For PDSCH allocations, the precoding granularity can be adjusted. Precondition is that the precoding for the PDSCH is
		enabled under 'User/BWP Settings > DL BWP Config > PDSCH > General Settings > Static Bundle Size'. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'BwPart')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: user_alloc_pdschp: N2| N4| WIDeband N2 Precoding granularity is set to N2. N4 Precoding granularity is set to N4. This setting is not available if: - [:SOURcehw]:BB:NR5G:UBWP:USERch0:CELLst0:DL:BWPdir0:PDSCh:VPINter equals 2 or - [:SOURcehw]:BB:NR5G:UBWP:USERch0:CELLst0:DL:BWPdir0:PDSCh:RBGSize equals Config1 and BWP size ≤ 36 RBs WIDeband Precoding granularity is set to wideband."""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:SCHed:CELL{cellNull_cmd_val}:SUBF{subframeNull_cmd_val}:USER{userNull_cmd_val}:BWPart{bwPartNull_cmd_val}:ALLoc{allocationNull_cmd_val}:PDSCh:PRECg?')
		return Conversions.str_to_scalar_enum(response, enums.DlpRbBundlingGranularity)
