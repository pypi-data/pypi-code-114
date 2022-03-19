from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Noise:
	"""Noise commands group definition. 18 total commands, 4 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("noise", core, parent)

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import Bandwidth
			self._bandwidth = Bandwidth(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def impulsive(self):
		"""impulsive commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_impulsive'):
			from .Impulsive import Impulsive
			self._impulsive = Impulsive(self._core, self._cmd_group)
		return self._impulsive

	@property
	def level(self):
		"""level commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_level'):
			from .Level import Level
			self._level = Level(self._core, self._cmd_group)
		return self._level

	@property
	def phasenoise(self):
		"""phasenoise commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_phasenoise'):
			from .Phasenoise import Phasenoise
			self._phasenoise = Phasenoise(self._core, self._cmd_group)
		return self._phasenoise

	# noinspection PyTypeChecker
	def get_distribution(self) -> enums.NoisDistrib:
		"""SCPI: [SOURce<HW>]:NOISe:DISTribution \n
		Snippet: value: enums.NoisDistrib = driver.source.noise.get_distribution() \n
		Sets the distribution of the noise power density. \n
			:return: distribution: GAUSs| EQUal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:NOISe:DISTribution?')
		return Conversions.str_to_scalar_enum(response, enums.NoisDistrib)

	def set_distribution(self, distribution: enums.NoisDistrib) -> None:
		"""SCPI: [SOURce<HW>]:NOISe:DISTribution \n
		Snippet: driver.source.noise.set_distribution(distribution = enums.NoisDistrib.EQUal) \n
		Sets the distribution of the noise power density. \n
			:param distribution: GAUSs| EQUal
		"""
		param = Conversions.enum_scalar_to_str(distribution, enums.NoisDistrib)
		self._core.io.write(f'SOURce<HwInstance>:NOISe:DISTribution {param}')

	def clone(self) -> 'Noise':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Noise(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
