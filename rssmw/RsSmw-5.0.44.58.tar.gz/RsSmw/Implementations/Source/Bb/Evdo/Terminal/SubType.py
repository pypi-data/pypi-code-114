from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SubType:
	"""SubType commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("subType", core, parent)

	def set(self, sub_type: enums.SubType, terminal=repcap.Terminal.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:SUBType \n
		Snippet: driver.source.bb.evdo.terminal.subType.set(sub_type = enums.SubType.S1, terminal = repcap.Terminal.Default) \n
		Selects the physical layer subtype for the selected access terminal. \n
			:param sub_type: S1| S2
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
		"""
		param = Conversions.enum_scalar_to_str(sub_type, enums.SubType)
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:SUBType {param}')

	# noinspection PyTypeChecker
	def get(self, terminal=repcap.Terminal.Default) -> enums.SubType:
		"""SCPI: [SOURce<HW>]:BB:EVDO:TERMinal<ST>:SUBType \n
		Snippet: value: enums.SubType = driver.source.bb.evdo.terminal.subType.get(terminal = repcap.Terminal.Default) \n
		Selects the physical layer subtype for the selected access terminal. \n
			:param terminal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Terminal')
			:return: sub_type: S1| S2"""
		terminal_cmd_val = self._cmd_group.get_repcap_cmd_value(terminal, repcap.Terminal)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:TERMinal{terminal_cmd_val}:SUBType?')
		return Conversions.str_to_scalar_enum(response, enums.SubType)
