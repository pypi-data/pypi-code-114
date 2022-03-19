from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hack:
	"""Hack commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hack", core, parent)

	def set(self, hack_resource: int, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:HACK \n
		Snippet: driver.source.bb.eutra.downlink.niot.dci.alloc.hack.set(hack_resource = 1, allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI field HARQ-ACK resource field. \n
			:param hack_resource: integer Range: 0 to 15
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(hack_resource)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:HACK {param}')

	def get(self, allocationNull=repcap.AllocationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:HACK \n
		Snippet: value: int = driver.source.bb.eutra.downlink.niot.dci.alloc.hack.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the DCI field HARQ-ACK resource field. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: hack_resource: integer Range: 0 to 15"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:HACK?')
		return Conversions.str_to_int(response)
