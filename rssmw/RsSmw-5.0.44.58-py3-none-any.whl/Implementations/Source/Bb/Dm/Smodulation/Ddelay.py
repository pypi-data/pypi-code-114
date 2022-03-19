from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ddelay:
	"""Ddelay commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ddelay", core, parent)

	def get_aadjust(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DM:SMODulation:DDELay:AADJust \n
		Snippet: value: bool = driver.source.bb.dm.smodulation.ddelay.get_aadjust() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:SMODulation:DDELay:AADJust?')
		return Conversions.str_to_bool(response)

	def set_aadjust(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:SMODulation:DDELay:AADJust \n
		Snippet: driver.source.bb.dm.smodulation.ddelay.set_aadjust(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:SMODulation:DDELay:AADJust {param}')

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DM:SMODulation:DDELay \n
		Snippet: value: float = driver.source.bb.dm.smodulation.ddelay.get_value() \n
		No command help available \n
			:return: delay: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:SMODulation:DDELay?')
		return Conversions.str_to_float(response)

	def set_value(self, delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:SMODulation:DDELay \n
		Snippet: driver.source.bb.dm.smodulation.ddelay.set_value(delay = 1.0) \n
		No command help available \n
			:param delay: No help available
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:SMODulation:DDELay {param}')
