from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqModulator:
	"""IqModulator commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqModulator", core, parent)

	def get_full(self) -> bool:
		"""SCPI: CALibration<HW>:IQModulator:FULL \n
		Snippet: value: bool = driver.calibration.iqModulator.get_full() \n
		No command help available \n
			:return: full: No help available
		"""
		response = self._core.io.query_str('CALibration<HwInstance>:IQModulator:FULL?')
		return Conversions.str_to_bool(response)

	def get_local(self) -> bool:
		"""SCPI: CALibration<HW>:IQModulator:LOCal \n
		Snippet: value: bool = driver.calibration.iqModulator.get_local() \n
		No command help available \n
			:return: local: No help available
		"""
		response = self._core.io.query_str('CALibration<HwInstance>:IQModulator:LOCal?')
		return Conversions.str_to_bool(response)
