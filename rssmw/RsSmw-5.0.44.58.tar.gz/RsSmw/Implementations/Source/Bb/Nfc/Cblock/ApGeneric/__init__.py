from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApGeneric:
	"""ApGeneric commands group definition. 9 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("apGeneric", core, parent)

	@property
	def bodata(self):
		"""bodata commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bodata'):
			from .Bodata import Bodata
			self._bodata = Bodata(self._core, self._cmd_group)
		return self._bodata

	@property
	def boLength(self):
		"""boLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_boLength'):
			from .BoLength import BoLength
			self._boLength = BoLength(self._core, self._cmd_group)
		return self._boLength

	@property
	def ftype(self):
		"""ftype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ftype'):
			from .Ftype import Ftype
			self._ftype = Ftype(self._core, self._cmd_group)
		return self._ftype

	@property
	def shdata(self):
		"""shdata commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_shdata'):
			from .Shdata import Shdata
			self._shdata = Shdata(self._core, self._cmd_group)
		return self._shdata

	@property
	def shLength(self):
		"""shLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_shLength'):
			from .ShLength import ShLength
			self._shLength = ShLength(self._core, self._cmd_group)
		return self._shLength

	@property
	def stdLength(self):
		"""stdLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stdLength'):
			from .StdLength import StdLength
			self._stdLength = StdLength(self._core, self._cmd_group)
		return self._stdLength

	@property
	def stdata(self):
		"""stdata commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stdata'):
			from .Stdata import Stdata
			self._stdata = Stdata(self._core, self._cmd_group)
		return self._stdata

	@property
	def stePresent(self):
		"""stePresent commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stePresent'):
			from .StePresent import StePresent
			self._stePresent = StePresent(self._core, self._cmd_group)
		return self._stePresent

	@property
	def stpLength(self):
		"""stpLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stpLength'):
			from .StpLength import StpLength
			self._stpLength = StpLength(self._core, self._cmd_group)
		return self._stpLength

	def clone(self) -> 'ApGeneric':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ApGeneric(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
