from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, count: int, terminal=repcap.Terminal.Default, packet=repcap.Packet.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:DCHannel:PACKet<CH>:COUNt \n
		Snippet: driver.source.bb.evdo.terminal.dchannel.packet.count.set(count = 1, terminal = repcap.Terminal.Default, packet = repcap.Packet.Default) \n
		(enabled for an access terminal working in traffic mode) Sets the number of packets to be sent. The number of packets to
		be send depends on whether the parameter 'Infinite Packets' is enabled or disabled. If 'Infinite Packets'is enabled,
		there is no limit to the number of packets sent. If 'Infinite Packets' is disabled, the number of packets can be
		specified. In this case, the data channel will be switched off after the specified number of packets have been sent.
		Note: Configuration of Packet 2 and Packet 3 transmitted on the second and the third subframe, is only enabled for
		physical layer subtype 2. \n
			:param count: integer Range: 0 to 65536
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:param packet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Packet')
		"""
		param = Conversions.decimal_value_to_str(count)
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		packet_cmd_val = self._cmd_group.get_repcap_cmd_value(packet, repcap.Packet)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:DCHannel:PACKet{packet_cmd_val}:COUNt {param}')

	def get(self, terminal=repcap.Terminal.Default, packet=repcap.Packet.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:DCHannel:PACKet<CH>:COUNt \n
		Snippet: value: int = driver.source.bb.evdo.terminal.dchannel.packet.count.get(terminal = repcap.Terminal.Default, packet = repcap.Packet.Default) \n
		(enabled for an access terminal working in traffic mode) Sets the number of packets to be sent. The number of packets to
		be send depends on whether the parameter 'Infinite Packets' is enabled or disabled. If 'Infinite Packets'is enabled,
		there is no limit to the number of packets sent. If 'Infinite Packets' is disabled, the number of packets can be
		specified. In this case, the data channel will be switched off after the specified number of packets have been sent.
		Note: Configuration of Packet 2 and Packet 3 transmitted on the second and the third subframe, is only enabled for
		physical layer subtype 2. \n
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:param packet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Packet')
			:return: count: integer Range: 0 to 65536"""
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		packet_cmd_val = self._cmd_group.get_repcap_cmd_value(packet, repcap.Packet)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:DCHannel:PACKet{packet_cmd_val}:COUNt?')
		return Conversions.str_to_int(response)
