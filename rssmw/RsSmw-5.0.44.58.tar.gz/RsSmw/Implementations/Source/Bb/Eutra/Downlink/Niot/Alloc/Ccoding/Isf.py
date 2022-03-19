from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Isf:
	"""Isf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("isf", core, parent)

	def get(self, allocationNull=repcap.AllocationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:ALLoc<CH0>:CCODing:ISF \n
		Snippet: value: int = driver.source.bb.eutra.downlink.niot.alloc.ccoding.isf.get(allocationNull = repcap.AllocationNull.Default) \n
		Queries the resource assignment field (ISF) . \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: ra_ssin_field: integer Range: 0 to 100"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:ALLoc{allocationNull_cmd_val}:CCODing:ISF?')
		return Conversions.str_to_int(response)
