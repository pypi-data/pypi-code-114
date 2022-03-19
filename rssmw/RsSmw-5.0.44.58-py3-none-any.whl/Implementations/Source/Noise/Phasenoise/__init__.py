from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phasenoise:
	"""Phasenoise commands group definition. 6 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phasenoise", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def level(self):
		"""level commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_level'):
			from .Level import Level
			self._level = Level(self._core, self._cmd_group)
		return self._level

	@property
	def shape(self):
		"""shape commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_shape'):
			from .Shape import Shape
			self._shape = Shape(self._core, self._cmd_group)
		return self._shape

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:NOISe:PHASenoise:[STATe] \n
		Snippet: value: bool = driver.source.noise.phasenoise.get_state() \n
		Enables or disables the phase noise generator. \n
			:return: phasenoise_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:NOISe:PHASenoise:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, phasenoise_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:NOISe:PHASenoise:[STATe] \n
		Snippet: driver.source.noise.phasenoise.set_state(phasenoise_state = False) \n
		Enables or disables the phase noise generator. \n
			:param phasenoise_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(phasenoise_state)
		self._core.io.write(f'SOURce<HwInstance>:NOISe:PHASenoise:STATe {param}')

	def clone(self) -> 'Phasenoise':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Phasenoise(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
