from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Minimum:
	"""Minimum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	def set(self, minimum: enums.EvdoPayload, terminal=repcap.Terminal.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:APCHannel:PAYLoad:MINimum \n
		Snippet: driver.source.bb.evdo.terminal.apChannel.payload.minimum.set(minimum = enums.EvdoPayload.PS1024, terminal = repcap.Terminal.Default) \n
		(enabled for Physical Layer subtype 2 and for an access terminal working in traffic mode) Sets the minimum payload size
		in bits of the data channel that activates the transmission of the auxiliary pilot channel. \n
			:param minimum: PS128| PS256| PS512| PS768| PS1024| PS1536| PS2048| PS3072| PS4096| PS6144| PS8192| PS12288
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
		"""
		param = Conversions.enum_scalar_to_str(minimum, enums.EvdoPayload)
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:APCHannel:PAYLoad:MINimum {param}')

	# noinspection PyTypeChecker
	def get(self, terminal=repcap.Terminal.Default) -> enums.EvdoPayload:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:APCHannel:PAYLoad:MINimum \n
		Snippet: value: enums.EvdoPayload = driver.source.bb.evdo.terminal.apChannel.payload.minimum.get(terminal = repcap.Terminal.Default) \n
		(enabled for Physical Layer subtype 2 and for an access terminal working in traffic mode) Sets the minimum payload size
		in bits of the data channel that activates the transmission of the auxiliary pilot channel. \n
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:return: minimum: PS128| PS256| PS512| PS768| PS1024| PS1536| PS2048| PS3072| PS4096| PS6144| PS8192| PS12288"""
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:APCHannel:PAYLoad:MINimum?')
		return Conversions.str_to_scalar_enum(response, enums.EvdoPayload)
