from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gt:
	"""Gt commands group definition. 49 total commands, 30 Subgroups, 0 group commands
	Repeated Capability: GroupNull, default value after init: GroupNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gt", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_groupNull_get', 'repcap_groupNull_set', repcap.GroupNull.Nr0)

	def repcap_groupNull_set(self, groupNull: repcap.GroupNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to GroupNull.Default
		Default value after init: GroupNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(groupNull)

	def repcap_groupNull_get(self) -> repcap.GroupNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def abFlag(self):
		"""abFlag commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_abFlag'):
			from .AbFlag import AbFlag
			self._abFlag = AbFlag(self._core, self._cmd_group)
		return self._abFlag

	@property
	def afon(self):
		"""afon commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_afon'):
			from .Afon import Afon
			self._afon = Afon(self._core, self._cmd_group)
		return self._afon

	@property
	def altf(self):
		"""altf commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_altf'):
			from .Altf import Altf
			self._altf = Altf(self._core, self._cmd_group)
		return self._altf

	@property
	def date(self):
		"""date commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_date'):
			from .Date import Date
			self._date = Date(self._core, self._cmd_group)
		return self._date

	@property
	def did(self):
		"""did commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_did'):
			from .Did import Did
			self._did = Did(self._core, self._cmd_group)
		return self._did

	@property
	def inpMethod(self):
		"""inpMethod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_inpMethod'):
			from .InpMethod import InpMethod
			self._inpMethod = InpMethod(self._core, self._cmd_group)
		return self._inpMethod

	@property
	def lion(self):
		"""lion commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_lion'):
			from .Lion import Lion
			self._lion = Lion(self._core, self._cmd_group)
		return self._lion

	@property
	def loTime(self):
		"""loTime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_loTime'):
			from .LoTime import LoTime
			self._loTime = LoTime(self._core, self._cmd_group)
		return self._loTime

	@property
	def mfl(self):
		"""mfl commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mfl'):
			from .Mfl import Mfl
			self._mfl = Mfl(self._core, self._cmd_group)
		return self._mfl

	@property
	def mvSwitch(self):
		"""mvSwitch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mvSwitch'):
			from .MvSwitch import MvSwitch
			self._mvSwitch = MvSwitch(self._core, self._cmd_group)
		return self._mvSwitch

	@property
	def pinon(self):
		"""pinon commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pinon'):
			from .Pinon import Pinon
			self._pinon = Pinon(self._core, self._cmd_group)
		return self._pinon

	@property
	def pion(self):
		"""pion commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pion'):
			from .Pion import Pion
			self._pion = Pion(self._core, self._cmd_group)
		return self._pion

	@property
	def psName(self):
		"""psName commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_psName'):
			from .PsName import PsName
			self._psName = PsName(self._core, self._cmd_group)
		return self._psName

	@property
	def pson(self):
		"""pson commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pson'):
			from .Pson import Pson
			self._pson = Pson(self._core, self._cmd_group)
		return self._pson

	@property
	def ptName(self):
		"""ptName commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ptName'):
			from .PtName import PtName
			self._ptName = PtName(self._core, self._cmd_group)
		return self._ptName

	@property
	def ptyta(self):
		"""ptyta commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ptyta'):
			from .Ptyta import Ptyta
			self._ptyta = Ptyta(self._core, self._cmd_group)
		return self._ptyta

	@property
	def radText(self):
		"""radText commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_radText'):
			from .RadText import RadText
			self._radText = RadText(self._core, self._cmd_group)
		return self._radText

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def sysDate(self):
		"""sysDate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sysDate'):
			from .SysDate import SysDate
			self._sysDate = SysDate(self._core, self._cmd_group)
		return self._sysDate

	@property
	def sysTime(self):
		"""sysTime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sysTime'):
			from .SysTime import SysTime
			self._sysTime = SysTime(self._core, self._cmd_group)
		return self._sysTime

	@property
	def ta(self):
		"""ta commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ta'):
			from .Ta import Ta
			self._ta = Ta(self._core, self._cmd_group)
		return self._ta

	@property
	def tabFlag(self):
		"""tabFlag commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tabFlag'):
			from .TabFlag import TabFlag
			self._tabFlag = TabFlag(self._core, self._cmd_group)
		return self._tabFlag

	@property
	def taon(self):
		"""taon commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_taon'):
			from .Taon import Taon
			self._taon = Taon(self._core, self._cmd_group)
		return self._taon

	@property
	def time(self):
		"""time commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_time'):
			from .Time import Time
			self._time = Time(self._core, self._cmd_group)
		return self._time

	@property
	def tpon(self):
		"""tpon commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpon'):
			from .Tpon import Tpon
			self._tpon = Tpon(self._core, self._cmd_group)
		return self._tpon

	@property
	def ttime(self):
		"""ttime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ttime'):
			from .Ttime import Ttime
			self._ttime = Ttime(self._core, self._cmd_group)
		return self._ttime

	@property
	def umt(self):
		"""umt commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_umt'):
			from .Umt import Umt
			self._umt = Umt(self._core, self._cmd_group)
		return self._umt

	@property
	def usrDate(self):
		"""usrDate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_usrDate'):
			from .UsrDate import UsrDate
			self._usrDate = UsrDate(self._core, self._cmd_group)
		return self._usrDate

	@property
	def usrTime(self):
		"""usrTime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_usrTime'):
			from .UsrTime import UsrTime
			self._usrTime = UsrTime(self._core, self._cmd_group)
		return self._usrTime

	@property
	def version(self):
		"""version commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_version'):
			from .Version import Version
			self._version = Version(self._core, self._cmd_group)
		return self._version

	def clone(self) -> 'Gt':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Gt(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
