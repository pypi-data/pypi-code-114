from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	def set(self, length: enums.EvdoDrcLenUp, terminal=repcap.Terminal.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:DRCChannel:LENGth \n
		Snippet: driver.source.bb.evdo.terminal.drcChannel.length.set(length = enums.EvdoDrcLenUp.DL1, terminal = repcap.Terminal.Default) \n
		(enabled for an access terminal working in traffic mode) Specifies the transmission duration of the Data Rate Control
		(DRC) channel in slots. \n
			:param length: DL1| DL2| DL4| DL8
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
		"""
		param = Conversions.enum_scalar_to_str(length, enums.EvdoDrcLenUp)
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:DRCChannel:LENGth {param}')

	# noinspection PyTypeChecker
	def get(self, terminal=repcap.Terminal.Default) -> enums.EvdoDrcLenUp:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:DRCChannel:LENGth \n
		Snippet: value: enums.EvdoDrcLenUp = driver.source.bb.evdo.terminal.drcChannel.length.get(terminal = repcap.Terminal.Default) \n
		(enabled for an access terminal working in traffic mode) Specifies the transmission duration of the Data Rate Control
		(DRC) channel in slots. \n
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:return: length: DL1| DL2| DL4| DL8"""
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:DRCChannel:LENGth?')
		return Conversions.str_to_scalar_enum(response, enums.EvdoDrcLenUp)
