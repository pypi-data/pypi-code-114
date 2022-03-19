from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HpNumber:
	"""HpNumber commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hpNumber", core, parent)

	def set(self, harq_process_num: int, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:HPNMber \n
		Snippet: driver.source.bb.eutra.downlink.niot.dci.alloc.hpNumber.set(harq_process_num = 1, allocationNull = repcap.AllocationNull.Default) \n
		Sets the HARQ processes number, for UEs for that [:SOURce<hw>]:BB:EUTRa:DL:USER<ch>:STHP:STATe1. \n
			:param harq_process_num: integer Range: 0 to 1
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(harq_process_num)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:HPNMber {param}')

	def get(self, allocationNull=repcap.AllocationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:HPNMber \n
		Snippet: value: int = driver.source.bb.eutra.downlink.niot.dci.alloc.hpNumber.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the HARQ processes number, for UEs for that [:SOURce<hw>]:BB:EUTRa:DL:USER<ch>:STHP:STATe1. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: harq_process_num: integer Range: 0 to 1"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:HPNMber?')
		return Conversions.str_to_int(response)
