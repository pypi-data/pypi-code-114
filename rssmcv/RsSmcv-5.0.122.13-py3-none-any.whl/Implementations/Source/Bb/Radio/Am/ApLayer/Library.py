from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Library:
	"""Library commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("library", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:RADio:AM:APLayer:LIBRary:CATalog \n
		Snippet: value: List[str] = driver.source.bb.radio.am.apLayer.library.get_catalog() \n
		Queries the files with settings in the default directory. Listed are files with the file extension *.wv and *.wav. Refer
		to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in
		a specific directory. \n
			:return: tx_audio_bc_am_wav_cat_nam: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:AM:APLayer:LIBRary:CATalog?')
		return Conversions.str_to_str_list(response)

	def get_select(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:RADio:AM:APLayer:LIBRary:SELect \n
		Snippet: value: str = driver.source.bb.radio.am.apLayer.library.get_select() \n
		Selects the audio file. If no file of the specified name exists, an error message is displayed. You can select files with
		the file extension *.wv and *.wav. Refer to 'Accessing Files in the Default or Specified Directory' for general
		information on file handling in the default and in a specific directory. \n
			:return: sel: string Filename or complete file path; file extension can be omitted
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:AM:APLayer:LIBRary:SELect?')
		return trim_str_response(response)

	def set_select(self, sel: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:AM:APLayer:LIBRary:SELect \n
		Snippet: driver.source.bb.radio.am.apLayer.library.set_select(sel = '1') \n
		Selects the audio file. If no file of the specified name exists, an error message is displayed. You can select files with
		the file extension *.wv and *.wav. Refer to 'Accessing Files in the Default or Specified Directory' for general
		information on file handling in the default and in a specific directory. \n
			:param sel: string Filename or complete file path; file extension can be omitted
		"""
		param = Conversions.value_to_quoted_str(sel)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:AM:APLayer:LIBRary:SELect {param}')
