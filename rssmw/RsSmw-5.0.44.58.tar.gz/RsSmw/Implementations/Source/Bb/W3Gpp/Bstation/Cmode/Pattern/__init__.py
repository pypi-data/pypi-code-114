from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pattern:
	"""Pattern commands group definition. 4 total commands, 4 Subgroups, 0 group commands
	Repeated Capability: PatternIx, default value after init: PatternIx.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_patternIx_get', 'repcap_patternIx_set', repcap.PatternIx.Nr1)

	def repcap_patternIx_set(self, patternIx: repcap.PatternIx) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to PatternIx.Default
		Default value after init: PatternIx.Nr1"""
		self._cmd_group.set_repcap_enum_value(patternIx)

	def repcap_patternIx_get(self) -> repcap.PatternIx:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def tgd(self):
		"""tgd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tgd'):
			from .Tgd import Tgd
			self._tgd = Tgd(self._core, self._cmd_group)
		return self._tgd

	@property
	def tgl(self):
		"""tgl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tgl'):
			from .Tgl import Tgl
			self._tgl = Tgl(self._core, self._cmd_group)
		return self._tgl

	@property
	def tgpl(self):
		"""tgpl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tgpl'):
			from .Tgpl import Tgpl
			self._tgpl = Tgpl(self._core, self._cmd_group)
		return self._tgpl

	@property
	def tgsn(self):
		"""tgsn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tgsn'):
			from .Tgsn import Tgsn
			self._tgsn = Tgsn(self._core, self._cmd_group)
		return self._tgsn

	def clone(self) -> 'Pattern':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pattern(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
