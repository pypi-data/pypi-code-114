from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Capability:
	"""Capability commands group definition. 16 total commands, 16 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("capability", core, parent)

	@property
	def apsd(self):
		"""apsd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apsd'):
			from .Apsd import Apsd
			self._apsd = Apsd(self._core, self._cmd_group)
		return self._apsd

	@property
	def cagility(self):
		"""cagility commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cagility'):
			from .Cagility import Cagility
			self._cagility = Cagility(self._core, self._cmd_group)
		return self._cagility

	@property
	def cpollable(self):
		"""cpollable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cpollable'):
			from .Cpollable import Cpollable
			self._cpollable = Cpollable(self._core, self._cmd_group)
		return self._cpollable

	@property
	def cpRequest(self):
		"""cpRequest commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cpRequest'):
			from .CpRequest import CpRequest
			self._cpRequest = CpRequest(self._core, self._cmd_group)
		return self._cpRequest

	@property
	def dback(self):
		"""dback commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dback'):
			from .Dback import Dback
			self._dback = Dback(self._core, self._cmd_group)
		return self._dback

	@property
	def dofdm(self):
		"""dofdm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dofdm'):
			from .Dofdm import Dofdm
			self._dofdm = Dofdm(self._core, self._cmd_group)
		return self._dofdm

	@property
	def ess(self):
		"""ess commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ess'):
			from .Ess import Ess
			self._ess = Ess(self._core, self._cmd_group)
		return self._ess

	@property
	def iback(self):
		"""iback commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iback'):
			from .Iback import Iback
			self._iback = Iback(self._core, self._cmd_group)
		return self._iback

	@property
	def ibss(self):
		"""ibss commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ibss'):
			from .Ibss import Ibss
			self._ibss = Ibss(self._core, self._cmd_group)
		return self._ibss

	@property
	def pbcc(self):
		"""pbcc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pbcc'):
			from .Pbcc import Pbcc
			self._pbcc = Pbcc(self._core, self._cmd_group)
		return self._pbcc

	@property
	def privacy(self):
		"""privacy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_privacy'):
			from .Privacy import Privacy
			self._privacy = Privacy(self._core, self._cmd_group)
		return self._privacy

	@property
	def qos(self):
		"""qos commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_qos'):
			from .Qos import Qos
			self._qos = Qos(self._core, self._cmd_group)
		return self._qos

	@property
	def rmeasurement(self):
		"""rmeasurement commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rmeasurement'):
			from .Rmeasurement import Rmeasurement
			self._rmeasurement = Rmeasurement(self._core, self._cmd_group)
		return self._rmeasurement

	@property
	def smgmt(self):
		"""smgmt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_smgmt'):
			from .Smgmt import Smgmt
			self._smgmt = Smgmt(self._core, self._cmd_group)
		return self._smgmt

	@property
	def spreamble(self):
		"""spreamble commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spreamble'):
			from .Spreamble import Spreamble
			self._spreamble = Spreamble(self._core, self._cmd_group)
		return self._spreamble

	@property
	def ssTime(self):
		"""ssTime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssTime'):
			from .SsTime import SsTime
			self._ssTime = SsTime(self._core, self._cmd_group)
		return self._ssTime

	def clone(self) -> 'Capability':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Capability(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
