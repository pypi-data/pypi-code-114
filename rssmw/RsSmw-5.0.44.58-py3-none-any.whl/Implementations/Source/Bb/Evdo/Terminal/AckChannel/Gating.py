from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gating:
	"""Gating commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gating", core, parent)

	def set(self, gating: List[str], terminal=repcap.Terminal.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:ACKChannel:GATing \n
		Snippet: driver.source.bb.evdo.terminal.ackChannel.gating.set(gating = ['raw1', 'raw2', 'raw3'], terminal = repcap.Terminal.Default) \n
		(enabled for access terminal working in traffic mode) Sets the active and inactive slots of the ACK channel.
		This parameter is in binary format and has a maximal length of 16 bits. The sequence starts at frame 0 and slot 0 and is
		repeated with the length of the pattern. A 0 gates the ACK channel off for the corresponding slot, a 1 activates the
		channel. \n
			:param gating: integer
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
		"""
		param = Conversions.list_to_csv_str(gating)
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:ACKChannel:GATing {param}')

	def get(self, terminal=repcap.Terminal.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:ACKChannel:GATing \n
		Snippet: value: List[str] = driver.source.bb.evdo.terminal.ackChannel.gating.get(terminal = repcap.Terminal.Default) \n
		(enabled for access terminal working in traffic mode) Sets the active and inactive slots of the ACK channel.
		This parameter is in binary format and has a maximal length of 16 bits. The sequence starts at frame 0 and slot 0 and is
		repeated with the length of the pattern. A 0 gates the ACK channel off for the corresponding slot, a 1 activates the
		channel. \n
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:return: gating: integer"""
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:ACKChannel:GATing?')
		return Conversions.str_to_str_list(response)
