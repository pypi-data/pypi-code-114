from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, offset: int, terminal=repcap.Terminal.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:ACYCle:OFFSet \n
		Snippet: driver.source.bb.evdo.terminal.acycle.offset.set(offset = 1, terminal = repcap.Terminal.Default) \n
		(enabled for access terminal working in access mode) The Access Channel transmission starts with this number of slots
		relative to the beginning of each access cycle duration. \n
			:param offset: integer Range: 0 to 12
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
		"""
		param = Conversions.decimal_value_to_str(offset)
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:ACYCle:OFFSet {param}')

	def get(self, terminal=repcap.Terminal.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:ACYCle:OFFSet \n
		Snippet: value: int = driver.source.bb.evdo.terminal.acycle.offset.get(terminal = repcap.Terminal.Default) \n
		(enabled for access terminal working in access mode) The Access Channel transmission starts with this number of slots
		relative to the beginning of each access cycle duration. \n
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:return: offset: integer Range: 0 to 12"""
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:ACYCle:OFFSet?')
		return Conversions.str_to_int(response)
