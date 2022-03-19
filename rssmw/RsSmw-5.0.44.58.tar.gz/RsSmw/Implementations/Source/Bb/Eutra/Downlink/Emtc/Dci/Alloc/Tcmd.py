from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tcmd:
	"""Tcmd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tcmd", core, parent)

	def set(self, tpc_cmd_3: List[str], allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:TCMD \n
		Snippet: driver.source.bb.eutra.downlink.emtc.dci.alloc.tcmd.set(tpc_cmd_3 = ['raw1', 'raw2', 'raw3'], allocationNull = repcap.AllocationNull.Default) \n
		Sets the TCP command field of the DCI format 3/3A. \n
			:param tpc_cmd_3: 64 bits
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.list_to_csv_str(tpc_cmd_3)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:TCMD {param}')

	def get(self, allocationNull=repcap.AllocationNull.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:EMTC:DCI:ALLoc<CH0>:TCMD \n
		Snippet: value: List[str] = driver.source.bb.eutra.downlink.emtc.dci.alloc.tcmd.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the TCP command field of the DCI format 3/3A. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: tpc_cmd_3: 64 bits"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:EMTC:DCI:ALLoc{allocationNull_cmd_val}:TCMD?')
		return Conversions.str_to_str_list(response)
