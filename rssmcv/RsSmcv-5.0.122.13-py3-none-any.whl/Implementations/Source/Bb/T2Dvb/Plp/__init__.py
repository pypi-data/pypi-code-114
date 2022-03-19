from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Plp:
	"""Plp commands group definition. 29 total commands, 21 Subgroups, 0 group commands
	Repeated Capability: PhysicalLayerPipe, default value after init: PhysicalLayerPipe.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plp", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_physicalLayerPipe_get', 'repcap_physicalLayerPipe_set', repcap.PhysicalLayerPipe.Nr1)

	def repcap_physicalLayerPipe_set(self, physicalLayerPipe: repcap.PhysicalLayerPipe) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to PhysicalLayerPipe.Default
		Default value after init: PhysicalLayerPipe.Nr1"""
		self._cmd_group.set_repcap_enum_value(physicalLayerPipe)

	def repcap_physicalLayerPipe_get(self) -> repcap.PhysicalLayerPipe:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def blocks(self):
		"""blocks commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_blocks'):
			from .Blocks import Blocks
			self._blocks = Blocks(self._core, self._cmd_group)
		return self._blocks

	@property
	def cmType(self):
		"""cmType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cmType'):
			from .CmType import CmType
			self._cmType = CmType(self._core, self._cmd_group)
		return self._cmType

	@property
	def constel(self):
		"""constel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_constel'):
			from .Constel import Constel
			self._constel = Constel(self._core, self._cmd_group)
		return self._constel

	@property
	def crotation(self):
		"""crotation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crotation'):
			from .Crotation import Crotation
			self._crotation = Crotation(self._core, self._cmd_group)
		return self._crotation

	@property
	def fecFrame(self):
		"""fecFrame commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fecFrame'):
			from .FecFrame import FecFrame
			self._fecFrame = FecFrame(self._core, self._cmd_group)
		return self._fecFrame

	@property
	def frameIndex(self):
		"""frameIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frameIndex'):
			from .FrameIndex import FrameIndex
			self._frameIndex = FrameIndex(self._core, self._cmd_group)
		return self._frameIndex

	@property
	def group(self):
		"""group commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_group'):
			from .Group import Group
			self._group = Group(self._core, self._cmd_group)
		return self._group

	@property
	def ibs(self):
		"""ibs commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_ibs'):
			from .Ibs import Ibs
			self._ibs = Ibs(self._core, self._cmd_group)
		return self._ibs

	@property
	def id(self):
		"""id commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_id'):
			from .Id import Id
			self._id = Id(self._core, self._cmd_group)
		return self._id

	@property
	def inputPy(self):
		"""inputPy commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

	@property
	def issy(self):
		"""issy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_issy'):
			from .Issy import Issy
			self._issy = Issy(self._core, self._cmd_group)
		return self._issy

	@property
	def maxBlocks(self):
		"""maxBlocks commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maxBlocks'):
			from .MaxBlocks import MaxBlocks
			self._maxBlocks = MaxBlocks(self._core, self._cmd_group)
		return self._maxBlocks

	@property
	def npd(self):
		"""npd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_npd'):
			from .Npd import Npd
			self._npd = Npd(self._core, self._cmd_group)
		return self._npd

	@property
	def oibPlp(self):
		"""oibPlp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_oibPlp'):
			from .OibPlp import OibPlp
			self._oibPlp = OibPlp(self._core, self._cmd_group)
		return self._oibPlp

	@property
	def packetLength(self):
		"""packetLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_packetLength'):
			from .PacketLength import PacketLength
			self._packetLength = PacketLength(self._core, self._cmd_group)
		return self._packetLength

	@property
	def padFlag(self):
		"""padFlag commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_padFlag'):
			from .PadFlag import PadFlag
			self._padFlag = PadFlag(self._core, self._cmd_group)
		return self._padFlag

	@property
	def rate(self):
		"""rate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rate'):
			from .Rate import Rate
			self._rate = Rate(self._core, self._cmd_group)
		return self._rate

	@property
	def staFlag(self):
		"""staFlag commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_staFlag'):
			from .StaFlag import StaFlag
			self._staFlag = StaFlag(self._core, self._cmd_group)
		return self._staFlag

	@property
	def til(self):
		"""til commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_til'):
			from .Til import Til
			self._til = Til(self._core, self._cmd_group)
		return self._til

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePy
			self._typePy = TypePy(self._core, self._cmd_group)
		return self._typePy

	@property
	def useful(self):
		"""useful commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_useful'):
			from .Useful import Useful
			self._useful = Useful(self._core, self._cmd_group)
		return self._useful

	def clone(self) -> 'Plp':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Plp(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
