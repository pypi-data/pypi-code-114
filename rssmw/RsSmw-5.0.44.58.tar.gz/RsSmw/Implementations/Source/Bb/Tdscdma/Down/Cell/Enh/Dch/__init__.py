from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dch:
	"""Dch commands group definition. 88 total commands, 17 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dch", core, parent)

	@property
	def bit(self):
		"""bit commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_bit'):
			from .Bit import Bit
			self._bit = Bit(self._core, self._cmd_group)
		return self._bit

	@property
	def block(self):
		"""block commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_block'):
			from .Block import Block
			self._block = Block(self._core, self._cmd_group)
		return self._block

	@property
	def bpFrame(self):
		"""bpFrame commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bpFrame'):
			from .BpFrame import BpFrame
			self._bpFrame = BpFrame(self._core, self._cmd_group)
		return self._bpFrame

	@property
	def ccount(self):
		"""ccount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ccount'):
			from .Ccount import Ccount
			self._ccount = Ccount(self._core, self._cmd_group)
		return self._ccount

	@property
	def dcch(self):
		"""dcch commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_dcch'):
			from .Dcch import Dcch
			self._dcch = Dcch(self._core, self._cmd_group)
		return self._dcch

	@property
	def dtch(self):
		"""dtch commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_dtch'):
			from .Dtch import Dtch
			self._dtch = Dtch(self._core, self._cmd_group)
		return self._dtch

	@property
	def hsch(self):
		"""hsch commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_hsch'):
			from .Hsch import Hsch
			self._hsch = Hsch(self._core, self._cmd_group)
		return self._hsch

	@property
	def hsdpa(self):
		"""hsdpa commands group. 21 Sub-classes, 0 commands."""
		if not hasattr(self, '_hsdpa'):
			from .Hsdpa import Hsdpa
			self._hsdpa = Hsdpa(self._core, self._cmd_group)
		return self._hsdpa

	@property
	def hsupa(self):
		"""hsupa commands group. 15 Sub-classes, 0 commands."""
		if not hasattr(self, '_hsupa'):
			from .Hsupa import Hsupa
			self._hsupa = Hsupa(self._core, self._cmd_group)
		return self._hsupa

	@property
	def plcch(self):
		"""plcch commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_plcch'):
			from .Plcch import Plcch
			self._plcch = Plcch(self._core, self._cmd_group)
		return self._plcch

	@property
	def rupLayer(self):
		"""rupLayer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rupLayer'):
			from .RupLayer import RupLayer
			self._rupLayer = RupLayer(self._core, self._cmd_group)
		return self._rupLayer

	@property
	def scsMode(self):
		"""scsMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scsMode'):
			from .ScsMode import ScsMode
			self._scsMode = ScsMode(self._core, self._cmd_group)
		return self._scsMode

	@property
	def sformat(self):
		"""sformat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sformat'):
			from .Sformat import Sformat
			self._sformat = Sformat(self._core, self._cmd_group)
		return self._sformat

	@property
	def slotState(self):
		"""slotState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slotState'):
			from .SlotState import SlotState
			self._slotState = SlotState(self._core, self._cmd_group)
		return self._slotState

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def tsCount(self):
		"""tsCount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tsCount'):
			from .TsCount import TsCount
			self._tsCount = TsCount(self._core, self._cmd_group)
		return self._tsCount

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePy
			self._typePy = TypePy(self._core, self._cmd_group)
		return self._typePy

	def clone(self) -> 'Dch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
