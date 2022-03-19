from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Noise:
	"""Noise commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("noise", core, parent)

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import Bandwidth
			self._bandwidth = Bandwidth(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def level(self):
		"""level commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_level'):
			from .Level import Level
			self._level = Level(self._core, self._cmd_group)
		return self._level

	# noinspection PyTypeChecker
	def get_state(self) -> enums.NoisAwgnFseState:
		"""SCPI: [SOURce]:NOISe:[STATe] \n
		Snippet: value: enums.NoisAwgnFseState = driver.source.noise.get_state() \n
		No command help available \n
			:return: noise_state_mode: No help available
		"""
		response = self._core.io.query_str('SOURce:NOISe:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.NoisAwgnFseState)

	def set_state(self, noise_state_mode: enums.NoisAwgnFseState) -> None:
		"""SCPI: [SOURce]:NOISe:[STATe] \n
		Snippet: driver.source.noise.set_state(noise_state_mode = enums.NoisAwgnFseState.ADD) \n
		No command help available \n
			:param noise_state_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(noise_state_mode, enums.NoisAwgnFseState)
		self._core.io.write(f'SOURce:NOISe:STATe {param}')

	def clone(self) -> 'Noise':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Noise(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
