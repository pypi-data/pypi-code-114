from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dselection:
	"""Dselection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dselection", core, parent)

	def set(self, filename: str, terminal=repcap.Terminal.Default, packet=repcap.Packet.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:DCHannel:PACKet<CH>:DATA:DSELection \n
		Snippet: driver.source.bb.evdo.terminal.dchannel.packet.data.dselection.set(filename = '1', terminal = repcap.Terminal.Default, packet = repcap.Packet.Default) \n
		(enabled for an access terminal working in traffic mode) Selects the data list for the data source. \n
			:param filename: string
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:param packet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Packet')
		"""
		param = Conversions.value_to_quoted_str(filename)
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		packet_cmd_val = self._cmd_group.get_repcap_cmd_value(packet, repcap.Packet)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:DCHannel:PACKet{packet_cmd_val}:DATA:DSELection {param}')

	def get(self, terminal=repcap.Terminal.Default, packet=repcap.Packet.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:DCHannel:PACKet<CH>:DATA:DSELection \n
		Snippet: value: str = driver.source.bb.evdo.terminal.dchannel.packet.data.dselection.get(terminal = repcap.Terminal.Default, packet = repcap.Packet.Default) \n
		(enabled for an access terminal working in traffic mode) Selects the data list for the data source. \n
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:param packet: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Packet')
			:return: filename: string"""
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		packet_cmd_val = self._cmd_group.get_repcap_cmd_value(packet, repcap.Packet)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:DCHannel:PACKet{packet_cmd_val}:DATA:DSELection?')
		return trim_str_response(response)
