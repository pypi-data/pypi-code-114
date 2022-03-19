from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PraMask:
	"""PraMask commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("praMask", core, parent)

	def set(self, dci_prach_mask_idx: int, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:PRAMask \n
		Snippet: driver.source.bb.eutra.downlink.emtc.dci.alloc.praMask.set(dci_prach_mask_idx = 1, allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI field PRACH mask index. \n
			:param dci_prach_mask_idx: integer Range: 0 to 15
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(dci_prach_mask_idx)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:PRAMask {param}')

	def get(self, allocationNull=repcap.AllocationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:PRAMask \n
		Snippet: value: int = driver.source.bb.eutra.downlink.emtc.dci.alloc.praMask.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI field PRACH mask index. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: dci_prach_mask_idx: integer Range: 0 to 15"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:PRAMask?')
		return Conversions.str_to_int(response)
