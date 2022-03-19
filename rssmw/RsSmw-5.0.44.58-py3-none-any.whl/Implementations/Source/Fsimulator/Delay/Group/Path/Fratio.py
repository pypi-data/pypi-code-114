from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fratio:
	"""Fratio commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fratio", core, parent)

	def set(self, fratio: float, fadingGroup=repcap.FadingGroup.Default, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DELay:GROup<ST>:PATH<CH>:FRATio \n
		Snippet: driver.source.fsimulator.delay.group.path.fratio.set(fratio = 1.0, fadingGroup = repcap.FadingGroup.Default, path = repcap.Path.Default) \n
		For Rice, pure Doppler and Gauss Doppler fading, sets the ratio of the actual Doppler frequency to the set Doppler
		frequency. The Frequency Ratio serves as a measure of the angle of incidence between the transmitter and receiver. \n
			:param fratio: float Range: -1 to 1
			:param fadingGroup: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Group')
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
		"""
		param = Conversions.decimal_value_to_str(fratio)
		fadingGroup_cmd_val = self._cmd_group.get_repcap_cmd_value(fadingGroup, repcap.FadingGroup)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DELay:GROup{fadingGroup_cmd_val}:PATH{path_cmd_val}:FRATio {param}')

	def get(self, fadingGroup=repcap.FadingGroup.Default, path=repcap.Path.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DELay:GROup<ST>:PATH<CH>:FRATio \n
		Snippet: value: float = driver.source.fsimulator.delay.group.path.fratio.get(fadingGroup = repcap.FadingGroup.Default, path = repcap.Path.Default) \n
		For Rice, pure Doppler and Gauss Doppler fading, sets the ratio of the actual Doppler frequency to the set Doppler
		frequency. The Frequency Ratio serves as a measure of the angle of incidence between the transmitter and receiver. \n
			:param fadingGroup: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Group')
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Path')
			:return: fratio: float Range: -1 to 1"""
		fadingGroup_cmd_val = self._cmd_group.get_repcap_cmd_value(fadingGroup, repcap.FadingGroup)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:DELay:GROup{fadingGroup_cmd_val}:PATH{path_cmd_val}:FRATio?')
		return Conversions.str_to_float(response)
