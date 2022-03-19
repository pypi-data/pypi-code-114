from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Harq:
	"""Harq commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("harq", core, parent)

	def set(self, dci_harq_proc_num: int, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:HARQ \n
		Snippet: driver.source.bb.eutra.downlink.emtc.dci.alloc.harq.set(dci_harq_proc_num = 1, allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI field HARQ process number. \n
			:param dci_harq_proc_num: integer In FDD mode: 0 to 7 In TDD mode: 0 to 15 Range: 0 to 15
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(dci_harq_proc_num)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:HARQ {param}')

	def get(self, allocationNull=repcap.AllocationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:HARQ \n
		Snippet: value: int = driver.source.bb.eutra.downlink.emtc.dci.alloc.harq.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI field HARQ process number. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: dci_harq_proc_num: integer In FDD mode: 0 to 7 In TDD mode: 0 to 15 Range: 0 to 15"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:HARQ?')
		return Conversions.str_to_int(response)
