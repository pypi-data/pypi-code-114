from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:CDYNamic:PATH<CH>:STATe \n
		Snippet: driver.source.fsimulator.cdynamic.path.state.set(state = False, path = repcap.Path.Default) \n
		Activates the selected path, if a customized dynamic file is selected. \n
			:param state: 1| ON| 0| OFF
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
		"""
		param = Conversions.bool_to_str(state)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:CDYNamic:PATH{path_cmd_val}:STATe {param}')

	def get(self, path=repcap.Path.Default) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:CDYNamic:PATH<CH>:STATe \n
		Snippet: value: bool = driver.source.fsimulator.cdynamic.path.state.get(path = repcap.Path.Default) \n
		Activates the selected path, if a customized dynamic file is selected. \n
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
			:return: state: 1| ON| 0| OFF"""
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:CDYNamic:PATH{path_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
