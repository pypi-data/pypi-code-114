from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ue:
	"""Ue commands group definition. 273 total commands, 17 Subgroups, 0 group commands
	Repeated Capability: UserEquipment, default value after init: UserEquipment.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ue", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_userEquipment_get', 'repcap_userEquipment_set', repcap.UserEquipment.Nr1)

	def repcap_userEquipment_set(self, userEquipment: repcap.UserEquipment) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to UserEquipment.Default
		Default value after init: UserEquipment.Nr1"""
		self._cmd_group.set_repcap_enum_value(userEquipment)

	def repcap_userEquipment_get(self) -> repcap.UserEquipment:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def aapto(self):
		"""aapto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aapto'):
			from .Aapto import Aapto
			self._aapto = Aapto(self._core, self._cmd_group)
		return self._aapto

	@property
	def apMap(self):
		"""apMap commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_apMap'):
			from .ApMap import ApMap
			self._apMap = ApMap(self._core, self._cmd_group)
		return self._apMap

	@property
	def cell(self):
		"""cell commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_cell'):
			from .Cell import Cell
			self._cell = Cell(self._core, self._cmd_group)
		return self._cell

	@property
	def cid(self):
		"""cid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cid'):
			from .Cid import Cid
			self._cid = Cid(self._core, self._cmd_group)
		return self._cid

	@property
	def conSubFrames(self):
		"""conSubFrames commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_conSubFrames'):
			from .ConSubFrames import ConSubFrames
			self._conSubFrames = ConSubFrames(self._core, self._cmd_group)
		return self._conSubFrames

	@property
	def dacRestart(self):
		"""dacRestart commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dacRestart'):
			from .DacRestart import DacRestart
			self._dacRestart = DacRestart(self._core, self._cmd_group)
		return self._dacRestart

	@property
	def emtc(self):
		"""emtc commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_emtc'):
			from .Emtc import Emtc
			self._emtc = Emtc(self._core, self._cmd_group)
		return self._emtc

	@property
	def id(self):
		"""id commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_id'):
			from .Id import Id
			self._id = Id(self._core, self._cmd_group)
		return self._id

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def niot(self):
		"""niot commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_niot'):
			from .Niot import Niot
			self._niot = Niot(self._core, self._cmd_group)
		return self._niot

	@property
	def ocid(self):
		"""ocid commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ocid'):
			from .Ocid import Ocid
			self._ocid = Ocid(self._core, self._cmd_group)
		return self._ocid

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def prach(self):
		"""prach commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_prach'):
			from .Prach import Prach
			self._prach = Prach(self._core, self._cmd_group)
		return self._prach

	@property
	def pucch(self):
		"""pucch commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_pucch'):
			from .Pucch import Pucch
			self._pucch = Pucch(self._core, self._cmd_group)
		return self._pucch

	@property
	def release(self):
		"""release commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_release'):
			from .Release import Release
			self._release = Release(self._core, self._cmd_group)
		return self._release

	@property
	def sl(self):
		"""sl commands group. 16 Sub-classes, 0 commands."""
		if not hasattr(self, '_sl'):
			from .Sl import Sl
			self._sl = Sl(self._core, self._cmd_group)
		return self._sl

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Ue':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ue(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
