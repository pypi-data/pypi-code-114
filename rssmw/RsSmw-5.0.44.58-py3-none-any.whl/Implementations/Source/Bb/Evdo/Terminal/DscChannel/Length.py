from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, length: int, terminal=repcap.Terminal.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:DSCChannel:LENGth \n
		Snippet: driver.source.bb.evdo.terminal.dscChannel.length.set(length = 1, terminal = repcap.Terminal.Default) \n
		(enabled for Physical Layer subtype 2 and for an access terminal working in traffic mode) Specifies the transmission
		duration of the Data Source Control (DSC) channel in slots. \n
			:param length: integer Range: 8 to 256
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
		"""
		param = Conversions.decimal_value_to_str(length)
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:DSCChannel:LENGth {param}')

	def get(self, terminal=repcap.Terminal.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:DSCChannel:LENGth \n
		Snippet: value: int = driver.source.bb.evdo.terminal.dscChannel.length.get(terminal = repcap.Terminal.Default) \n
		(enabled for Physical Layer subtype 2 and for an access terminal working in traffic mode) Specifies the transmission
		duration of the Data Source Control (DSC) channel in slots. \n
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:return: length: integer Range: 8 to 256"""
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:DSCChannel:LENGth?')
		return Conversions.str_to_int(response)
