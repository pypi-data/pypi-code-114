from ..............Internal.Core import Core
from ..............Internal.CommandsGroup import CommandsGroup
from ..............Internal.RepeatedCapability import RepeatedCapability
from .............. import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Res:
	"""Res commands group definition. 22 total commands, 17 Subgroups, 0 group commands
	Repeated Capability: ResourceNull, default value after init: ResourceNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("res", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_resourceNull_get', 'repcap_resourceNull_set', repcap.ResourceNull.Nr0)

	def repcap_resourceNull_set(self, resourceNull: repcap.ResourceNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ResourceNull.Default
		Default value after init: ResourceNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(resourceNull)

	def repcap_resourceNull_get(self) -> repcap.ResourceNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def apMap(self):
		"""apMap commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_apMap'):
			from .ApMap import ApMap
			self._apMap = ApMap(self._core, self._cmd_group)
		return self._apMap

	@property
	def bhop(self):
		"""bhop commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bhop'):
			from .Bhop import Bhop
			self._bhop = Bhop(self._core, self._cmd_group)
		return self._bhop

	@property
	def bsrs(self):
		"""bsrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bsrs'):
			from .Bsrs import Bsrs
			self._bsrs = Bsrs(self._core, self._cmd_group)
		return self._bsrs

	@property
	def coffset(self):
		"""coffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_coffset'):
			from .Coffset import Coffset
			self._coffset = Coffset(self._core, self._cmd_group)
		return self._coffset

	@property
	def csrs(self):
		"""csrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csrs'):
			from .Csrs import Csrs
			self._csrs = Csrs(self._core, self._cmd_group)
		return self._csrs

	@property
	def fpos(self):
		"""fpos commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fpos'):
			from .Fpos import Fpos
			self._fpos = Fpos(self._core, self._cmd_group)
		return self._fpos

	@property
	def fqShift(self):
		"""fqShift commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fqShift'):
			from .FqShift import FqShift
			self._fqShift = FqShift(self._core, self._cmd_group)
		return self._fqShift

	@property
	def naPort(self):
		"""naPort commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_naPort'):
			from .NaPort import NaPort
			self._naPort = NaPort(self._core, self._cmd_group)
		return self._naPort

	@property
	def offset(self):
		"""offset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_offset'):
			from .Offset import Offset
			self._offset = Offset(self._core, self._cmd_group)
		return self._offset

	@property
	def per(self):
		"""per commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_per'):
			from .Per import Per
			self._per = Per(self._core, self._cmd_group)
		return self._per

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def ptrs(self):
		"""ptrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ptrs'):
			from .Ptrs import Ptrs
			self._ptrs = Ptrs(self._core, self._cmd_group)
		return self._ptrs

	@property
	def refactor(self):
		"""refactor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_refactor'):
			from .Refactor import Refactor
			self._refactor = Refactor(self._core, self._cmd_group)
		return self._refactor

	@property
	def seq(self):
		"""seq commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_seq'):
			from .Seq import Seq
			self._seq = Seq(self._core, self._cmd_group)
		return self._seq

	@property
	def spos(self):
		"""spos commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spos'):
			from .Spos import Spos
			self._spos = Spos(self._core, self._cmd_group)
		return self._spos

	@property
	def symNumber(self):
		"""symNumber commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symNumber'):
			from .SymNumber import SymNumber
			self._symNumber = SymNumber(self._core, self._cmd_group)
		return self._symNumber

	@property
	def trtComb(self):
		"""trtComb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trtComb'):
			from .TrtComb import TrtComb
			self._trtComb = TrtComb(self._core, self._cmd_group)
		return self._trtComb

	def clone(self) -> 'Res':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Res(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
