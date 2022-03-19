from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sci:
	"""Sci commands group definition. 19 total commands, 19 Subgroups, 0 group commands
	Repeated Capability: IndexNull, default value after init: IndexNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sci", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_indexNull_get', 'repcap_indexNull_set', repcap.IndexNull.Nr0)

	def repcap_indexNull_set(self, indexNull: repcap.IndexNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to IndexNull.Default
		Default value after init: IndexNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(indexNull)

	def repcap_indexNull_get(self) -> repcap.IndexNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def bitData(self):
		"""bitData commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bitData'):
			from .BitData import BitData
			self._bitData = BitData(self._core, self._cmd_group)
		return self._bitData

	@property
	def fhFlag(self):
		"""fhFlag commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fhFlag'):
			from .FhFlag import FhFlag
			self._fhFlag = FhFlag(self._core, self._cmd_group)
		return self._fhFlag

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPy
			self._formatPy = FormatPy(self._core, self._cmd_group)
		return self._formatPy

	@property
	def freqResloc(self):
		"""freqResloc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_freqResloc'):
			from .FreqResloc import FreqResloc
			self._freqResloc = FreqResloc(self._core, self._cmd_group)
		return self._freqResloc

	@property
	def grid(self):
		"""grid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_grid'):
			from .Grid import Grid
			self._grid = Grid(self._core, self._cmd_group)
		return self._grid

	@property
	def mcs(self):
		"""mcs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcs'):
			from .Mcs import Mcs
			self._mcs = Mcs(self._core, self._cmd_group)
		return self._mcs

	@property
	def npscch(self):
		"""npscch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_npscch'):
			from .Npscch import Npscch
			self._npscch = Npscch(self._core, self._cmd_group)
		return self._npscch

	@property
	def pririty(self):
		"""pririty commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pririty'):
			from .Pririty import Pririty
			self._pririty = Pririty(self._core, self._cmd_group)
		return self._pririty

	@property
	def pscPeriod(self):
		"""pscPeriod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pscPeriod'):
			from .PscPeriod import PscPeriod
			self._pscPeriod = PscPeriod(self._core, self._cmd_group)
		return self._pscPeriod

	@property
	def rbahoppAlloc(self):
		"""rbahoppAlloc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbahoppAlloc'):
			from .RbahoppAlloc import RbahoppAlloc
			self._rbahoppAlloc = RbahoppAlloc(self._core, self._cmd_group)
		return self._rbahoppAlloc

	@property
	def rreservation(self):
		"""rreservation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rreservation'):
			from .Rreservation import Rreservation
			self._rreservation = Rreservation(self._core, self._cmd_group)
		return self._rreservation

	@property
	def sf(self):
		"""sf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sf'):
			from .Sf import Sf
			self._sf = Sf(self._core, self._cmd_group)
		return self._sf

	@property
	def startSf(self):
		"""startSf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_startSf'):
			from .StartSf import StartSf
			self._startSf = StartSf(self._core, self._cmd_group)
		return self._startSf

	@property
	def subChannel(self):
		"""subChannel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_subChannel'):
			from .SubChannel import SubChannel
			self._subChannel = SubChannel(self._core, self._cmd_group)
		return self._subChannel

	@property
	def taInd(self):
		"""taInd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_taInd'):
			from .TaInd import TaInd
			self._taInd = TaInd(self._core, self._cmd_group)
		return self._taInd

	@property
	def timGap(self):
		"""timGap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_timGap'):
			from .TimGap import TimGap
			self._timGap = TimGap(self._core, self._cmd_group)
		return self._timGap

	@property
	def trp(self):
		"""trp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trp'):
			from .Trp import Trp
			self._trp = Trp(self._core, self._cmd_group)
		return self._trp

	@property
	def txIndex(self):
		"""txIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txIndex'):
			from .TxIndex import TxIndex
			self._txIndex = TxIndex(self._core, self._cmd_group)
		return self._txIndex

	@property
	def txMode(self):
		"""txMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txMode'):
			from .TxMode import TxMode
			self._txMode = TxMode(self._core, self._cmd_group)
		return self._txMode

	def clone(self) -> 'Sci':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sci(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
