from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Communicate:
	"""Communicate commands group definition. 49 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("communicate", core, parent)

	@property
	def bb(self):
		"""bb commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bb'):
			from .Bb import Bb
			self._bb = Bb(self._core, self._cmd_group)
		return self._bb

	@property
	def gpib(self):
		"""gpib commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_gpib'):
			from .Gpib import Gpib
			self._gpib = Gpib(self._core, self._cmd_group)
		return self._gpib

	@property
	def hislip(self):
		"""hislip commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hislip'):
			from .Hislip import Hislip
			self._hislip = Hislip(self._core, self._cmd_group)
		return self._hislip

	@property
	def network(self):
		"""network commands group. 3 Sub-classes, 3 commands."""
		if not hasattr(self, '_network'):
			from .Network import Network
			self._network = Network(self._core, self._cmd_group)
		return self._network

	@property
	def scpi(self):
		"""scpi commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_scpi'):
			from .Scpi import Scpi
			self._scpi = Scpi(self._core, self._cmd_group)
		return self._scpi

	@property
	def serial(self):
		"""serial commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_serial'):
			from .Serial import Serial
			self._serial = Serial(self._core, self._cmd_group)
		return self._serial

	@property
	def socket(self):
		"""socket commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_socket'):
			from .Socket import Socket
			self._socket = Socket(self._core, self._cmd_group)
		return self._socket

	@property
	def usb(self):
		"""usb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_usb'):
			from .Usb import Usb
			self._usb = Usb(self._core, self._cmd_group)
		return self._usb

	def clone(self) -> 'Communicate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Communicate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
