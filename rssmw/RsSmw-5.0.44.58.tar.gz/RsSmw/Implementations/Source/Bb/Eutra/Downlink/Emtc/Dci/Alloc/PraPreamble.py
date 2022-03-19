from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PraPreamble:
	"""PraPreamble commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("praPreamble", core, parent)

	def set(self, dci_prach_preamble: int, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:PRAPreamble \n
		Snippet: driver.source.bb.eutra.downlink.emtc.dci.alloc.praPreamble.set(dci_prach_preamble = 1, allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI field preamble index. \n
			:param dci_prach_preamble: integer Range: 0 to 63
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(dci_prach_preamble)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:PRAPreamble {param}')

	def get(self, allocationNull=repcap.AllocationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:PRAPreamble \n
		Snippet: value: int = driver.source.bb.eutra.downlink.emtc.dci.alloc.praPreamble.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI field preamble index. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: dci_prach_preamble: integer Range: 0 to 63"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:PRAPreamble?')
		return Conversions.str_to_int(response)
