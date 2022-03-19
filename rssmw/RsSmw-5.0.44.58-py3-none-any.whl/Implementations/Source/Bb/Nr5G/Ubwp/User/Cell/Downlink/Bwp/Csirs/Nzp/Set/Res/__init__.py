from ..............Internal.Core import Core
from ..............Internal.CommandsGroup import CommandsGroup
from ..............Internal.RepeatedCapability import RepeatedCapability
from .............. import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Res:
	"""Res commands group definition. 17 total commands, 14 Subgroups, 0 group commands
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
	def bitmap(self):
		"""bitmap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bitmap'):
			from .Bitmap import Bitmap
			self._bitmap = Bitmap(self._core, self._cmd_group)
		return self._bitmap

	@property
	def cdmType(self):
		"""cdmType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cdmType'):
			from .CdmType import CdmType
			self._cdmType = CdmType(self._core, self._cmd_group)
		return self._cdmType

	@property
	def density(self):
		"""density commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_density'):
			from .Density import Density
			self._density = Density(self._core, self._cmd_group)
		return self._density

	@property
	def i0(self):
		"""i0 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_i0'):
			from .I0 import I0
			self._i0 = I0(self._core, self._cmd_group)
		return self._i0

	@property
	def i1(self):
		"""i1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_i1'):
			from .I1 import I1
			self._i1 = I1(self._core, self._cmd_group)
		return self._i1

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
	def ports(self):
		"""ports commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ports'):
			from .Ports import Ports
			self._ports = Ports(self._core, self._cmd_group)
		return self._ports

	@property
	def pwr(self):
		"""pwr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pwr'):
			from .Pwr import Pwr
			self._pwr = Pwr(self._core, self._cmd_group)
		return self._pwr

	@property
	def rbNumber(self):
		"""rbNumber commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbNumber'):
			from .RbNumber import RbNumber
			self._rbNumber = RbNumber(self._core, self._cmd_group)
		return self._rbNumber

	@property
	def row(self):
		"""row commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_row'):
			from .Row import Row
			self._row = Row(self._core, self._cmd_group)
		return self._row

	@property
	def scid(self):
		"""scid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scid'):
			from .Scid import Scid
			self._scid = Scid(self._core, self._cmd_group)
		return self._scid

	@property
	def srbNumber(self):
		"""srbNumber commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_srbNumber'):
			from .SrbNumber import SrbNumber
			self._srbNumber = SrbNumber(self._core, self._cmd_group)
		return self._srbNumber

	def clone(self) -> 'Res':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Res(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
