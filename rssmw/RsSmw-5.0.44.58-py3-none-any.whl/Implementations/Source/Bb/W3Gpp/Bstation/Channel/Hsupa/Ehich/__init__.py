from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ehich:
	"""Ehich commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ehich", core, parent)

	@property
	def ctype(self):
		"""ctype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ctype'):
			from .Ctype import Ctype
			self._ctype = Ctype(self._core, self._cmd_group)
		return self._ctype

	@property
	def dtau(self):
		"""dtau commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dtau'):
			from .Dtau import Dtau
			self._dtau = Dtau(self._core, self._cmd_group)
		return self._dtau

	@property
	def etau(self):
		"""etau commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_etau'):
			from .Etau import Etau
			self._etau = Etau(self._core, self._cmd_group)
		return self._etau

	@property
	def rgPattern(self):
		"""rgPattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rgPattern'):
			from .RgPattern import RgPattern
			self._rgPattern = RgPattern(self._core, self._cmd_group)
		return self._rgPattern

	@property
	def ssIndex(self):
		"""ssIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssIndex'):
			from .SsIndex import SsIndex
			self._ssIndex = SsIndex(self._core, self._cmd_group)
		return self._ssIndex

	@property
	def ttiedch(self):
		"""ttiedch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ttiedch'):
			from .Ttiedch import Ttiedch
			self._ttiedch = Ttiedch(self._core, self._cmd_group)
		return self._ttiedch

	def clone(self) -> 'Ehich':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ehich(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
