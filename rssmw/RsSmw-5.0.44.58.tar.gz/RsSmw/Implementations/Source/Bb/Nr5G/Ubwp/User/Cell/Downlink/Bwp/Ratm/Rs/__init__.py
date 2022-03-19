from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal.RepeatedCapability import RepeatedCapability
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rs:
	"""Rs commands group definition. 7 total commands, 7 Subgroups, 0 group commands
	Repeated Capability: RateSettingNull, default value after init: RateSettingNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rs", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_rateSettingNull_get', 'repcap_rateSettingNull_set', repcap.RateSettingNull.Nr0)

	def repcap_rateSettingNull_set(self, rateSettingNull: repcap.RateSettingNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to RateSettingNull.Default
		Default value after init: RateSettingNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(rateSettingNull)

	def repcap_rateSettingNull_get(self) -> repcap.RateSettingNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def grid(self):
		"""grid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_grid'):
			from .Grid import Grid
			self._grid = Grid(self._core, self._cmd_group)
		return self._grid

	@property
	def per(self):
		"""per commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_per'):
			from .Per import Per
			self._per = Per(self._core, self._cmd_group)
		return self._per

	@property
	def perPatt(self):
		"""perPatt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_perPatt'):
			from .PerPatt import PerPatt
			self._perPatt = PerPatt(self._core, self._cmd_group)
		return self._perPatt

	@property
	def rbdlist(self):
		"""rbdlist commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbdlist'):
			from .Rbdlist import Rbdlist
			self._rbdlist = Rbdlist(self._core, self._cmd_group)
		return self._rbdlist

	@property
	def rbpAtt(self):
		"""rbpAtt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbpAtt'):
			from .RbpAtt import RbpAtt
			self._rbpAtt = RbpAtt(self._core, self._cmd_group)
		return self._rbpAtt

	@property
	def slot(self):
		"""slot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slot'):
			from .Slot import Slot
			self._slot = Slot(self._core, self._cmd_group)
		return self._slot

	@property
	def sltPatt(self):
		"""sltPatt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sltPatt'):
			from .SltPatt import SltPatt
			self._sltPatt = SltPatt(self._core, self._cmd_group)
		return self._sltPatt

	def clone(self) -> 'Rs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
