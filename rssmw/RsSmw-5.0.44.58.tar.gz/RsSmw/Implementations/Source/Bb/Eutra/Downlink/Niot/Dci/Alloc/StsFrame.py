from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StsFrame:
	"""StsFrame commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stsFrame", core, parent)

	def set(self, start_sf: int, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:STSFrame \n
		Snippet: driver.source.bb.eutra.downlink.niot.dci.alloc.stsFrame.set(start_sf = 1, allocationNull = repcap.AllocationNull.Default) \n
		Sets the next valid starting subframe for the selected allocation. \n
			:param start_sf: integer Range: 1 to 20
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(start_sf)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:STSFrame {param}')

	def get(self, allocationNull=repcap.AllocationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:DCI:ALLoc<CH0>:STSFrame \n
		Snippet: value: int = driver.source.bb.eutra.downlink.niot.dci.alloc.stsFrame.get(allocationNull = repcap.AllocationNull.Default) \n
		Sets the next valid starting subframe for the selected allocation. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: start_sf: integer Range: 1 to 20"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:DCI:ALLoc{allocationNull_cmd_val}:STSFrame?')
		return Conversions.str_to_int(response)
