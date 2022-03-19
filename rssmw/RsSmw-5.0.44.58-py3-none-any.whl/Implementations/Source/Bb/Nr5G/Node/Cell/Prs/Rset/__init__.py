from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rset:
	"""Rset commands group definition. 18 total commands, 9 Subgroups, 0 group commands
	Repeated Capability: ResourceSetNull, default value after init: ResourceSetNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rset", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_resourceSetNull_get', 'repcap_resourceSetNull_set', repcap.ResourceSetNull.Nr0)

	def repcap_resourceSetNull_set(self, resourceSetNull: repcap.ResourceSetNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ResourceSetNull.Default
		Default value after init: ResourceSetNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(resourceSetNull)

	def repcap_resourceSetNull_get(self) -> repcap.ResourceSetNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def cmbSize(self):
		"""cmbSize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cmbSize'):
			from .CmbSize import CmbSize
			self._cmbSize = CmbSize(self._core, self._cmd_group)
		return self._cmbSize

	@property
	def nresources(self):
		"""nresources commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nresources'):
			from .Nresources import Nresources
			self._nresources = Nresources(self._core, self._cmd_group)
		return self._nresources

	@property
	def per(self):
		"""per commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_per'):
			from .Per import Per
			self._per = Per(self._core, self._cmd_group)
		return self._per

	@property
	def rbNumber(self):
		"""rbNumber commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbNumber'):
			from .RbNumber import RbNumber
			self._rbNumber = RbNumber(self._core, self._cmd_group)
		return self._rbNumber

	@property
	def rbStart(self):
		"""rbStart commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbStart'):
			from .RbStart import RbStart
			self._rbStart = RbStart(self._core, self._cmd_group)
		return self._rbStart

	@property
	def repFactor(self):
		"""repFactor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_repFactor'):
			from .RepFactor import RepFactor
			self._repFactor = RepFactor(self._core, self._cmd_group)
		return self._repFactor

	@property
	def res(self):
		"""res commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_res'):
			from .Res import Res
			self._res = Res(self._core, self._cmd_group)
		return self._res

	@property
	def slOffset(self):
		"""slOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slOffset'):
			from .SlOffset import SlOffset
			self._slOffset = SlOffset(self._core, self._cmd_group)
		return self._slOffset

	@property
	def tgap(self):
		"""tgap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tgap'):
			from .Tgap import Tgap
			self._tgap = Tgap(self._core, self._cmd_group)
		return self._tgap

	def clone(self) -> 'Rset':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rset(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
