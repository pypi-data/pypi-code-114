from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, chan_cod_state: bool, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:ALLoc<CH0>:CCODing:STATe \n
		Snippet: driver.source.bb.eutra.downlink.niot.alloc.ccoding.state.set(chan_cod_state = False, allocationNull = repcap.AllocationNull.Default) \n
		Enables channel coding. \n
			:param chan_cod_state: 1| ON| 0| OFF
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.bool_to_str(chan_cod_state)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:ALLoc{allocationNull_cmd_val}:CCODing:STATe {param}')

	def get(self, allocationNull=repcap.AllocationNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:ALLoc<CH0>:CCODing:STATe \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.niot.alloc.ccoding.state.get(allocationNull = repcap.AllocationNull.Default) \n
		Enables channel coding. \n
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: chan_cod_state: 1| ON| 0| OFF"""
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:ALLoc{allocationNull_cmd_val}:CCODing:STATe?')
		return Conversions.str_to_bool(response)
