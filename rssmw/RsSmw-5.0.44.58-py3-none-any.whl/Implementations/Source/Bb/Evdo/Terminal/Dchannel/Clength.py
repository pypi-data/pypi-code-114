from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Clength:
	"""Clength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("clength", core, parent)

	def set(self, clength: int, terminal=repcap.Terminal.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:DCHannel:CLENgth \n
		Snippet: driver.source.bb.evdo.terminal.dchannel.clength.set(clength = 1, terminal = repcap.Terminal.Default) \n
		(enabled for access terminal working in access mode) Sets the number of frames (16 slots each) to be transmitted after
		the preamble. Each frame contains one data packet. \n
			:param clength: integer Range: 1 to 15
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
		"""
		param = Conversions.decimal_value_to_str(clength)
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:DCHannel:CLENgth {param}')

	def get(self, terminal=repcap.Terminal.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:DCHannel:CLENgth \n
		Snippet: value: int = driver.source.bb.evdo.terminal.dchannel.clength.get(terminal = repcap.Terminal.Default) \n
		(enabled for access terminal working in access mode) Sets the number of frames (16 slots each) to be transmitted after
		the preamble. Each frame contains one data packet. \n
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:return: clength: integer Range: 1 to 15"""
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:DCHannel:CLENgth?')
		return Conversions.str_to_int(response)
