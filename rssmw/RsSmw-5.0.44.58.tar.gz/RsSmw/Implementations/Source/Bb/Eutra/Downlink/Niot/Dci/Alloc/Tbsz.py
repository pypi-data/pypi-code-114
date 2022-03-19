from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tbsz:
	"""Tbsz commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tbsz", core, parent)

	def get(self, allocationNull=repcap.AllocationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:TBSZ \n
		Snippet: value: int = driver.source.bb.eutra.downlink.niot.dci.alloc.tbsz.get(allocationNull = repcap.AllocationNull.Default) \n
		Queries the transport block size. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: transport_blocks: integer Max transport block size depends on the installed options Option: R&S SMW-K115: Max = 680 Option: R&S SMW-K143: Max = 2536 Range: 16 to max"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:TBSZ?')
		return Conversions.str_to_int(response)
