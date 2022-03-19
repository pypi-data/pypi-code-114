from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Logging:
	"""Logging commands group definition. 56 total commands, 4 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("logging", core, parent)

	@property
	def category(self):
		"""category commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_category'):
			from .Category import Category
			self._category = Category(self._core, self._cmd_group)
		return self._category

	@property
	def destination(self):
		"""destination commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_destination'):
			from .Destination import Destination
			self._destination = Destination(self._core, self._cmd_group)
		return self._destination

	@property
	def offline(self):
		"""offline commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_offline'):
			from .Offline import Offline
			self._offline = Offline(self._core, self._cmd_group)
		return self._offline

	@property
	def rt(self):
		"""rt commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rt'):
			from .Rt import Rt
			self._rt = Rt(self._core, self._cmd_group)
		return self._rt

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.LogMode:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:MODE \n
		Snippet: value: enums.LogMode = driver.source.bb.gnss.logging.get_mode() \n
		Sets the logging mode. \n
			:return: mode: RT| OFFLine RT = real-time OFFLine = offline
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.LogMode)

	def set_mode(self, mode: enums.LogMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:MODE \n
		Snippet: driver.source.bb.gnss.logging.set_mode(mode = enums.LogMode.OFFLine) \n
		Sets the logging mode. \n
			:param mode: RT| OFFLine RT = real-time OFFLine = offline
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.LogMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:MODE {param}')

	def clone(self) -> 'Logging':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Logging(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
