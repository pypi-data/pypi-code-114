from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.EvdoAckMode, terminal=repcap.Terminal.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:ACKChannel:MODE \n
		Snippet: driver.source.bb.evdo.terminal.ackChannel.mode.set(mode = enums.EvdoAckMode.BPSK, terminal = repcap.Terminal.Default) \n
		(enabled for access terminal working in traffic mode) Specifies the modulation mode of the ACK channel.
		With BPSK modulation, a 0 (ACK) is mapped to +1 and a 1 (NAK) to -1.With OOK modulation, a 0 (ACK) is mapped to ON and a
		1 (NAK) to OFF. \n
			:param mode: BPSK| OOK BPSK Sets the modulation to BPSK (Binary Phase Shift Keying) . OOK Sets the modulation to OOK (On-Off Keying) . Note: This value is only enabled for physical layer subtype 2.
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.EvdoAckMode)
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:ACKChannel:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, terminal=repcap.Terminal.Default) -> enums.EvdoAckMode:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:ACKChannel:MODE \n
		Snippet: value: enums.EvdoAckMode = driver.source.bb.evdo.terminal.ackChannel.mode.get(terminal = repcap.Terminal.Default) \n
		(enabled for access terminal working in traffic mode) Specifies the modulation mode of the ACK channel.
		With BPSK modulation, a 0 (ACK) is mapped to +1 and a 1 (NAK) to -1.With OOK modulation, a 0 (ACK) is mapped to ON and a
		1 (NAK) to OFF. \n
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:return: mode: BPSK| OOK BPSK Sets the modulation to BPSK (Binary Phase Shift Keying) . OOK Sets the modulation to OOK (On-Off Keying) . Note: This value is only enabled for physical layer subtype 2."""
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:ACKChannel:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.EvdoAckMode)
