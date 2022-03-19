from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrConfig:
	"""FrConfig commands group definition. 44 total commands, 12 Subgroups, 0 group commands
	Repeated Capability: FrCfgIxNull, default value after init: FrCfgIxNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frConfig", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_frCfgIxNull_get', 'repcap_frCfgIxNull_set', repcap.FrCfgIxNull.Nr0)

	def repcap_frCfgIxNull_set(self, frCfgIxNull: repcap.FrCfgIxNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to FrCfgIxNull.Default
		Default value after init: FrCfgIxNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(frCfgIxNull)

	def repcap_frCfgIxNull_get(self) -> repcap.FrCfgIxNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def btu(self):
		"""btu commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_btu'):
			from .Btu import Btu
			self._btu = Btu(self._core, self._cmd_group)
		return self._btu

	@property
	def conflicts(self):
		"""conflicts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_conflicts'):
			from .Conflicts import Conflicts
			self._conflicts = Conflicts(self._core, self._cmd_group)
		return self._conflicts

	@property
	def frbw(self):
		"""frbw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frbw'):
			from .Frbw import Frbw
			self._frbw = Frbw(self._core, self._cmd_group)
		return self._frbw

	@property
	def frsTime(self):
		"""frsTime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frsTime'):
			from .FrsTime import FrsTime
			self._frsTime = FrsTime(self._core, self._cmd_group)
		return self._frsTime

	@property
	def grid(self):
		"""grid commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_grid'):
			from .Grid import Grid
			self._grid = Grid(self._core, self._cmd_group)
		return self._grid

	@property
	def grids(self):
		"""grids commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_grids'):
			from .Grids import Grids
			self._grids = Grids(self._core, self._cmd_group)
		return self._grids

	@property
	def offset(self):
		"""offset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_offset'):
			from .Offset import Offset
			self._offset = Offset(self._core, self._cmd_group)
		return self._offset

	@property
	def resolve(self):
		"""resolve commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_resolve'):
			from .Resolve import Resolve
			self._resolve = Resolve(self._core, self._cmd_group)
		return self._resolve

	@property
	def sec(self):
		"""sec commands group. 29 Sub-classes, 0 commands."""
		if not hasattr(self, '_sec'):
			from .Sec import Sec
			self._sec = Sec(self._core, self._cmd_group)
		return self._sec

	@property
	def sections(self):
		"""sections commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sections'):
			from .Sections import Sections
			self._sections = Sections(self._core, self._cmd_group)
		return self._sections

	@property
	def secIdx(self):
		"""secIdx commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_secIdx'):
			from .SecIdx import SecIdx
			self._secIdx = SecIdx(self._core, self._cmd_group)
		return self._secIdx

	@property
	def txFormat(self):
		"""txFormat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txFormat'):
			from .TxFormat import TxFormat
			self._txFormat = TxFormat(self._core, self._cmd_group)
		return self._txFormat

	def clone(self) -> 'FrConfig':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FrConfig(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
