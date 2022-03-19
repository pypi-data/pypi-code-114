from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UlIndex:
	"""UlIndex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ulIndex", core, parent)

	def set(self, dci_ul_index: int, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:ULINdex \n
		Snippet: driver.source.bb.eutra.downlink.emtc.dci.alloc.ulIndex.set(dci_ul_index = 1, allocationNull = repcap.AllocationNull.Default) \n
		In TDD mode and if UL/DL Configuration 0 is used, sets the DCI field UL index. \n
			:param dci_ul_index: integer Range: 0 to 3
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(dci_ul_index)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:ULINdex {param}')

	def get(self, allocationNull=repcap.AllocationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:ULINdex \n
		Snippet: value: int = driver.source.bb.eutra.downlink.emtc.dci.alloc.ulIndex.get(allocationNull = repcap.AllocationNull.Default) \n
		In TDD mode and if UL/DL Configuration 0 is used, sets the DCI field UL index. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: dci_ul_index: integer Range: 0 to 3"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:ULINdex?')
		return Conversions.str_to_int(response)
