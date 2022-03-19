from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cell:
	"""Cell commands group definition. 17 total commands, 14 Subgroups, 0 group commands
	Repeated Capability: CellNull, default value after init: CellNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cell", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_cellNull_get', 'repcap_cellNull_set', repcap.CellNull.Nr0)

	def repcap_cellNull_set(self, cellNull: repcap.CellNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to CellNull.Default
		Default value after init: CellNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(cellNull)

	def repcap_cellNull_get(self) -> repcap.CellNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def cdmType(self):
		"""cdmType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cdmType'):
			from .CdmType import CdmType
			self._cdmType = CdmType(self._core, self._cmd_group)
		return self._cdmType

	@property
	def config(self):
		"""config commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_config'):
			from .Config import Config
			self._config = Config(self._core, self._cmd_group)
		return self._config

	@property
	def dwpts(self):
		"""dwpts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dwpts'):
			from .Dwpts import Dwpts
			self._dwpts = Dwpts(self._core, self._cmd_group)
		return self._dwpts

	@property
	def frDensity(self):
		"""frDensity commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frDensity'):
			from .FrDensity import FrDensity
			self._frDensity = FrDensity(self._core, self._cmd_group)
		return self._frDensity

	@property
	def nap(self):
		"""nap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nap'):
			from .Nap import Nap
			self._nap = Nap(self._core, self._cmd_group)
		return self._nap

	@property
	def ncfg(self):
		"""ncfg commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ncfg'):
			from .Ncfg import Ncfg
			self._ncfg = Ncfg(self._core, self._cmd_group)
		return self._ncfg

	@property
	def pow(self):
		"""pow commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pow'):
			from .Pow import Pow
			self._pow = Pow(self._core, self._cmd_group)
		return self._pow

	@property
	def scid(self):
		"""scid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scid'):
			from .Scid import Scid
			self._scid = Scid(self._core, self._cmd_group)
		return self._scid

	@property
	def sfDelta(self):
		"""sfDelta commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfDelta'):
			from .SfDelta import SfDelta
			self._sfDelta = SfDelta(self._core, self._cmd_group)
		return self._sfDelta

	@property
	def sfi(self):
		"""sfi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfi'):
			from .Sfi import Sfi
			self._sfi = Sfi(self._core, self._cmd_group)
		return self._sfi

	@property
	def sft(self):
		"""sft commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sft'):
			from .Sft import Sft
			self._sft = Sft(self._core, self._cmd_group)
		return self._sft

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def transcomb(self):
		"""transcomb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_transcomb'):
			from .Transcomb import Transcomb
			self._transcomb = Transcomb(self._core, self._cmd_group)
		return self._transcomb

	@property
	def zprs(self):
		"""zprs commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_zprs'):
			from .Zprs import Zprs
			self._zprs = Zprs(self._core, self._cmd_group)
		return self._zprs

	def clone(self) -> 'Cell':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cell(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
