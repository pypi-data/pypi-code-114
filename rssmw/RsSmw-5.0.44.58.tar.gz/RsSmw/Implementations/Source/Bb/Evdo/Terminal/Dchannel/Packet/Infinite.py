from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Infinite:
	"""Infinite commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("infinite", core, parent)

	def set(self, infinite: bool, terminal=repcap.Terminal.Default, packet=repcap.Packet.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:DCHannel:PACKet<CH>:INFinite \n
		Snippet: driver.source.bb.evdo.terminal.dchannel.packet.infinite.set(infinite = False, terminal = repcap.Terminal.Default, packet = repcap.Packet.Default) \n
		(enabled for an access terminal working in traffic mode) Enables or disables sending an unlimited number of packets. The
		parameter 'Number of Packets to be Send' depends on whether the parameter 'Infinite Packets' is enabled or disabled.
		If 'Infinite Packets' is enabled, there is no limit to the number of packets sent. If 'Infinite Packets' is disabled, the
		number of packets can be specified. Note: Configuration of Packet 2 and Packet 3 transmitted on the second and the third
		subframe, is only enabled for physical layer subtype 2. \n
			:param infinite: 1| ON| 0| OFF
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:param packet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Packet')
		"""
		param = Conversions.bool_to_str(infinite)
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		packet_cmd_val = self._cmd_group.get_repcap_cmd_value(packet, repcap.Packet)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:DCHannel:PACKet{packet_cmd_val}:INFinite {param}')

	def get(self, terminal=repcap.Terminal.Default, packet=repcap.Packet.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:DCHannel:PACKet<CH>:INFinite \n
		Snippet: value: bool = driver.source.bb.evdo.terminal.dchannel.packet.infinite.get(terminal = repcap.Terminal.Default, packet = repcap.Packet.Default) \n
		(enabled for an access terminal working in traffic mode) Enables or disables sending an unlimited number of packets. The
		parameter 'Number of Packets to be Send' depends on whether the parameter 'Infinite Packets' is enabled or disabled.
		If 'Infinite Packets' is enabled, there is no limit to the number of packets sent. If 'Infinite Packets' is disabled, the
		number of packets can be specified. Note: Configuration of Packet 2 and Packet 3 transmitted on the second and the third
		subframe, is only enabled for physical layer subtype 2. \n
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:param packet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Packet')
			:return: infinite: 1| ON| 0| OFF"""
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		packet_cmd_val = self._cmd_group.get_repcap_cmd_value(packet, repcap.Packet)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:DCHannel:PACKet{packet_cmd_val}:INFinite?')
		return Conversions.str_to_bool(response)
