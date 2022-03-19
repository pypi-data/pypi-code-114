from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Correction:
	"""Correction commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("correction", core, parent)

	def get_file(self) -> str:
		"""SCPI: SOURce<HW>:BEXTension:CORRection:FILE \n
		Snippet: value: str = driver.source.bextension.correction.get_file() \n
		No command help available \n
			:return: correction_file: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BEXTension:CORRection:FILE?')
		return trim_str_response(response)

	def set_file(self, correction_file: str) -> None:
		"""SCPI: SOURce<HW>:BEXTension:CORRection:FILE \n
		Snippet: driver.source.bextension.correction.set_file(correction_file = '1') \n
		No command help available \n
			:param correction_file: No help available
		"""
		param = Conversions.value_to_quoted_str(correction_file)
		self._core.io.write(f'SOURce<HwInstance>:BEXTension:CORRection:FILE {param}')

	def get_state(self) -> bool:
		"""SCPI: SOURce<HW>:BEXTension:CORRection:STATe \n
		Snippet: value: bool = driver.source.bextension.correction.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BEXTension:CORRection:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: SOURce<HW>:BEXTension:CORRection:STATe \n
		Snippet: driver.source.bextension.correction.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BEXTension:CORRection:STATe {param}')
