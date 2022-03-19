from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coefficient:
	"""Coefficient commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coefficient", core, parent)

	def set(self, coefficient: float, fadingGroup=repcap.FadingGroup.Default, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DELay:GROup<ST>:PATH<CH>:CORRelation:COEFficient \n
		Snippet: driver.source.fsimulator.delay.group.path.correlation.coefficient.set(coefficient = 1.0, fadingGroup = repcap.FadingGroup.Default, path = repcap.Path.Default) \n
		Determines the magnitude of the complex correlation coefficient. The higher the entered percentage, the greater the
		correlation of the statistical fading processes for the two paths. Highly correlated ambient conditions for the signal
		are simulated in this manner. Sets the correlation coefficient of the correlated path of the second fader also to the
		entered value. \n
			:param coefficient: float Range: 0 to 100, Unit: PCT
			:param fadingGroup: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Group')
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
		"""
		param = Conversions.decimal_value_to_str(coefficient)
		fadingGroup_cmd_val = self._cmd_group.get_repcap_cmd_value(fadingGroup, repcap.FadingGroup)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DELay:GROup{fadingGroup_cmd_val}:PATH{path_cmd_val}:CORRelation:COEFficient {param}')

	def get(self, fadingGroup=repcap.FadingGroup.Default, path=repcap.Path.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DELay:GROup<ST>:PATH<CH>:CORRelation:COEFficient \n
		Snippet: value: float = driver.source.fsimulator.delay.group.path.correlation.coefficient.get(fadingGroup = repcap.FadingGroup.Default, path = repcap.Path.Default) \n
		Determines the magnitude of the complex correlation coefficient. The higher the entered percentage, the greater the
		correlation of the statistical fading processes for the two paths. Highly correlated ambient conditions for the signal
		are simulated in this manner. Sets the correlation coefficient of the correlated path of the second fader also to the
		entered value. \n
			:param fadingGroup: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Group')
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
			:return: coefficient: float Range: 0 to 100, Unit: PCT"""
		fadingGroup_cmd_val = self._cmd_group.get_repcap_cmd_value(fadingGroup, repcap.FadingGroup)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:DELay:GROup{fadingGroup_cmd_val}:PATH{path_cmd_val}:CORRelation:COEFficient?')
		return Conversions.str_to_float(response)
