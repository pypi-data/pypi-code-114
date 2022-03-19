from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, fadingGroup=repcap.FadingGroup.Default, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DELay:GROup<ST>:PATH<CH>:STATe \n
		Snippet: driver.source.fsimulator.delay.group.path.state.set(state = False, fadingGroup = repcap.FadingGroup.Default, path = repcap.Path.Default) \n
		Activates the selected path. \n
			:param state: 1| ON| 0| OFF
			:param fadingGroup: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Group')
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
		"""
		param = Conversions.bool_to_str(state)
		fadingGroup_cmd_val = self._cmd_group.get_repcap_cmd_value(fadingGroup, repcap.FadingGroup)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DELay:GROup{fadingGroup_cmd_val}:PATH{path_cmd_val}:STATe {param}')

	def get(self, fadingGroup=repcap.FadingGroup.Default, path=repcap.Path.Default) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:DELay:GROup<ST>:PATH<CH>:STATe \n
		Snippet: value: bool = driver.source.fsimulator.delay.group.path.state.get(fadingGroup = repcap.FadingGroup.Default, path = repcap.Path.Default) \n
		Activates the selected path. \n
			:param fadingGroup: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Group')
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
			:return: state: 1| ON| 0| OFF"""
		fadingGroup_cmd_val = self._cmd_group.get_repcap_cmd_value(fadingGroup, repcap.FadingGroup)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:DELay:GROup{fadingGroup_cmd_val}:PATH{path_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
