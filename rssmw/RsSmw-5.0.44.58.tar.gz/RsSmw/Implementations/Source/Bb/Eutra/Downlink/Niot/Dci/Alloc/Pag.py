from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pag:
	"""Pag commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pag", core, parent)

	def set(self, paging: bool, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:PAG \n
		Snippet: driver.source.bb.eutra.downlink.niot.dci.alloc.pag.set(paging = False, allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI field flag for paging/direct indication. \n
			:param paging: 1| ON| 0| OFF 1 Paging 0 Direct indication
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.bool_to_str(paging)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:PAG {param}')

	def get(self, allocationNull=repcap.AllocationNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:PAG \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.niot.dci.alloc.pag.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI field flag for paging/direct indication. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: paging: 1| ON| 0| OFF 1 Paging 0 Direct indication"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:PAG?')
		return Conversions.str_to_bool(response)
