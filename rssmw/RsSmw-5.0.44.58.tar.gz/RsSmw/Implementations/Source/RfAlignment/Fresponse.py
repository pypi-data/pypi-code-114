from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fresponse:
	"""Fresponse commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fresponse", core, parent)

	def get_file(self) -> str:
		"""SCPI: SOURce<HW>:RFALignment:FRESponse:FILE \n
		Snippet: value: str = driver.source.rfAlignment.fresponse.get_file() \n
		No command help available \n
			:return: freq_resp_file: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:RFALignment:FRESponse:FILE?')
		return trim_str_response(response)

	def set_file(self, freq_resp_file: str) -> None:
		"""SCPI: SOURce<HW>:RFALignment:FRESponse:FILE \n
		Snippet: driver.source.rfAlignment.fresponse.set_file(freq_resp_file = '1') \n
		No command help available \n
			:param freq_resp_file: No help available
		"""
		param = Conversions.value_to_quoted_str(freq_resp_file)
		self._core.io.write(f'SOURce<HwInstance>:RFALignment:FRESponse:FILE {param}')
