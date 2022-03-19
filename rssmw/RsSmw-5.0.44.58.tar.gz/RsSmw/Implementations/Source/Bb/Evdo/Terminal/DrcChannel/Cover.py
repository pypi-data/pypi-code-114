from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cover:
	"""Cover commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cover", core, parent)

	def set(self, cover: int, terminal=repcap.Terminal.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:DRCChannel:COVer \n
		Snippet: driver.source.bb.evdo.terminal.drcChannel.cover.set(cover = 1, terminal = repcap.Terminal.Default) \n
		(enabled for an access terminal working in traffic mode) Selects the Data Rate Control (DRC) Channel Walsh cover. \n
			:param cover: integer Range: 0 to 7
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
		"""
		param = Conversions.decimal_value_to_str(cover)
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:DRCChannel:COVer {param}')

	def get(self, terminal=repcap.Terminal.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:DRCChannel:COVer \n
		Snippet: value: int = driver.source.bb.evdo.terminal.drcChannel.cover.get(terminal = repcap.Terminal.Default) \n
		(enabled for an access terminal working in traffic mode) Selects the Data Rate Control (DRC) Channel Walsh cover. \n
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:return: cover: integer Range: 0 to 7"""
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:DRCChannel:COVer?')
		return Conversions.str_to_int(response)
