from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fader:
	"""Fader commands group definition. 15 total commands, 7 Subgroups, 0 group commands
	Repeated Capability: DigitalIq, default value after init: DigitalIq.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fader", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_digitalIq_get', 'repcap_digitalIq_set', repcap.DigitalIq.Nr1)

	def repcap_digitalIq_set(self, digitalIq: repcap.DigitalIq) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to DigitalIq.Default
		Default value after init: DigitalIq.Nr1"""
		self._cmd_group.set_repcap_enum_value(digitalIq)

	def repcap_digitalIq_get(self) -> repcap.DigitalIq:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def cdevice(self):
		"""cdevice commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cdevice'):
			from .Cdevice import Cdevice
			self._cdevice = Cdevice(self._core, self._cmd_group)
		return self._cdevice

	@property
	def interface(self):
		"""interface commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_interface'):
			from .Interface import Interface
			self._interface = Interface(self._core, self._cmd_group)
		return self._interface

	@property
	def oflow(self):
		"""oflow commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_oflow'):
			from .Oflow import Oflow
			self._oflow = Oflow(self._core, self._cmd_group)
		return self._oflow

	@property
	def pon(self):
		"""pon commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pon'):
			from .Pon import Pon
			self._pon = Pon(self._core, self._cmd_group)
		return self._pon

	@property
	def power(self):
		"""power commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def symbolRate(self):
		"""symbolRate commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRate
			self._symbolRate = SymbolRate(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Fader':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fader(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
