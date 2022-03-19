from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scind:
	"""Scind commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scind", core, parent)

	def set(self, subcarrier_ind: int, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:SCINd \n
		Snippet: driver.source.bb.eutra.downlink.niot.dci.alloc.scind.set(subcarrier_ind = 1, allocationNull = repcap.AllocationNull.Default) \n
		Sets teh DCI field subcarrier identification field of NPUSCH (ISC) . \n
			:param subcarrier_ind: integer Range: 0 to 47
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(subcarrier_ind)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:SCINd {param}')

	def get(self, allocationNull=repcap.AllocationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:SCINd \n
		Snippet: value: int = driver.source.bb.eutra.downlink.niot.dci.alloc.scind.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets teh DCI field subcarrier identification field of NPUSCH (ISC) . \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: subcarrier_ind: integer Range: 0 to 47"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:SCINd?')
		return Conversions.str_to_int(response)
