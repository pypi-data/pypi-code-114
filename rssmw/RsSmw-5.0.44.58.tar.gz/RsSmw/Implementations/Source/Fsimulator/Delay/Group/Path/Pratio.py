from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pratio:
	"""Pratio commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pratio", core, parent)

	def set(self, pratio: float, fadingGroup=repcap.FadingGroup.Default, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DELay:GROup<ST>:PATH<CH>:PRATio \n
		Snippet: driver.source.fsimulator.delay.group.path.pratio.set(pratio = 1.0, fadingGroup = repcap.FadingGroup.Default, path = repcap.Path.Default) \n
		Sets the power ratio of the discrete and distributed components for Rice fading
		(SOURce:FSIMulator:DELay:GROup:PATH2:PROFile RICE) . \n
			:param pratio: float Range: -30 to 30, Unit: dB
			:param fadingGroup: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Group')
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
		"""
		param = Conversions.decimal_value_to_str(pratio)
		fadingGroup_cmd_val = self._cmd_group.get_repcap_cmd_value(fadingGroup, repcap.FadingGroup)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DELay:GROup{fadingGroup_cmd_val}:PATH{path_cmd_val}:PRATio {param}')

	def get(self, fadingGroup=repcap.FadingGroup.Default, path=repcap.Path.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DELay:GROup<ST>:PATH<CH>:PRATio \n
		Snippet: value: float = driver.source.fsimulator.delay.group.path.pratio.get(fadingGroup = repcap.FadingGroup.Default, path = repcap.Path.Default) \n
		Sets the power ratio of the discrete and distributed components for Rice fading
		(SOURce:FSIMulator:DELay:GROup:PATH2:PROFile RICE) . \n
			:param fadingGroup: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Group')
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
			:return: pratio: float Range: -30 to 30, Unit: dB"""
		fadingGroup_cmd_val = self._cmd_group.get_repcap_cmd_value(fadingGroup, repcap.FadingGroup)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:DELay:GROup{fadingGroup_cmd_val}:PATH{path_cmd_val}:PRATio?')
		return Conversions.str_to_float(response)
