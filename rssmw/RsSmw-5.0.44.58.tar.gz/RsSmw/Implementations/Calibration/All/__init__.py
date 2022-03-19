from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 5 total commands, 1 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	@property
	def measure(self):
		"""measure commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_measure'):
			from .Measure import Measure
			self._measure = Measure(self._core, self._cmd_group)
		return self._measure

	def get_date(self) -> str:
		"""SCPI: CALibration<HW>:ALL:DATE \n
		Snippet: value: str = driver.calibration.all.get_date() \n
		Queries the date of the most recently executed full adjustment. \n
			:return: date: string
		"""
		response = self._core.io.query_str('CALibration<HwInstance>:ALL:DATE?')
		return trim_str_response(response)

	def get_information(self) -> str:
		"""SCPI: CALibration<HW>:ALL:INFormation \n
		Snippet: value: str = driver.calibration.all.get_information() \n
		Queries the current state of the internal adjustment. \n
			:return: cal_info_text: string
		"""
		response = self._core.io.query_str('CALibration<HwInstance>:ALL:INFormation?')
		return trim_str_response(response)

	def get_temp(self) -> str:
		"""SCPI: CALibration<HW>:ALL:TEMP \n
		Snippet: value: str = driver.calibration.all.get_temp() \n
		Queries the temperature deviation compared to the calibration temperature. \n
			:return: temperature: string
		"""
		response = self._core.io.query_str('CALibration<HwInstance>:ALL:TEMP?')
		return trim_str_response(response)

	def get_time(self) -> str:
		"""SCPI: CALibration<HW>:ALL:TIME \n
		Snippet: value: str = driver.calibration.all.get_time() \n
		Queries the time elapsed since the last full adjustment. \n
			:return: time: string
		"""
		response = self._core.io.query_str('CALibration<HwInstance>:ALL:TIME?')
		return trim_str_response(response)

	def clone(self) -> 'All':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = All(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
