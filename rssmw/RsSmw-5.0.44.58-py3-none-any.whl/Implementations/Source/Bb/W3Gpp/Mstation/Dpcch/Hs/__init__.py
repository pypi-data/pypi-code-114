from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hs:
	"""Hs commands group definition. 45 total commands, 20 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hs", core, parent)

	@property
	def ccode(self):
		"""ccode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ccode'):
			from .Ccode import Ccode
			self._ccode = Ccode(self._core, self._cmd_group)
		return self._ccode

	@property
	def compatibility(self):
		"""compatibility commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_compatibility'):
			from .Compatibility import Compatibility
			self._compatibility = Compatibility(self._core, self._cmd_group)
		return self._compatibility

	@property
	def cqi(self):
		"""cqi commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cqi'):
			from .Cqi import Cqi
			self._cqi = Cqi(self._core, self._cmd_group)
		return self._cqi

	@property
	def hack(self):
		"""hack commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_hack'):
			from .Hack import Hack
			self._hack = Hack(self._core, self._cmd_group)
		return self._hack

	@property
	def haPattern(self):
		"""haPattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_haPattern'):
			from .HaPattern import HaPattern
			self._haPattern = HaPattern(self._core, self._cmd_group)
		return self._haPattern

	@property
	def mimo(self):
		"""mimo commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_mimo'):
			from .Mimo import Mimo
			self._mimo = Mimo(self._core, self._cmd_group)
		return self._mimo

	@property
	def mmode(self):
		"""mmode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mmode'):
			from .Mmode import Mmode
			self._mmode = Mmode(self._core, self._cmd_group)
		return self._mmode

	@property
	def pcqi(self):
		"""pcqi commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcqi'):
			from .Pcqi import Pcqi
			self._pcqi = Pcqi(self._core, self._cmd_group)
		return self._pcqi

	@property
	def poAck(self):
		"""poAck commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_poAck'):
			from .PoAck import PoAck
			self._poAck = PoAck(self._core, self._cmd_group)
		return self._poAck

	@property
	def poNack(self):
		"""poNack commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_poNack'):
			from .PoNack import PoNack
			self._poNack = PoNack(self._core, self._cmd_group)
		return self._poNack

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def row(self):
		"""row commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_row'):
			from .Row import Row
			self._row = Row(self._core, self._cmd_group)
		return self._row

	@property
	def rowCount(self):
		"""rowCount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rowCount'):
			from .RowCount import RowCount
			self._rowCount = RowCount(self._core, self._cmd_group)
		return self._rowCount

	@property
	def sc(self):
		"""sc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_sc'):
			from .Sc import Sc
			self._sc = Sc(self._core, self._cmd_group)
		return self._sc

	@property
	def scActive(self):
		"""scActive commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scActive'):
			from .ScActive import ScActive
			self._scActive = ScActive(self._core, self._cmd_group)
		return self._scActive

	@property
	def sdelay(self):
		"""sdelay commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sdelay'):
			from .Sdelay import Sdelay
			self._sdelay = Sdelay(self._core, self._cmd_group)
		return self._sdelay

	@property
	def sformat(self):
		"""sformat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sformat'):
			from .Sformat import Sformat
			self._sformat = Sformat(self._core, self._cmd_group)
		return self._sformat

	@property
	def slength(self):
		"""slength commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_slength'):
			from .Slength import Slength
			self._slength = Slength(self._core, self._cmd_group)
		return self._slength

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def ttiDistance(self):
		"""ttiDistance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ttiDistance'):
			from .TtiDistance import TtiDistance
			self._ttiDistance = TtiDistance(self._core, self._cmd_group)
		return self._ttiDistance

	def clone(self) -> 'Hs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Hs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
