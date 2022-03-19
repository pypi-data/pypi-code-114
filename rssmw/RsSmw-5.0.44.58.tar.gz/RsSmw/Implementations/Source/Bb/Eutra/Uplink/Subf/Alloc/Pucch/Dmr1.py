from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dmr1:
	"""Dmr1 commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dmr1", core, parent)

	def set(self, pucc_dmrs_1: enums.EutraPuccN1Dmrs, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:[SUBF<ST0>]:ALLoc<CH0>:PUCCh:DMR1 \n
		Snippet: driver.source.bb.eutra.uplink.subf.alloc.pucch.dmr1.set(pucc_dmrs_1 = enums.EutraPuccN1Dmrs._0, subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		Sets the index n(2) DMRS. \n
			:param pucc_dmrs_1: 0| 2| 3| 4| 6| 8| 9| 10
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.enum_scalar_to_str(pucc_dmrs_1, enums.EutraPuccN1Dmrs)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:PUCCh:DMR1 {param}')

	# noinspection PyTypeChecker
	def get(self, subframeNull=repcap.SubframeNull.Default, allocationNull=repcap.AllocationNull.Default) -> enums.EutraPuccN1Dmrs:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:[SUBF<ST0>]:ALLoc<CH0>:PUCCh:DMR1 \n
		Snippet: value: enums.EutraPuccN1Dmrs = driver.source.bb.eutra.uplink.subf.alloc.pucch.dmr1.get(subframeNull = repcap.SubframeNull.Default, allocationNull = repcap.AllocationNull.Default) \n
		Sets the index n(2) DMRS. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: pucc_dmrs_1: 0| 2| 3| 4| 6| 8| 9| 10"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:SUBF{subframeNull_cmd_val}:ALLoc{allocationNull_cmd_val}:PUCCh:DMR1?')
		return Conversions.str_to_scalar_enum(response, enums.EutraPuccN1Dmrs)
