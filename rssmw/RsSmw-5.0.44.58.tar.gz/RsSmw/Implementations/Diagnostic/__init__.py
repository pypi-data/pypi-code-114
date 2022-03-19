from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Diagnostic:
	"""Diagnostic commands group definition. 19 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("diagnostic", core, parent)

	@property
	def bgInfo(self):
		"""bgInfo commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_bgInfo'):
			from .BgInfo import BgInfo
			self._bgInfo = BgInfo(self._core, self._cmd_group)
		return self._bgInfo

	@property
	def debug(self):
		"""debug commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_debug'):
			from .Debug import Debug
			self._debug = Debug(self._core, self._cmd_group)
		return self._debug

	@property
	def eeprom(self):
		"""eeprom commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_eeprom'):
			from .Eeprom import Eeprom
			self._eeprom = Eeprom(self._core, self._cmd_group)
		return self._eeprom

	@property
	def info(self):
		"""info commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_info'):
			from .Info import Info
			self._info = Info(self._core, self._cmd_group)
		return self._info

	@property
	def point(self):
		"""point commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_point'):
			from .Point import Point
			self._point = Point(self._core, self._cmd_group)
		return self._point

	@property
	def service(self):
		"""service commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_service'):
			from .Service import Service
			self._service = Service(self._core, self._cmd_group)
		return self._service

	@property
	def measure(self):
		"""measure commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_measure'):
			from .Measure import Measure
			self._measure = Measure(self._core, self._cmd_group)
		return self._measure

	def clone(self) -> 'Diagnostic':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Diagnostic(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
