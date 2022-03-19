from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 4 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	@property
	def apply(self):
		"""apply commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apply'):
			from .Apply import Apply
			self._apply = Apply(self._core, self._cmd_group)
		return self._apply

	@property
	def updated(self):
		"""updated commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_updated'):
			from .Updated import Updated
			self._updated = Updated(self._core, self._cmd_group)
		return self._updated

	@property
	def valid(self):
		"""valid commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_valid'):
			from .Valid import Valid
			self._valid = Valid(self._core, self._cmd_group)
		return self._valid

	def get(self, level: float) -> float:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:LEVel \n
		Snippet: value: float = driver.source.regenerator.simulation.level.get(level = 1.0) \n
		Queries the calculated level value. \n
			:param level: float Range: -541 to 591
			:return: level: float Range: -541 to 591"""
		param = Conversions.decimal_value_to_str(level)
		response = self._core.io.query_str(f'SOURce<HwInstance>:REGenerator:SIMulation:LEVel? {param}')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Level':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Level(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
