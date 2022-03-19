from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, count: int, terminal=repcap.Terminal.Default, packet=repcap.Packet.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:DCHannel:PACKet<CH>:SUBPackets:[COUNt] \n
		Snippet: driver.source.bb.evdo.terminal.dchannel.packet.subPackets.count.set(count = 1, terminal = repcap.Terminal.Default, packet = repcap.Packet.Default) \n
		(enabled for physical layer subtype 2 and for an access terminal working in traffic mode) Sets the number of subpackets
		to be sent. \n
			:param count: integer Range: 1 to 4
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:param packet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Packet')
		"""
		param = Conversions.decimal_value_to_str(count)
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		packet_cmd_val = self._cmd_group.get_repcap_cmd_value(packet, repcap.Packet)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:DCHannel:PACKet{packet_cmd_val}:SUBPackets:COUNt {param}')

	def get(self, terminal=repcap.Terminal.Default, packet=repcap.Packet.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:DCHannel:PACKet<CH>:SUBPackets:[COUNt] \n
		Snippet: value: int = driver.source.bb.evdo.terminal.dchannel.packet.subPackets.count.get(terminal = repcap.Terminal.Default, packet = repcap.Packet.Default) \n
		(enabled for physical layer subtype 2 and for an access terminal working in traffic mode) Sets the number of subpackets
		to be sent. \n
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:param packet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Packet')
			:return: count: integer Range: 1 to 4"""
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		packet_cmd_val = self._cmd_group.get_repcap_cmd_value(packet, repcap.Packet)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:DCHannel:PACKet{packet_cmd_val}:SUBPackets:COUNt?')
		return Conversions.str_to_int(response)
