from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class User:
	"""User commands group definition. 85 total commands, 21 Subgroups, 0 group commands
	Repeated Capability: UserIx, default value after init: UserIx.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("user", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_userIx_get', 'repcap_userIx_set', repcap.UserIx.Nr1)

	def repcap_userIx_set(self, userIx: repcap.UserIx) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to UserIx.Default
		Default value after init: UserIx.Nr1"""
		self._cmd_group.set_repcap_enum_value(userIx)

	def repcap_userIx_get(self) -> repcap.UserIx:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def dcm(self):
		"""dcm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dcm'):
			from .Dcm import Dcm
			self._dcm = Dcm(self._core, self._cmd_group)
		return self._dcm

	@property
	def gain(self):
		"""gain commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gain'):
			from .Gain import Gain
			self._gain = Gain(self._core, self._cmd_group)
		return self._gain

	@property
	def mruIndex(self):
		"""mruIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mruIndex'):
			from .MruIndex import MruIndex
			self._mruIndex = MruIndex(self._core, self._cmd_group)
		return self._mruIndex

	@property
	def muMimo(self):
		"""muMimo commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_muMimo'):
			from .MuMimo import MuMimo
			self._muMimo = MuMimo(self._core, self._cmd_group)
		return self._muMimo

	@property
	def nsts(self):
		"""nsts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nsts'):
			from .Nsts import Nsts
			self._nsts = Nsts(self._core, self._cmd_group)
		return self._nsts

	@property
	def ruType(self):
		"""ruType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ruType'):
			from .RuType import RuType
			self._ruType = RuType(self._core, self._cmd_group)
		return self._ruType

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def staId(self):
		"""staId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_staId'):
			from .StaId import StaId
			self._staId = StaId(self._core, self._cmd_group)
		return self._staId

	@property
	def txBf(self):
		"""txBf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_txBf'):
			from .TxBf import TxBf
			self._txBf = TxBf(self._core, self._cmd_group)
		return self._txBf

	@property
	def coding(self):
		"""coding commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_coding'):
			from .Coding import Coding
			self._coding = Coding(self._core, self._cmd_group)
		return self._coding

	@property
	def data(self):
		"""data commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def dpnSeed(self):
		"""dpnSeed commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dpnSeed'):
			from .DpnSeed import DpnSeed
			self._dpnSeed = DpnSeed(self._core, self._cmd_group)
		return self._dpnSeed

	@property
	def ileaver(self):
		"""ileaver commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ileaver'):
			from .Ileaver import Ileaver
			self._ileaver = Ileaver(self._core, self._cmd_group)
		return self._ileaver

	@property
	def mac(self):
		"""mac commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_mac'):
			from .Mac import Mac
			self._mac = Mac(self._core, self._cmd_group)
		return self._mac

	@property
	def mcs(self):
		"""mcs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcs'):
			from .Mcs import Mcs
			self._mcs = Mcs(self._core, self._cmd_group)
		return self._mcs

	@property
	def modulation(self):
		"""modulation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import Modulation
			self._modulation = Modulation(self._core, self._cmd_group)
		return self._modulation

	@property
	def mpdu(self):
		"""mpdu commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_mpdu'):
			from .Mpdu import Mpdu
			self._mpdu = Mpdu(self._core, self._cmd_group)
		return self._mpdu

	@property
	def pnSeed(self):
		"""pnSeed commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pnSeed'):
			from .PnSeed import PnSeed
			self._pnSeed = PnSeed(self._core, self._cmd_group)
		return self._pnSeed

	@property
	def scrambler(self):
		"""scrambler commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_scrambler'):
			from .Scrambler import Scrambler
			self._scrambler = Scrambler(self._core, self._cmd_group)
		return self._scrambler

	@property
	def service(self):
		"""service commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_service'):
			from .Service import Service
			self._service = Service(self._core, self._cmd_group)
		return self._service

	@property
	def tfConfig(self):
		"""tfConfig commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tfConfig'):
			from .TfConfig import TfConfig
			self._tfConfig = TfConfig(self._core, self._cmd_group)
		return self._tfConfig

	def clone(self) -> 'User':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = User(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
