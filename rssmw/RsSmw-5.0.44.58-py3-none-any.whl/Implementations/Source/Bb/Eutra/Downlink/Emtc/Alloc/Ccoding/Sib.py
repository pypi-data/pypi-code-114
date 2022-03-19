from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sib:
	"""Sib commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sib", core, parent)

	def set(self, scheduling_sib_1: int, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:ALLoc<CH0>:CCODing:SIB \n
		Snippet: driver.source.bb.eutra.downlink.emtc.alloc.ccoding.sib.set(scheduling_sib_1 = 1, allocationNull = repcap.AllocationNull.Default) \n
		Sets the parameter schedulingInfoSIB1-RB and defines the PDSCH number of repetitions. Query the resulting number of
		repetitions with the command [:SOURce<hw>]:BB:EUTRa:DL:EMTC:ALLoc<ch0>:CCODing:RSIB?. \n
			:param scheduling_sib_1: integer Range: 0 to 18
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(scheduling_sib_1)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:ALLoc{allocationNull_cmd_val}:CCODing:SIB {param}')

	def get(self, allocationNull=repcap.AllocationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:ALLoc<CH0>:CCODing:SIB \n
		Snippet: value: int = driver.source.bb.eutra.downlink.emtc.alloc.ccoding.sib.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the parameter schedulingInfoSIB1-RB and defines the PDSCH number of repetitions. Query the resulting number of
		repetitions with the command [:SOURce<hw>]:BB:EUTRa:DL:EMTC:ALLoc<ch0>:CCODing:RSIB?. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: scheduling_sib_1: integer Range: 0 to 18"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:ALLoc{allocationNull_cmd_val}:CCODing:SIB?')
		return Conversions.str_to_int(response)
