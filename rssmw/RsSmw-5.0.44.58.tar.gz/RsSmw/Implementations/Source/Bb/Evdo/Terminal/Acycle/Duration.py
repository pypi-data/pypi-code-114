from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Duration:
	"""Duration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("duration", core, parent)

	def set(self, duration: int, terminal=repcap.Terminal.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:ACYCle:DURation \n
		Snippet: driver.source.bb.evdo.terminal.acycle.duration.set(duration = 1, terminal = repcap.Terminal.Default) \n
		(enabled for access terminal working in access mode) Sets the access cycle duration in slots. Access probes are repeated
		with a period of access cycle duration slots. \n
			:param duration: integer Range: 1 to 255
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
		"""
		param = Conversions.decimal_value_to_str(duration)
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:ACYCle:DURation {param}')

	def get(self, terminal=repcap.Terminal.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:ACYCle:DURation \n
		Snippet: value: int = driver.source.bb.evdo.terminal.acycle.duration.get(terminal = repcap.Terminal.Default) \n
		(enabled for access terminal working in access mode) Sets the access cycle duration in slots. Access probes are repeated
		with a period of access cycle duration slots. \n
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:return: duration: integer Range: 1 to 255"""
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:ACYCle:DURation?')
		return Conversions.str_to_int(response)
