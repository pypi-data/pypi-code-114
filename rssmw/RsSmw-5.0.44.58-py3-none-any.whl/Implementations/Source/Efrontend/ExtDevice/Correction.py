from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Correction:
	"""Correction commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("correction", core, parent)

	def get_file(self) -> str:
		"""SCPI: [SOURce<HW>]:EFRontend:EXTDevice:CORRection:FILE \n
		Snippet: value: str = driver.source.efrontend.extDevice.correction.get_file() \n
		No command help available \n
			:return: filename: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:EXTDevice:CORRection:FILE?')
		return trim_str_response(response)

	def set_file(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:EFRontend:EXTDevice:CORRection:FILE \n
		Snippet: driver.source.efrontend.extDevice.correction.set_file(filename = '1') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:EFRontend:EXTDevice:CORRection:FILE {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:EFRontend:EXTDevice:CORRection:STATe \n
		Snippet: value: bool = driver.source.efrontend.extDevice.correction.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:EXTDevice:CORRection:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:EFRontend:EXTDevice:CORRection:STATe \n
		Snippet: driver.source.efrontend.extDevice.correction.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:EFRontend:EXTDevice:CORRection:STATe {param}')
