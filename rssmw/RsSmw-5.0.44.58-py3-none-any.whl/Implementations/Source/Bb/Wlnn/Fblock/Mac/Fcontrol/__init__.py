from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fcontrol:
	"""Fcontrol commands group definition. 7 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fcontrol", core, parent)

	@property
	def bindication(self):
		"""bindication commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bindication'):
			from .Bindication import Bindication
			self._bindication = Bindication(self._core, self._cmd_group)
		return self._bindication

	@property
	def dindication(self):
		"""dindication commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dindication'):
			from .Dindication import Dindication
			self._dindication = Dindication(self._core, self._cmd_group)
		return self._dindication

	@property
	def fcontrol(self):
		"""fcontrol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fcontrol'):
			from .Fcontrol import Fcontrol
			self._fcontrol = Fcontrol(self._core, self._cmd_group)
		return self._fcontrol

	@property
	def ntiPresent(self):
		"""ntiPresent commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ntiPresent'):
			from .NtiPresent import NtiPresent
			self._ntiPresent = NtiPresent(self._core, self._cmd_group)
		return self._ntiPresent

	@property
	def pframe(self):
		"""pframe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pframe'):
			from .Pframe import Pframe
			self._pframe = Pframe(self._core, self._cmd_group)
		return self._pframe

	@property
	def ptype(self):
		"""ptype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ptype'):
			from .Ptype import Ptype
			self._ptype = Ptype(self._core, self._cmd_group)
		return self._ptype

	@property
	def reserved(self):
		"""reserved commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reserved'):
			from .Reserved import Reserved
			self._reserved = Reserved(self._core, self._cmd_group)
		return self._reserved

	def clone(self) -> 'Fcontrol':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fcontrol(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
