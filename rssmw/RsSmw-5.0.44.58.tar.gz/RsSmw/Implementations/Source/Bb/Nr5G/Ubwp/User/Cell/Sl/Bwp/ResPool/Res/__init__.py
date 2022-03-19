from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Res:
	"""Res commands group definition. 19 total commands, 19 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("res", core, parent)

	@property
	def amcs(self):
		"""amcs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_amcs'):
			from .Amcs import Amcs
			self._amcs = Amcs(self._core, self._cmd_group)
		return self._amcs

	@property
	def bof1(self):
		"""bof1 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bof1'):
			from .Bof1 import Bof1
			self._bof1 = Bof1(self._core, self._cmd_group)
		return self._bof1

	@property
	def bof2(self):
		"""bof2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bof2'):
			from .Bof2 import Bof2
			self._bof2 = Bof2(self._core, self._cmd_group)
		return self._bof2

	@property
	def bof3(self):
		"""bof3 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bof3'):
			from .Bof3 import Bof3
			self._bof3 = Bof3(self._core, self._cmd_group)
		return self._bof3

	@property
	def bof4(self):
		"""bof4 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bof4'):
			from .Bof4 import Bof4
			self._bof4 = Bof4(self._core, self._cmd_group)
		return self._bof4

	@property
	def indicator(self):
		"""indicator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_indicator'):
			from .Indicator import Indicator
			self._indicator = Indicator(self._core, self._cmd_group)
		return self._indicator

	@property
	def mnPres(self):
		"""mnPres commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mnPres'):
			from .MnPres import MnPres
			self._mnPres = MnPres(self._core, self._cmd_group)
		return self._mnPres

	@property
	def mreserve(self):
		"""mreserve commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mreserve'):
			from .Mreserve import Mreserve
			self._mreserve = Mreserve(self._core, self._cmd_group)
		return self._mreserve

	@property
	def mscTable(self):
		"""mscTable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mscTable'):
			from .MscTable import MscTable
			self._mscTable = MscTable(self._core, self._cmd_group)
		return self._mscTable

	@property
	def nprb(self):
		"""nprb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nprb'):
			from .Nprb import Nprb
			self._nprb = Nprb(self._core, self._cmd_group)
		return self._nprb

	@property
	def nsubChannels(self):
		"""nsubChannels commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nsubChannels'):
			from .NsubChannels import NsubChannels
			self._nsubChannels = NsubChannels(self._core, self._cmd_group)
		return self._nsubChannels

	@property
	def pat2(self):
		"""pat2 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pat2'):
			from .Pat2 import Pat2
			self._pat2 = Pat2(self._core, self._cmd_group)
		return self._pat2

	@property
	def pat3(self):
		"""pat3 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pat3'):
			from .Pat3 import Pat3
			self._pat3 = Pat3(self._core, self._cmd_group)
		return self._pat3

	@property
	def pat4(self):
		"""pat4 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pat4'):
			from .Pat4 import Pat4
			self._pat4 = Pat4(self._core, self._cmd_group)
		return self._pat4

	@property
	def repList(self):
		"""repList commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_repList'):
			from .RepList import RepList
			self._repList = RepList(self._core, self._cmd_group)
		return self._repList

	@property
	def resBits(self):
		"""resBits commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_resBits'):
			from .ResBits import ResBits
			self._resBits = ResBits(self._core, self._cmd_group)
		return self._resBits

	@property
	def scaling(self):
		"""scaling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scaling'):
			from .Scaling import Scaling
			self._scaling = Scaling(self._core, self._cmd_group)
		return self._scaling

	@property
	def schSize(self):
		"""schSize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_schSize'):
			from .SchSize import SchSize
			self._schSize = SchSize(self._core, self._cmd_group)
		return self._schSize

	@property
	def strb(self):
		"""strb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_strb'):
			from .Strb import Strb
			self._strb = Strb(self._core, self._cmd_group)
		return self._strb

	def clone(self) -> 'Res':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Res(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
