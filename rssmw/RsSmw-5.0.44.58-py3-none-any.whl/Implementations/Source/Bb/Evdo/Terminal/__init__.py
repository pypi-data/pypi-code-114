from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Terminal:
	"""Terminal commands group definition. 52 total commands, 15 Subgroups, 0 group commands
	Repeated Capability: Terminal, default value after init: Terminal.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("terminal", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_terminal_get', 'repcap_terminal_set', repcap.Terminal.Nr1)

	def repcap_terminal_set(self, terminal: repcap.Terminal) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Terminal.Default
		Default value after init: Terminal.Nr1"""
		self._cmd_group.set_repcap_enum_value(terminal)

	def repcap_terminal_get(self) -> repcap.Terminal:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def ackChannel(self):
		"""ackChannel commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_ackChannel'):
			from .AckChannel import AckChannel
			self._ackChannel = AckChannel(self._core, self._cmd_group)
		return self._ackChannel

	@property
	def acycle(self):
		"""acycle commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_acycle'):
			from .Acycle import Acycle
			self._acycle = Acycle(self._core, self._cmd_group)
		return self._acycle

	@property
	def apChannel(self):
		"""apChannel commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_apChannel'):
			from .ApChannel import ApChannel
			self._apChannel = ApChannel(self._core, self._cmd_group)
		return self._apChannel

	@property
	def dchannel(self):
		"""dchannel commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_dchannel'):
			from .Dchannel import Dchannel
			self._dchannel = Dchannel(self._core, self._cmd_group)
		return self._dchannel

	@property
	def dqSpreading(self):
		"""dqSpreading commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dqSpreading'):
			from .DqSpreading import DqSpreading
			self._dqSpreading = DqSpreading(self._core, self._cmd_group)
		return self._dqSpreading

	@property
	def drcChannel(self):
		"""drcChannel commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_drcChannel'):
			from .DrcChannel import DrcChannel
			self._drcChannel = DrcChannel(self._core, self._cmd_group)
		return self._drcChannel

	@property
	def dscChannel(self):
		"""dscChannel commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_dscChannel'):
			from .DscChannel import DscChannel
			self._dscChannel = DscChannel(self._core, self._cmd_group)
		return self._dscChannel

	@property
	def imask(self):
		"""imask commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_imask'):
			from .Imask import Imask
			self._imask = Imask(self._core, self._cmd_group)
		return self._imask

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def pchannel(self):
		"""pchannel commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pchannel'):
			from .Pchannel import Pchannel
			self._pchannel = Pchannel(self._core, self._cmd_group)
		return self._pchannel

	@property
	def plength(self):
		"""plength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_plength'):
			from .Plength import Plength
			self._plength = Plength(self._core, self._cmd_group)
		return self._plength

	@property
	def qmask(self):
		"""qmask commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_qmask'):
			from .Qmask import Qmask
			self._qmask = Qmask(self._core, self._cmd_group)
		return self._qmask

	@property
	def rriChannel(self):
		"""rriChannel commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rriChannel'):
			from .RriChannel import RriChannel
			self._rriChannel = RriChannel(self._core, self._cmd_group)
		return self._rriChannel

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def subType(self):
		"""subType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_subType'):
			from .SubType import SubType
			self._subType = SubType(self._core, self._cmd_group)
		return self._subType

	def clone(self) -> 'Terminal':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Terminal(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
