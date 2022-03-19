from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tsignal:
	"""Tsignal commands group definition. 18 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsignal", core, parent)

	@property
	def awgn(self):
		"""awgn commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_awgn'):
			from .Awgn import Awgn
			self._awgn = Awgn(self._core, self._cmd_group)
		return self._awgn

	@property
	def ciq(self):
		"""ciq commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_ciq'):
			from .Ciq import Ciq
			self._ciq = Ciq(self._core, self._cmd_group)
		return self._ciq

	@property
	def rectangle(self):
		"""rectangle commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_rectangle'):
			from .Rectangle import Rectangle
			self._rectangle = Rectangle(self._core, self._cmd_group)
		return self._rectangle

	@property
	def sine(self):
		"""sine commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_sine'):
			from .Sine import Sine
			self._sine = Sine(self._core, self._cmd_group)
		return self._sine

	def clone(self) -> 'Tsignal':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tsignal(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
