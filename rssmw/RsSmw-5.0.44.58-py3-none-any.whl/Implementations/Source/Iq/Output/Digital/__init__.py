from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Digital:
	"""Digital commands group definition. 40 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("digital", core, parent)

	@property
	def bbmm(self):
		"""bbmm commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_bbmm'):
			from .Bbmm import Bbmm
			self._bbmm = Bbmm(self._core, self._cmd_group)
		return self._bbmm

	@property
	def fader(self):
		"""fader commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_fader'):
			from .Fader import Fader
			self._fader = Fader(self._core, self._cmd_group)
		return self._fader

	def clone(self) -> 'Digital':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Digital(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
