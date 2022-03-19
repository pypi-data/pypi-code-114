from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cinfo:
	"""Cinfo commands group definition. 17 total commands, 17 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cinfo", core, parent)

	@property
	def bw(self):
		"""bw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bw'):
			from .Bw import Bw
			self._bw = Bw(self._core, self._cmd_group)
		return self._bw

	@property
	def cindication(self):
		"""cindication commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cindication'):
			from .Cindication import Cindication
			self._cindication = Cindication(self._core, self._cmd_group)
		return self._cindication

	@property
	def csRequired(self):
		"""csRequired commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csRequired'):
			from .CsRequired import CsRequired
			self._csRequired = CsRequired(self._core, self._cmd_group)
		return self._csRequired

	@property
	def doppler(self):
		"""doppler commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_doppler'):
			from .Doppler import Doppler
			self._doppler = Doppler(self._core, self._cmd_group)
		return self._doppler

	@property
	def giltf(self):
		"""giltf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_giltf'):
			from .Giltf import Giltf
			self._giltf = Giltf(self._core, self._cmd_group)
		return self._giltf

	@property
	def hreserved(self):
		"""hreserved commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hreserved'):
			from .Hreserved import Hreserved
			self._hreserved = Hreserved(self._core, self._cmd_group)
		return self._hreserved

	@property
	def len(self):
		"""len commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_len'):
			from .Len import Len
			self._len = Len(self._core, self._cmd_group)
		return self._len

	@property
	def lesSeg(self):
		"""lesSeg commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lesSeg'):
			from .LesSeg import LesSeg
			self._lesSeg = LesSeg(self._core, self._cmd_group)
		return self._lesSeg

	@property
	def mltfMode(self):
		"""mltfMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mltfMode'):
			from .MltfMode import MltfMode
			self._mltfMode = MltfMode(self._core, self._cmd_group)
		return self._mltfMode

	@property
	def nhlSym(self):
		"""nhlSym commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nhlSym'):
			from .NhlSym import NhlSym
			self._nhlSym = NhlSym(self._core, self._cmd_group)
		return self._nhlSym

	@property
	def pextension(self):
		"""pextension commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pextension'):
			from .Pextension import Pextension
			self._pextension = Pextension(self._core, self._cmd_group)
		return self._pextension

	@property
	def rsv(self):
		"""rsv commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rsv'):
			from .Rsv import Rsv
			self._rsv = Rsv(self._core, self._cmd_group)
		return self._rsv

	@property
	def spareUse(self):
		"""spareUse commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spareUse'):
			from .SpareUse import SpareUse
			self._spareUse = SpareUse(self._core, self._cmd_group)
		return self._spareUse

	@property
	def stbc(self):
		"""stbc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stbc'):
			from .Stbc import Stbc
			self._stbc = Stbc(self._core, self._cmd_group)
		return self._stbc

	@property
	def tfType(self):
		"""tfType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tfType'):
			from .TfType import TfType
			self._tfType = TfType(self._core, self._cmd_group)
		return self._tfType

	@property
	def ttype(self):
		"""ttype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ttype'):
			from .Ttype import Ttype
			self._ttype = Ttype(self._core, self._cmd_group)
		return self._ttype

	@property
	def txpow(self):
		"""txpow commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txpow'):
			from .Txpow import Txpow
			self._txpow = Txpow(self._core, self._cmd_group)
		return self._txpow

	def clone(self) -> 'Cinfo':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cinfo(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
