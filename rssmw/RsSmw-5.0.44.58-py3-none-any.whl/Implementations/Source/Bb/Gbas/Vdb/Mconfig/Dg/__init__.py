from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dg:
	"""Dg commands group definition. 16 total commands, 12 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dg", core, parent)

	@property
	def ccgp(self):
		"""ccgp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccgp'):
			from .Ccgp import Ccgp
			self._ccgp = Ccgp(self._core, self._cmd_group)
		return self._ccgp

	@property
	def file(self):
		"""file commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_file'):
			from .File import File
			self._file = File(self._core, self._cmd_group)
		return self._file

	@property
	def gpolynomial(self):
		"""gpolynomial commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_gpolynomial'):
			from .Gpolynomial import Gpolynomial
			self._gpolynomial = Gpolynomial(self._core, self._cmd_group)
		return self._gpolynomial

	@property
	def m11state(self):
		"""m11state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_m11state'):
			from .M11state import M11state
			self._m11state = M11state(self._core, self._cmd_group)
		return self._m11state

	@property
	def m1state(self):
		"""m1state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_m1state'):
			from .M1state import M1state
			self._m1state = M1state(self._core, self._cmd_group)
		return self._m1state

	@property
	def predefined(self):
		"""predefined commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_predefined'):
			from .Predefined import Predefined
			self._predefined = Predefined(self._core, self._cmd_group)
		return self._predefined

	@property
	def rbOrder(self):
		"""rbOrder commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rbOrder'):
			from .RbOrder import RbOrder
			self._rbOrder = RbOrder(self._core, self._cmd_group)
		return self._rbOrder

	@property
	def sfile(self):
		"""sfile commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfile'):
			from .Sfile import Sfile
			self._sfile = Sfile(self._core, self._cmd_group)
		return self._sfile

	@property
	def spredefined(self):
		"""spredefined commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_spredefined'):
			from .Spredefined import Spredefined
			self._spredefined = Spredefined(self._core, self._cmd_group)
		return self._spredefined

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def suser(self):
		"""suser commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_suser'):
			from .Suser import Suser
			self._suser = Suser(self._core, self._cmd_group)
		return self._suser

	@property
	def user(self):
		"""user commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_user'):
			from .User import User
			self._user = User(self._core, self._cmd_group)
		return self._user

	def clone(self) -> 'Dg':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dg(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
