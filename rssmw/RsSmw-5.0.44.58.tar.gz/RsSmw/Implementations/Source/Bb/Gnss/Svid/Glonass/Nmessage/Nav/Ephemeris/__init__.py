from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ephemeris:
	"""Ephemeris commands group definition. 29 total commands, 19 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ephemeris", core, parent)

	@property
	def aoep(self):
		"""aoep commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aoep'):
			from .Aoep import Aoep
			self._aoep = Aoep(self._core, self._cmd_group)
		return self._aoep

	@property
	def cfm(self):
		"""cfm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cfm'):
			from .Cfm import Cfm
			self._cfm = Cfm(self._core, self._cmd_group)
		return self._cfm

	@property
	def health(self):
		"""health commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_health'):
			from .Health import Health
			self._health = Health(self._core, self._cmd_group)
		return self._health

	@property
	def p(self):
		"""p commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_p'):
			from .P import P
			self._p = P(self._core, self._cmd_group)
		return self._p

	@property
	def seType(self):
		"""seType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_seType'):
			from .SeType import SeType
			self._seType = SeType(self._core, self._cmd_group)
		return self._seType

	@property
	def talignment(self):
		"""talignment commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_talignment'):
			from .Talignment import Talignment
			self._talignment = Talignment(self._core, self._cmd_group)
		return self._talignment

	@property
	def tindex(self):
		"""tindex commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_tindex'):
			from .Tindex import Tindex
			self._tindex = Tindex(self._core, self._cmd_group)
		return self._tindex

	@property
	def tinterval(self):
		"""tinterval commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tinterval'):
			from .Tinterval import Tinterval
			self._tinterval = Tinterval(self._core, self._cmd_group)
		return self._tinterval

	@property
	def toe(self):
		"""toe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_toe'):
			from .Toe import Toe
			self._toe = Toe(self._core, self._cmd_group)
		return self._toe

	@property
	def ura(self):
		"""ura commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ura'):
			from .Ura import Ura
			self._ura = Ura(self._core, self._cmd_group)
		return self._ura

	@property
	def xddn(self):
		"""xddn commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_xddn'):
			from .Xddn import Xddn
			self._xddn = Xddn(self._core, self._cmd_group)
		return self._xddn

	@property
	def xdn(self):
		"""xdn commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_xdn'):
			from .Xdn import Xdn
			self._xdn = Xdn(self._core, self._cmd_group)
		return self._xdn

	@property
	def xn(self):
		"""xn commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_xn'):
			from .Xn import Xn
			self._xn = Xn(self._core, self._cmd_group)
		return self._xn

	@property
	def yddn(self):
		"""yddn commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_yddn'):
			from .Yddn import Yddn
			self._yddn = Yddn(self._core, self._cmd_group)
		return self._yddn

	@property
	def ydn(self):
		"""ydn commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ydn'):
			from .Ydn import Ydn
			self._ydn = Ydn(self._core, self._cmd_group)
		return self._ydn

	@property
	def yn(self):
		"""yn commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_yn'):
			from .Yn import Yn
			self._yn = Yn(self._core, self._cmd_group)
		return self._yn

	@property
	def zddn(self):
		"""zddn commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_zddn'):
			from .Zddn import Zddn
			self._zddn = Zddn(self._core, self._cmd_group)
		return self._zddn

	@property
	def zdn(self):
		"""zdn commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_zdn'):
			from .Zdn import Zdn
			self._zdn = Zdn(self._core, self._cmd_group)
		return self._zdn

	@property
	def zn(self):
		"""zn commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_zn'):
			from .Zn import Zn
			self._zn = Zn(self._core, self._cmd_group)
		return self._zn

	def clone(self) -> 'Ephemeris':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ephemeris(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
