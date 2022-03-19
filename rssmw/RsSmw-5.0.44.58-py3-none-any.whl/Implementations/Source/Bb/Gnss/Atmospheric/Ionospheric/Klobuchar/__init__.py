from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Klobuchar:
	"""Klobuchar commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("klobuchar", core, parent)

	@property
	def alpha(self):
		"""alpha commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_alpha'):
			from .Alpha import Alpha
			self._alpha = Alpha(self._core, self._cmd_group)
		return self._alpha

	@property
	def beta(self):
		"""beta commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_beta'):
			from .Beta import Beta
			self._beta = Beta(self._core, self._cmd_group)
		return self._beta

	def clone(self) -> 'Klobuchar':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Klobuchar(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
