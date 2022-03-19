from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	# noinspection PyTypeChecker
	def get(self, terminal=repcap.Terminal.Default, packet=repcap.Packet.Default) -> enums.EvdoModulation:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:DCHannel:PACKet<CH>:MODulation \n
		Snippet: value: enums.EvdoModulation = driver.source.bb.evdo.terminal.dchannel.packet.modulation.get(terminal = repcap.Terminal.Default, packet = repcap.Packet.Default) \n
		(enabled for physical layer subtype 2 and for an access terminal working in traffic mode) Displays the modulation type
		per packet. \n
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:param packet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Packet')
			:return: modulation: B4| Q4| Q2| Q4Q2| E4E2 B4 The modulation type is set to BPSK modulation with 4-ary Walsh cover. Q4 The modulation type is set to QPSK modulation with 4-ary Walsh cover. Q2 The modulation type is set to QPSK modulation with 2-ary Walsh cover. Q4Q2 Sum of Q4 and Q2 modulated symbols. E4E2 Sum of E4 (8-PSK modulated with 4-ary Walsh cover) and E2 (8-PSK modulated with 2-ary Walsh cover) modulated symbols."""
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		packet_cmd_val = self._cmd_group.get_repcap_cmd_value(packet, repcap.Packet)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:DCHannel:PACKet{packet_cmd_val}:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.EvdoModulation)
