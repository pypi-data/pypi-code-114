from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Values:
	"""Values commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("values", core, parent)

	def set(self, values: List[str], terminal=repcap.Terminal.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:ACKChannel:VALues \n
		Snippet: driver.source.bb.evdo.terminal.ackChannel.values.set(values = ['raw1', 'raw2', 'raw3'], terminal = repcap.Terminal.Default) \n
		(enabled for access terminal working in traffic mode) Specifies the data pattern transmitted on the ACK Channel.
		The sequence starts at frame 0 and slot 0 and is repeated with the length of the pattern.A 0 specifies an ACK, a 1
		specifies a NAK. The pattern is only read for slots that are gated on. This parameter is in binary format and has a
		maximal length of 16 bits. \n
			:param values: integer
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
		"""
		param = Conversions.list_to_csv_str(values)
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:ACKChannel:VALues {param}')

	def get(self, terminal=repcap.Terminal.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:ACKChannel:VALues \n
		Snippet: value: List[str] = driver.source.bb.evdo.terminal.ackChannel.values.get(terminal = repcap.Terminal.Default) \n
		(enabled for access terminal working in traffic mode) Specifies the data pattern transmitted on the ACK Channel.
		The sequence starts at frame 0 and slot 0 and is repeated with the length of the pattern.A 0 specifies an ACK, a 1
		specifies a NAK. The pattern is only read for slots that are gated on. This parameter is in binary format and has a
		maximal length of 16 bits. \n
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:return: values: integer"""
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:ACKChannel:VALues?')
		return Conversions.str_to_str_list(response)
