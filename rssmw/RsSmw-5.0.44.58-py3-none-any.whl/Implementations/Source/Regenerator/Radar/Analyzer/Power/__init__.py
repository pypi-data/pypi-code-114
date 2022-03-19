from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def apply(self):
		"""apply commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apply'):
			from .Apply import Apply
			self._apply = Apply(self._core, self._cmd_group)
		return self._apply

	def get_attenuator(self) -> float:
		"""SCPI: [SOURce<HW>]:REGenerator:RADar:ANALyzer:POWer:ATTenuator \n
		Snippet: value: float = driver.source.regenerator.radar.analyzer.power.get_attenuator() \n
		Sets the attenuation of the external attenuator. The command can be used only if a R&S FSW is connected to the R&S SMW. \n
			:return: power_attenuator: float Range: -600 to 500
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:RADar:ANALyzer:POWer:ATTenuator?')
		return Conversions.str_to_float(response)

	def set_attenuator(self, power_attenuator: float) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:RADar:ANALyzer:POWer:ATTenuator \n
		Snippet: driver.source.regenerator.radar.analyzer.power.set_attenuator(power_attenuator = 1.0) \n
		Sets the attenuation of the external attenuator. The command can be used only if a R&S FSW is connected to the R&S SMW. \n
			:param power_attenuator: float Range: -600 to 500
		"""
		param = Conversions.decimal_value_to_str(power_attenuator)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:RADar:ANALyzer:POWer:ATTenuator {param}')

	def get_reference(self) -> float:
		"""SCPI: [SOURce<HW>]:REGenerator:RADar:ANALyzer:POWer:REFerence \n
		Snippet: value: float = driver.source.regenerator.radar.analyzer.power.get_reference() \n
		Queries the reference level of the analyzer. The command can be used only if a R&S FSW is connected to the R&S SMW. \n
			:return: power_reference: float Range: -400 to 500
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:RADar:ANALyzer:POWer:REFerence?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Power':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Power(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
