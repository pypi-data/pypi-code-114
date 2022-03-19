from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gain:
	"""Gain commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gain", core, parent)

	def set(self, gain: float, terminal=repcap.Terminal.Default, packet=repcap.Packet.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:DCHannel:PACKet<CH>:GAIN \n
		Snippet: driver.source.bb.evdo.terminal.dchannel.packet.gain.set(gain = 1.0, terminal = repcap.Terminal.Default, packet = repcap.Packet.Default) \n
		(enabled for an access terminal working in traffic mode) Sets the gain in dB of the Data Channel relative to the pilot
		channel power. Note: Configuration of Packet 2 and Packet 3 transmitted on the second and the third subframe, is only
		enabled for physical layer subtype 2. \n
			:param gain: float Range: -80 to 30
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:param packet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Packet')
		"""
		param = Conversions.decimal_value_to_str(gain)
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		packet_cmd_val = self._cmd_group.get_repcap_cmd_value(packet, repcap.Packet)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:DCHannel:PACKet{packet_cmd_val}:GAIN {param}')

	def get(self, terminal=repcap.Terminal.Default, packet=repcap.Packet.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:DCHannel:PACKet<CH>:GAIN \n
		Snippet: value: float = driver.source.bb.evdo.terminal.dchannel.packet.gain.get(terminal = repcap.Terminal.Default, packet = repcap.Packet.Default) \n
		(enabled for an access terminal working in traffic mode) Sets the gain in dB of the Data Channel relative to the pilot
		channel power. Note: Configuration of Packet 2 and Packet 3 transmitted on the second and the third subframe, is only
		enabled for physical layer subtype 2. \n
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:param packet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Packet')
			:return: gain: float Range: -80 to 30"""
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		packet_cmd_val = self._cmd_group.get_repcap_cmd_value(packet, repcap.Packet)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:DCHannel:PACKet{packet_cmd_val}:GAIN?')
		return Conversions.str_to_float(response)
