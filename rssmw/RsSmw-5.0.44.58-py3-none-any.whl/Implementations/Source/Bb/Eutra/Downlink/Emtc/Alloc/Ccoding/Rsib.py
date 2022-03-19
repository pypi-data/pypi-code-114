from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rsib:
	"""Rsib commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rsib", core, parent)

	def get(self, allocationNull=repcap.AllocationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:ALLoc<CH0>:CCODing:RSIB \n
		Snippet: value: int = driver.source.bb.eutra.downlink.emtc.alloc.ccoding.rsib.get(allocationNull = repcap.AllocationNull.Default) \n
		Queries the number of PDSCH repetitions NRepPDSCH, as defined with the command
		[:SOURce<hw>]:BB:EUTRa:DL:EMTC:ALLoc<ch0>:CCODing:SIB. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: pdsch_rep_sib_1: integer Range: 0 to 11"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:ALLoc{allocationNull_cmd_val}:CCODing:RSIB?')
		return Conversions.str_to_int(response)
