from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Actual:
	"""Actual commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("actual", core, parent)

	def get(self, fadingGroup=repcap.FadingGroup.Default, path=repcap.Path.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DEL:GROup<ST>:PATH<CH>:FDOPpler:ACTual \n
		Snippet: value: float = driver.source.fsimulator.delPy.group.path.fdoppler.actual.get(fadingGroup = repcap.FadingGroup.Default, path = repcap.Path.Default) \n
		Queries the actual Doppler shift. For the Pure Doppler and Rice Fading profiles, the actual Doppler shift is a function
		of the selected ratio of the Doppler shift to the Doppler frequency
		([:SOURce<hw>]:FSIMulator:DELay|DEL:GROup<st>:PATH<ch>:FRATio) . \n
			:param fadingGroup: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Group')
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
			:return: act_doppler: float Range: -4000.0 to 4000"""
		fadingGroup_cmd_val = self._cmd_group.get_repcap_cmd_value(fadingGroup, repcap.FadingGroup)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:DEL:GROup{fadingGroup_cmd_val}:PATH{path_cmd_val}:FDOPpler:ACTual?')
		return Conversions.str_to_float(response)
