from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Correction:
	"""Correction commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("correction", core, parent)

	def get_file(self) -> str:
		"""SCPI: SOURce<HW>:RFALignment:CORRection:FILE \n
		Snippet: value: str = driver.source.rfAlignment.correction.get_file() \n
		No command help available \n
			:return: correction_file: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:RFALignment:CORRection:FILE?')
		return trim_str_response(response)

	def set_file(self, correction_file: str) -> None:
		"""SCPI: SOURce<HW>:RFALignment:CORRection:FILE \n
		Snippet: driver.source.rfAlignment.correction.set_file(correction_file = '1') \n
		No command help available \n
			:param correction_file: No help available
		"""
		param = Conversions.value_to_quoted_str(correction_file)
		self._core.io.write(f'SOURce<HwInstance>:RFALignment:CORRection:FILE {param}')

	def get_iq_delay(self) -> float:
		"""SCPI: SOURce<HW>:RFALignment:CORRection:IQDelay \n
		Snippet: value: float = driver.source.rfAlignment.correction.get_iq_delay() \n
		Queries the I/Q delay applied for compensation of the frequency response of the signal. \n
			:return: ipart_qdelay: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:RFALignment:CORRection:IQDelay?')
		return Conversions.str_to_float(response)

	def get_level(self) -> float:
		"""SCPI: SOURce<HW>:RFALignment:CORRection:LEVel \n
		Snippet: value: float = driver.source.rfAlignment.correction.get_level() \n
		Queries the level correction applied to the signal of the selected path. \n
			:return: level: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:RFALignment:CORRection:LEVel?')
		return Conversions.str_to_float(response)

	def get_phase(self) -> float:
		"""SCPI: SOURce<HW>:RFALignment:CORRection:PHASe \n
		Snippet: value: float = driver.source.rfAlignment.correction.get_phase() \n
		queries the delta phase applied for compensation of the frequency response of the signal. \n
			:return: phase: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:RFALignment:CORRection:PHASe?')
		return Conversions.str_to_float(response)
