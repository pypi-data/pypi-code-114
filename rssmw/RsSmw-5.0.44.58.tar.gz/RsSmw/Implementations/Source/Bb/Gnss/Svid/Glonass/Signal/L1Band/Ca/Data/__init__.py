from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 8 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	@property
	def meandering(self):
		"""meandering commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_meandering'):
			from .Meandering import Meandering
			self._meandering = Meandering(self._core, self._cmd_group)
		return self._meandering

	@property
	def nmessage(self):
		"""nmessage commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_nmessage'):
			from .Nmessage import Nmessage
			self._nmessage = Nmessage(self._core, self._cmd_group)
		return self._nmessage

	@property
	def pcode(self):
		"""pcode commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcode'):
			from .Pcode import Pcode
			self._pcode = Pcode(self._core, self._cmd_group)
		return self._pcode

	@property
	def tsequence(self):
		"""tsequence commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tsequence'):
			from .Tsequence import Tsequence
			self._tsequence = Tsequence(self._core, self._cmd_group)
		return self._tsequence

	def clone(self) -> 'Data':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Data(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
