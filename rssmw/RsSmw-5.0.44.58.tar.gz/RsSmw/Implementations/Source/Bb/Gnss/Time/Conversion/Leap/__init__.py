from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Leap:
	"""Leap commands group definition. 4 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("leap", core, parent)

	@property
	def date(self):
		"""date commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_date'):
			from .Date import Date
			self._date = Date(self._core, self._cmd_group)
		return self._date

	@property
	def seconds(self):
		"""seconds commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_seconds'):
			from .Seconds import Seconds
			self._seconds = Seconds(self._core, self._cmd_group)
		return self._seconds

	def get_auto(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:CONVersion:LEAP:AUTO \n
		Snippet: value: bool = driver.source.bb.gnss.time.conversion.leap.get_auto() \n
		Enables the simulation of the leap second transition. \n
			:return: auto_configure: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:TIME:CONVersion:LEAP:AUTO?')
		return Conversions.str_to_bool(response)

	def set_auto(self, auto_configure: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:CONVersion:LEAP:AUTO \n
		Snippet: driver.source.bb.gnss.time.conversion.leap.set_auto(auto_configure = False) \n
		Enables the simulation of the leap second transition. \n
			:param auto_configure: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(auto_configure)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:TIME:CONVersion:LEAP:AUTO {param}')

	def clone(self) -> 'Leap':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Leap(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
