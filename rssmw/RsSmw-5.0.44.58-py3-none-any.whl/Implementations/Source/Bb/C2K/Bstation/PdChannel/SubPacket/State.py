from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, baseStation=repcap.BaseStation.Default, subpacket=repcap.Subpacket.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:PDCHannel:SUBPacket<DI>:STATe \n
		Snippet: driver.source.bb.c2K.bstation.pdChannel.subPacket.state.set(state = False, baseStation = repcap.BaseStation.Default, subpacket = repcap.Subpacket.Default) \n
		This command activates/deactivates the selected sub packet for F_PDCH. Sub packet 1 is always active. \n
			:param state: 1| ON| 0| OFF
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param subpacket: optional repeated capability selector. Default value: Nr1 (settable in the interface 'SubPacket')
		"""
		param = Conversions.bool_to_str(state)
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		subpacket_cmd_val = self._cmd_group.get_repcap_cmd_value(subpacket, repcap.Subpacket)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:PDCHannel:SUBPacket{subpacket_cmd_val}:STATe {param}')

	def get(self, baseStation=repcap.BaseStation.Default, subpacket=repcap.Subpacket.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:C2K:BSTation<ST>:PDCHannel:SUBPacket<DI>:STATe \n
		Snippet: value: bool = driver.source.bb.c2K.bstation.pdChannel.subPacket.state.get(baseStation = repcap.BaseStation.Default, subpacket = repcap.Subpacket.Default) \n
		This command activates/deactivates the selected sub packet for F_PDCH. Sub packet 1 is always active. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:param subpacket: optional repeated capability selector. Default value: Nr1 (settable in the interface 'SubPacket')
			:return: state: 1| ON| 0| OFF"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		subpacket_cmd_val = self._cmd_group.get_repcap_cmd_value(subpacket, repcap.Subpacket)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:BSTation{baseStation_cmd_val}:PDCHannel:SUBPacket{subpacket_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
