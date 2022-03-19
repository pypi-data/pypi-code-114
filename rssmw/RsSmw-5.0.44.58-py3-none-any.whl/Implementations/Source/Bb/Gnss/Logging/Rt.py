from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rt:
	"""Rt commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rt", core, parent)

	def get_changes(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:RT:CHANges \n
		Snippet: value: bool = driver.source.bb.gnss.logging.rt.get_changes() \n
		No command help available \n
			:return: status: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:RT:CHANges?')
		return Conversions.str_to_bool(response)

	def set_changes(self, status: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:RT:CHANges \n
		Snippet: driver.source.bb.gnss.logging.rt.set_changes(status = False) \n
		No command help available \n
			:param status: No help available
		"""
		param = Conversions.bool_to_str(status)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:RT:CHANges {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:RT:STATe \n
		Snippet: value: bool = driver.source.bb.gnss.logging.rt.get_state() \n
		Starts real-time data logging. \n
			:return: status: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:RT:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, status: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:RT:STATe \n
		Snippet: driver.source.bb.gnss.logging.rt.set_state(status = False) \n
		Starts real-time data logging. \n
			:param status: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(status)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:RT:STATe {param}')
