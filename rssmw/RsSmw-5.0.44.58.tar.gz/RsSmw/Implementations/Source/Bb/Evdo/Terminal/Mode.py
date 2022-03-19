from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.EvdoTermMode, terminal=repcap.Terminal.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:MODE \n
		Snippet: driver.source.bb.evdo.terminal.mode.set(mode = enums.EvdoTermMode.ACCess, terminal = repcap.Terminal.Default) \n
		Sets the mode (Traffic or Access) of the selected access terminal. \n
			:param mode: ACCess| TRAFfic
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.EvdoTermMode)
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, terminal=repcap.Terminal.Default) -> enums.EvdoTermMode:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:MODE \n
		Snippet: value: enums.EvdoTermMode = driver.source.bb.evdo.terminal.mode.get(terminal = repcap.Terminal.Default) \n
		Sets the mode (Traffic or Access) of the selected access terminal. \n
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:return: mode: ACCess| TRAFfic"""
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.EvdoTermMode)
