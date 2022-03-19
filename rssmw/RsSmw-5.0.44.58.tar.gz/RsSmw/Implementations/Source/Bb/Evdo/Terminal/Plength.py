from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Plength:
	"""Plength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plength", core, parent)

	def set(self, plength: int, terminal=repcap.Terminal.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:PLENgth \n
		Snippet: driver.source.bb.evdo.terminal.plength.set(plength = 1, terminal = repcap.Terminal.Default) \n
		(enabled for access terminal working in access mode) Specifies the length of the preamble in frames (16 slots each) of
		the access probe. \n
			:param plength: integer Range: 1 to 7
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
		"""
		param = Conversions.decimal_value_to_str(plength)
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:PLENgth {param}')

	def get(self, terminal=repcap.Terminal.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:PLENgth \n
		Snippet: value: int = driver.source.bb.evdo.terminal.plength.get(terminal = repcap.Terminal.Default) \n
		(enabled for access terminal working in access mode) Specifies the length of the preamble in frames (16 slots each) of
		the access probe. \n
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:return: plength: integer Range: 1 to 7"""
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:PLENgth?')
		return Conversions.str_to_int(response)
