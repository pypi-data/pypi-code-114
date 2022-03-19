from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mapping:
	"""Mapping commands group definition. 12 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mapping", core, parent)

	@property
	def bbmm(self):
		"""bbmm commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_bbmm'):
			from .Bbmm import Bbmm
			self._bbmm = Bbmm(self._core, self._cmd_group)
		return self._bbmm

	@property
	def fader(self):
		"""fader commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fader'):
			from .Fader import Fader
			self._fader = Fader(self._core, self._cmd_group)
		return self._fader

	@property
	def iqOutput(self):
		"""iqOutput commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOutput'):
			from .IqOutput import IqOutput
			self._iqOutput = IqOutput(self._core, self._cmd_group)
		return self._iqOutput

	@property
	def rf(self):
		"""rf commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rf'):
			from .Rf import Rf
			self._rf = Rf(self._core, self._cmd_group)
		return self._rf

	@property
	def stream(self):
		"""stream commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_stream'):
			from .Stream import Stream
			self._stream = Stream(self._core, self._cmd_group)
		return self._stream

	def clone(self) -> 'Mapping':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mapping(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
