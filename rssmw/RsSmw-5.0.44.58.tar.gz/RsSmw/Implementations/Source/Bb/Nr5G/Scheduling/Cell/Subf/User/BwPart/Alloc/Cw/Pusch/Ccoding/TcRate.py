from ..............Internal.Core import Core
from ..............Internal.CommandsGroup import CommandsGroup
from ..............Internal import Conversions
from .............. import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TcRate:
	"""TcRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tcRate", core, parent)

	def set(self, target_code_rate: float, cellNull=repcap.CellNull.Default, subframeNull=repcap.SubframeNull.Default, userNull=repcap.UserNull.Default, bwPartNull=repcap.BwPartNull.Default, allocationNull=repcap.AllocationNull.Default, codewordNull=repcap.CodewordNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SCHed:CELL<CH0>:SUBF<ST0>:USER<DIR0>:BWPart<GR0>:ALLoc<USER0>:[CW<S2US0>]:PUSCh:CCODing:TCRate \n
		Snippet: driver.source.bb.nr5G.scheduling.cell.subf.user.bwPart.alloc.cw.pusch.ccoding.tcRate.set(target_code_rate = 1.0, cellNull = repcap.CellNull.Default, subframeNull = repcap.SubframeNull.Default, userNull = repcap.UserNull.Default, bwPartNull = repcap.BwPartNull.Default, allocationNull = repcap.AllocationNull.Default, codewordNull = repcap.CodewordNull.Default) \n
		Queries the target code rate for the selected modulation and coding scheme. Setting the coderate is possible when you
		turn on manual coderate definition
		([:SOURce<hw>]:BB:NR5G:SCHed:CELL<ch0>:SUBF<st0>:USER<dir0>:BWPart<gr0>:ALLoc<user0>[:CW<s2us0>]:PDSCh|PUSCh:CCODing:FRCR)
		. \n
			:param target_code_rate: float Range: 0.0 to 1.0
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'BwPart')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:param codewordNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cw')
		"""
		param = Conversions.decimal_value_to_str(target_code_rate)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		codewordNull_cmd_val = self._cmd_group.get_repcap_cmd_value(codewordNull, repcap.CodewordNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:SCHed:CELL{cellNull_cmd_val}:SUBF{subframeNull_cmd_val}:USER{userNull_cmd_val}:BWPart{bwPartNull_cmd_val}:ALLoc{allocationNull_cmd_val}:CW{codewordNull_cmd_val}:PUSCh:CCODing:TCRate {param}')

	def get(self, cellNull=repcap.CellNull.Default, subframeNull=repcap.SubframeNull.Default, userNull=repcap.UserNull.Default, bwPartNull=repcap.BwPartNull.Default, allocationNull=repcap.AllocationNull.Default, codewordNull=repcap.CodewordNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:NR5G:SCHed:CELL<CH0>:SUBF<ST0>:USER<DIR0>:BWPart<GR0>:ALLoc<USER0>:[CW<S2US0>]:PUSCh:CCODing:TCRate \n
		Snippet: value: float = driver.source.bb.nr5G.scheduling.cell.subf.user.bwPart.alloc.cw.pusch.ccoding.tcRate.get(cellNull = repcap.CellNull.Default, subframeNull = repcap.SubframeNull.Default, userNull = repcap.UserNull.Default, bwPartNull = repcap.BwPartNull.Default, allocationNull = repcap.AllocationNull.Default, codewordNull = repcap.CodewordNull.Default) \n
		Queries the target code rate for the selected modulation and coding scheme. Setting the coderate is possible when you
		turn on manual coderate definition
		([:SOURce<hw>]:BB:NR5G:SCHed:CELL<ch0>:SUBF<st0>:USER<dir0>:BWPart<gr0>:ALLoc<user0>[:CW<s2us0>]:PDSCh|PUSCh:CCODing:FRCR)
		. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'BwPart')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:param codewordNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cw')
			:return: target_code_rate: float Range: 0.0 to 1.0"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		codewordNull_cmd_val = self._cmd_group.get_repcap_cmd_value(codewordNull, repcap.CodewordNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:SCHed:CELL{cellNull_cmd_val}:SUBF{subframeNull_cmd_val}:USER{userNull_cmd_val}:BWPart{bwPartNull_cmd_val}:ALLoc{allocationNull_cmd_val}:CW{codewordNull_cmd_val}:PUSCh:CCODing:TCRate?')
		return Conversions.str_to_float(response)
