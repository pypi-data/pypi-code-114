from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Diagnostic:
	"""Diagnostic commands group definition. 5 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("diagnostic", core, parent)

	@property
	def counters(self):
		"""counters commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_counters'):
			from .Counters import Counters
			self._counters = Counters(self._core, self._cmd_group)
		return self._counters

	@property
	def test(self):
		"""test commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_test'):
			from .Test import Test
			self._test = Test(self._core, self._cmd_group)
		return self._test

	def clone(self) -> 'Diagnostic':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Diagnostic(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
