from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rbaf:
	"""Rbaf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbaf", core, parent)

	def get(self, allocationNull=repcap.AllocationNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:RBAF \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.emtc.dci.alloc.rbaf.get(allocationNull = repcap.AllocationNull.Default) \n
		If [:SOURce<hw>]:BB:EUTRa:DL:BWBW20_00 and [:SOURce<hw>]:BB:EUTRa:DL:EMTC:WBCFgBW20 sets the DCI format 6-1A field
		resource block assignment index. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: dci_pusch_rbaf: 1| ON| 0| OFF"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:RBAF?')
		return Conversions.str_to_bool(response)
