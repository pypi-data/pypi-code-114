from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fblock:
	"""Fblock commands group definition. 231 total commands, 67 Subgroups, 2 group commands
	Repeated Capability: FrameBlock, default value after init: FrameBlock.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fblock", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_frameBlock_get', 'repcap_frameBlock_set', repcap.FrameBlock.Nr1)

	def repcap_frameBlock_set(self, frameBlock: repcap.FrameBlock) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to FrameBlock.Default
		Default value after init: FrameBlock.Nr1"""
		self._cmd_group.set_repcap_enum_value(frameBlock)

	def repcap_frameBlock_get(self) -> repcap.FrameBlock:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def append(self):
		"""append commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_append'):
			from .Append import Append
			self._append = Append(self._core, self._cmd_group)
		return self._append

	@property
	def bchg(self):
		"""bchg commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bchg'):
			from .Bchg import Bchg
			self._bchg = Bchg(self._core, self._cmd_group)
		return self._bchg

	@property
	def bcSmoothing(self):
		"""bcSmoothing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bcSmoothing'):
			from .BcSmoothing import BcSmoothing
			self._bcSmoothing = BcSmoothing(self._core, self._cmd_group)
		return self._bcSmoothing

	@property
	def bdcm(self):
		"""bdcm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bdcm'):
			from .Bdcm import Bdcm
			self._bdcm = Bdcm(self._core, self._cmd_group)
		return self._bdcm

	@property
	def beul(self):
		"""beul commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_beul'):
			from .Beul import Beul
			self._beul = Beul(self._core, self._cmd_group)
		return self._beul

	@property
	def bfConfiguration(self):
		"""bfConfiguration commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_bfConfiguration'):
			from .BfConfiguration import BfConfiguration
			self._bfConfiguration = BfConfiguration(self._core, self._cmd_group)
		return self._bfConfiguration

	@property
	def bmcs(self):
		"""bmcs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bmcs'):
			from .Bmcs import Bmcs
			self._bmcs = Bmcs(self._core, self._cmd_group)
		return self._bmcs

	@property
	def boost(self):
		"""boost commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_boost'):
			from .Boost import Boost
			self._boost = Boost(self._core, self._cmd_group)
		return self._boost

	@property
	def bssColor(self):
		"""bssColor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bssColor'):
			from .BssColor import BssColor
			self._bssColor = BssColor(self._core, self._cmd_group)
		return self._bssColor

	@property
	def cbiNonht(self):
		"""cbiNonht commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbiNonht'):
			from .CbiNonht import CbiNonht
			self._cbiNonht = CbiNonht(self._core, self._cmd_group)
		return self._cbiNonht

	@property
	def cch1(self):
		"""cch1 commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cch1'):
			from .Cch1 import Cch1
			self._cch1 = Cch1(self._core, self._cmd_group)
		return self._cch1

	@property
	def cch2(self):
		"""cch2 commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cch2'):
			from .Cch2 import Cch2
			self._cch2 = Cch2(self._core, self._cmd_group)
		return self._cch2

	@property
	def cenru(self):
		"""cenru commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cenru'):
			from .Cenru import Cenru
			self._cenru = Cenru(self._core, self._cmd_group)
		return self._cenru

	@property
	def color(self):
		"""color commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_color'):
			from .Color import Color
			self._color = Color(self._core, self._cmd_group)
		return self._color

	@property
	def curpe(self):
		"""curpe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_curpe'):
			from .Curpe import Curpe
			self._curpe = Curpe(self._core, self._cmd_group)
		return self._curpe

	@property
	def data(self):
		"""data commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def dbinonht(self):
		"""dbinonht commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dbinonht'):
			from .Dbinonht import Dbinonht
			self._dbinonht = Dbinonht(self._core, self._cmd_group)
		return self._dbinonht

	@property
	def doppler(self):
		"""doppler commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_doppler'):
			from .Doppler import Doppler
			self._doppler = Doppler(self._core, self._cmd_group)
		return self._doppler

	@property
	def emcs(self):
		"""emcs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_emcs'):
			from .Emcs import Emcs
			self._emcs = Emcs(self._core, self._cmd_group)
		return self._emcs

	@property
	def esDiffer(self):
		"""esDiffer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_esDiffer'):
			from .EsDiffer import EsDiffer
			self._esDiffer = EsDiffer(self._core, self._cmd_group)
		return self._esDiffer

	@property
	def esStream(self):
		"""esStream commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_esStream'):
			from .EsStream import EsStream
			self._esStream = EsStream(self._core, self._cmd_group)
		return self._esStream

	@property
	def fcount(self):
		"""fcount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fcount'):
			from .Fcount import Fcount
			self._fcount = Fcount(self._core, self._cmd_group)
		return self._fcount

	@property
	def guard(self):
		"""guard commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_guard'):
			from .Guard import Guard
			self._guard = Guard(self._core, self._cmd_group)
		return self._guard

	@property
	def insert(self):
		"""insert commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_insert'):
			from .Insert import Insert
			self._insert = Insert(self._core, self._cmd_group)
		return self._insert

	@property
	def itime(self):
		"""itime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_itime'):
			from .Itime import Itime
			self._itime = Itime(self._core, self._cmd_group)
		return self._itime

	@property
	def link(self):
		"""link commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_link'):
			from .Link import Link
			self._link = Link(self._core, self._cmd_group)
		return self._link

	@property
	def logFile(self):
		"""logFile commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_logFile'):
			from .LogFile import LogFile
			self._logFile = LogFile(self._core, self._cmd_group)
		return self._logFile

	@property
	def logging(self):
		"""logging commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_logging'):
			from .Logging import Logging
			self._logging = Logging(self._core, self._cmd_group)
		return self._logging

	@property
	def mac(self):
		"""mac commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_mac'):
			from .Mac import Mac
			self._mac = Mac(self._core, self._cmd_group)
		return self._mac

	@property
	def maxPe(self):
		"""maxPe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maxPe'):
			from .MaxPe import MaxPe
			self._maxPe = MaxPe(self._core, self._cmd_group)
		return self._maxPe

	@property
	def mu(self):
		"""mu commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_mu'):
			from .Mu import Mu
			self._mu = Mu(self._core, self._cmd_group)
		return self._mu

	@property
	def muMimo(self):
		"""muMimo commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_muMimo'):
			from .MuMimo import MuMimo
			self._muMimo = MuMimo(self._core, self._cmd_group)
		return self._muMimo

	@property
	def nonOfdmaUser(self):
		"""nonOfdmaUser commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nonOfdmaUser'):
			from .NonOfdmaUser import NonOfdmaUser
			self._nonOfdmaUser = NonOfdmaUser(self._core, self._cmd_group)
		return self._nonOfdmaUser

	@property
	def ntps(self):
		"""ntps commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ntps'):
			from .Ntps import Ntps
			self._ntps = Ntps(self._core, self._cmd_group)
		return self._ntps

	@property
	def paid(self):
		"""paid commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_paid'):
			from .Paid import Paid
			self._paid = Paid(self._core, self._cmd_group)
		return self._paid

	@property
	def paste(self):
		"""paste commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_paste'):
			from .Paste import Paste
			self._paste = Paste(self._core, self._cmd_group)
		return self._paste

	@property
	def ped(self):
		"""ped commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ped'):
			from .Ped import Ped
			self._ped = Ped(self._core, self._cmd_group)
		return self._ped

	@property
	def pformat(self):
		"""pformat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pformat'):
			from .Pformat import Pformat
			self._pformat = Pformat(self._core, self._cmd_group)
		return self._pformat

	@property
	def pfpFactor(self):
		"""pfpFactor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pfpFactor'):
			from .PfpFactor import PfpFactor
			self._pfpFactor = PfpFactor(self._core, self._cmd_group)
		return self._pfpFactor

	@property
	def piType(self):
		"""piType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_piType'):
			from .PiType import PiType
			self._piType = PiType(self._core, self._cmd_group)
		return self._piType

	@property
	def plcp(self):
		"""plcp commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_plcp'):
			from .Plcp import Plcp
			self._plcp = Plcp(self._core, self._cmd_group)
		return self._plcp

	@property
	def pmode(self):
		"""pmode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmode'):
			from .Pmode import Pmode
			self._pmode = Pmode(self._core, self._cmd_group)
		return self._pmode

	@property
	def pofdma(self):
		"""pofdma commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pofdma'):
			from .Pofdma import Pofdma
			self._pofdma = Pofdma(self._core, self._cmd_group)
		return self._pofdma

	@property
	def ppuncturing(self):
		"""ppuncturing commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ppuncturing'):
			from .Ppuncturing import Ppuncturing
			self._ppuncturing = Ppuncturing(self._core, self._cmd_group)
		return self._ppuncturing

	@property
	def preamble(self):
		"""preamble commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_preamble'):
			from .Preamble import Preamble
			self._preamble = Preamble(self._core, self._cmd_group)
		return self._preamble

	@property
	def prtype(self):
		"""prtype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prtype'):
			from .Prtype import Prtype
			self._prtype = Prtype(self._core, self._cmd_group)
		return self._prtype

	@property
	def psdu(self):
		"""psdu commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_psdu'):
			from .Psdu import Psdu
			self._psdu = Psdu(self._core, self._cmd_group)
		return self._psdu

	@property
	def right106Tone(self):
		"""right106Tone commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_right106Tone'):
			from .Right106Tone import Right106Tone
			self._right106Tone = Right106Tone(self._core, self._cmd_group)
		return self._right106Tone

	@property
	def segment(self):
		"""segment commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_segment'):
			from .Segment import Segment
			self._segment = Segment(self._core, self._cmd_group)
		return self._segment

	@property
	def smapping(self):
		"""smapping commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_smapping'):
			from .Smapping import Smapping
			self._smapping = Smapping(self._core, self._cmd_group)
		return self._smapping

	@property
	def smoothing(self):
		"""smoothing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_smoothing'):
			from .Smoothing import Smoothing
			self._smoothing = Smoothing(self._core, self._cmd_group)
		return self._smoothing

	@property
	def spareUse(self):
		"""spareUse commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spareUse'):
			from .SpareUse import SpareUse
			self._spareUse = SpareUse(self._core, self._cmd_group)
		return self._spareUse

	@property
	def sstream(self):
		"""sstream commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sstream'):
			from .Sstream import Sstream
			self._sstream = Sstream(self._core, self._cmd_group)
		return self._sstream

	@property
	def standard(self):
		"""standard commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_standard'):
			from .Standard import Standard
			self._standard = Standard(self._core, self._cmd_group)
		return self._standard

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def stbc(self):
		"""stbc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_stbc'):
			from .Stbc import Stbc
			self._stbc = Stbc(self._core, self._cmd_group)
		return self._stbc

	@property
	def stStream(self):
		"""stStream commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stStream'):
			from .StStream import StStream
			self._stStream = StStream(self._core, self._cmd_group)
		return self._stStream

	@property
	def symDuration(self):
		"""symDuration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symDuration'):
			from .SymDuration import SymDuration
			self._symDuration = SymDuration(self._core, self._cmd_group)
		return self._symDuration

	@property
	def tdWindowing(self):
		"""tdWindowing commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tdWindowing'):
			from .TdWindowing import TdWindowing
			self._tdWindowing = TdWindowing(self._core, self._cmd_group)
		return self._tdWindowing

	@property
	def tmode(self):
		"""tmode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tmode'):
			from .Tmode import Tmode
			self._tmode = Tmode(self._core, self._cmd_group)
		return self._tmode

	@property
	def ttime(self):
		"""ttime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ttime'):
			from .Ttime import Ttime
			self._ttime = Ttime(self._core, self._cmd_group)
		return self._ttime

	@property
	def txopDuration(self):
		"""txopDuration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txopDuration'):
			from .TxopDuration import TxopDuration
			self._txopDuration = TxopDuration(self._core, self._cmd_group)
		return self._txopDuration

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePy
			self._typePy = TypePy(self._core, self._cmd_group)
		return self._typePy

	@property
	def uindex(self):
		"""uindex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uindex'):
			from .Uindex import Uindex
			self._uindex = Uindex(self._core, self._cmd_group)
		return self._uindex

	@property
	def uindication(self):
		"""uindication commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uindication'):
			from .Uindication import Uindication
			self._uindication = Uindication(self._core, self._cmd_group)
		return self._uindication

	@property
	def ulen(self):
		"""ulen commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ulen'):
			from .Ulen import Ulen
			self._ulen = Ulen(self._core, self._cmd_group)
		return self._ulen

	@property
	def user(self):
		"""user commands group. 21 Sub-classes, 0 commands."""
		if not hasattr(self, '_user'):
			from .User import User
			self._user = User(self._core, self._cmd_group)
		return self._user

	def copy(self, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:COPY \n
		Snippet: driver.source.bb.wlnn.fblock.copy(frameBlock = repcap.FrameBlock.Default) \n
		Copies the selected frame block. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:COPY')

	def copy_with_opc(self, frameBlock=repcap.FrameBlock.Default, opc_timeout_ms: int = -1) -> None:
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:COPY \n
		Snippet: driver.source.bb.wlnn.fblock.copy_with_opc(frameBlock = repcap.FrameBlock.Default) \n
		Copies the selected frame block. \n
		Same as copy, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:COPY', opc_timeout_ms)

	def delete(self, frameBlock=repcap.FrameBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:DELete \n
		Snippet: driver.source.bb.wlnn.fblock.delete(frameBlock = repcap.FrameBlock.Default) \n
		Deletes the selected frame block. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
		"""
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:DELete')

	def delete_with_opc(self, frameBlock=repcap.FrameBlock.Default, opc_timeout_ms: int = -1) -> None:
		frameBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(frameBlock, repcap.FrameBlock)
		"""SCPI: [SOURce<HW>]:BB:WLNN:FBLock<CH>:DELete \n
		Snippet: driver.source.bb.wlnn.fblock.delete_with_opc(frameBlock = repcap.FrameBlock.Default) \n
		Deletes the selected frame block. \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param frameBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fblock')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:WLNN:FBLock{frameBlock_cmd_val}:DELete', opc_timeout_ms)

	def clone(self) -> 'Fblock':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fblock(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
