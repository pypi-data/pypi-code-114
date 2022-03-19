from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lconstant:
	"""Lconstant commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lconstant", core, parent)

	def set(self, lconstant: float, fadingGroup=repcap.FadingGroup.Default, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DEL:GROup<ST>:PATH<CH>:LOGNormal:LCONstant \n
		Snippet: driver.source.fsimulator.delPy.group.path.logNormal.lconstant.set(lconstant = 1.0, fadingGroup = repcap.FadingGroup.Default, path = repcap.Path.Default) \n
		Sets the Local Constant for lognormal fading. \n
			:param lconstant: float Range: 0 to 200, Unit: m
			:param fadingGroup: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Group')
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
		"""
		param = Conversions.decimal_value_to_str(lconstant)
		fadingGroup_cmd_val = self._cmd_group.get_repcap_cmd_value(fadingGroup, repcap.FadingGroup)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DEL:GROup{fadingGroup_cmd_val}:PATH{path_cmd_val}:LOGNormal:LCONstant {param}')

	def get(self, fadingGroup=repcap.FadingGroup.Default, path=repcap.Path.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DEL:GROup<ST>:PATH<CH>:LOGNormal:LCONstant \n
		Snippet: value: float = driver.source.fsimulator.delPy.group.path.logNormal.lconstant.get(fadingGroup = repcap.FadingGroup.Default, path = repcap.Path.Default) \n
		Sets the Local Constant for lognormal fading. \n
			:param fadingGroup: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Group')
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
			:return: lconstant: float Range: 0 to 200, Unit: m"""
		fadingGroup_cmd_val = self._cmd_group.get_repcap_cmd_value(fadingGroup, repcap.FadingGroup)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:DEL:GROup{fadingGroup_cmd_val}:PATH{path_cmd_val}:LOGNormal:LCONstant?')
		return Conversions.str_to_float(response)
