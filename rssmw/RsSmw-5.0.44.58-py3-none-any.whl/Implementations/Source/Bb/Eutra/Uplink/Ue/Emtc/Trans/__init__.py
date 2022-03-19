from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trans:
	"""Trans commands group definition. 32 total commands, 23 Subgroups, 0 group commands
	Repeated Capability: Transmission, default value after init: Transmission.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trans", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_transmission_get', 'repcap_transmission_set', repcap.Transmission.Nr1)

	def repcap_transmission_set(self, transmission: repcap.Transmission) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Transmission.Default
		Default value after init: Transmission.Nr1"""
		self._cmd_group.set_repcap_enum_value(transmission)

	def repcap_transmission_get(self) -> repcap.Transmission:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def asFrame(self):
		"""asFrame commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_asFrame'):
			from .AsFrame import AsFrame
			self._asFrame = AsFrame(self._core, self._cmd_group)
		return self._asFrame

	@property
	def ccoding(self):
		"""ccoding commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccoding'):
			from .Ccoding import Ccoding
			self._ccoding = Ccoding(self._core, self._cmd_group)
		return self._ccoding

	@property
	def content(self):
		"""content commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_content'):
			from .Content import Content
			self._content = Content(self._core, self._cmd_group)
		return self._content

	@property
	def drs(self):
		"""drs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_drs'):
			from .Drs import Drs
			self._drs = Drs(self._core, self._cmd_group)
		return self._drs

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPy
			self._formatPy = FormatPy(self._core, self._cmd_group)
		return self._formatPy

	@property
	def harq(self):
		"""harq commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_harq'):
			from .Harq import Harq
			self._harq = Harq(self._core, self._cmd_group)
		return self._harq

	@property
	def modulation(self):
		"""modulation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import Modulation
			self._modulation = Modulation(self._core, self._cmd_group)
		return self._modulation

	@property
	def napUsed(self):
		"""napUsed commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_napUsed'):
			from .NapUsed import NapUsed
			self._napUsed = NapUsed(self._core, self._cmd_group)
		return self._napUsed

	@property
	def ndmrs(self):
		"""ndmrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ndmrs'):
			from .Ndmrs import Ndmrs
			self._ndmrs = Ndmrs(self._core, self._cmd_group)
		return self._ndmrs

	@property
	def npucch(self):
		"""npucch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_npucch'):
			from .Npucch import Npucch
			self._npucch = Npucch(self._core, self._cmd_group)
		return self._npucch

	@property
	def nrBlocks(self):
		"""nrBlocks commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nrBlocks'):
			from .NrBlocks import NrBlocks
			self._nrBlocks = NrBlocks(self._core, self._cmd_group)
		return self._nrBlocks

	@property
	def physBits(self):
		"""physBits commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_physBits'):
			from .PhysBits import PhysBits
			self._physBits = PhysBits(self._core, self._cmd_group)
		return self._physBits

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def pucch(self):
		"""pucch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pucch'):
			from .Pucch import Pucch
			self._pucch = Pucch(self._core, self._cmd_group)
		return self._pucch

	@property
	def pusch(self):
		"""pusch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pusch'):
			from .Pusch import Pusch
			self._pusch = Pusch(self._core, self._cmd_group)
		return self._pusch

	@property
	def rbOffset(self):
		"""rbOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbOffset'):
			from .RbOffset import RbOffset
			self._rbOffset = RbOffset(self._core, self._cmd_group)
		return self._rbOffset

	@property
	def repetitions(self):
		"""repetitions commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_repetitions'):
			from .Repetitions import Repetitions
			self._repetitions = Repetitions(self._core, self._cmd_group)
		return self._repetitions

	@property
	def stnBand(self):
		"""stnBand commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stnBand'):
			from .StnBand import StnBand
			self._stnBand = StnBand(self._core, self._cmd_group)
		return self._stnBand

	@property
	def stsFrame(self):
		"""stsFrame commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stsFrame'):
			from .StsFrame import StsFrame
			self._stsFrame = StsFrame(self._core, self._cmd_group)
		return self._stsFrame

	@property
	def stwBand(self):
		"""stwBand commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stwBand'):
			from .StwBand import StwBand
			self._stwBand = StwBand(self._core, self._cmd_group)
		return self._stwBand

	@property
	def ulsch(self):
		"""ulsch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ulsch'):
			from .Ulsch import Ulsch
			self._ulsch = Ulsch(self._core, self._cmd_group)
		return self._ulsch

	@property
	def wbrbOffset(self):
		"""wbrbOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wbrbOffset'):
			from .WbrbOffset import WbrbOffset
			self._wbrbOffset = WbrbOffset(self._core, self._cmd_group)
		return self._wbrbOffset

	@property
	def wrBlocks(self):
		"""wrBlocks commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wrBlocks'):
			from .WrBlocks import WrBlocks
			self._wrBlocks = WrBlocks(self._core, self._cmd_group)
		return self._wrBlocks

	def clone(self) -> 'Trans':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trans(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
