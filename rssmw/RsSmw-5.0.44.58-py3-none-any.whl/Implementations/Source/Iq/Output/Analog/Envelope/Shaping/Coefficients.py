from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coefficients:
	"""Coefficients commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coefficients", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:SHAPing:COEFficients:CATalog \n
		Snippet: value: List[str] = driver.source.iq.output.analog.envelope.shaping.coefficients.get_catalog() \n
		Queries the available polynomial files in the default directory. Only files with the file extension *.iq_poly are listed. \n
			:return: catalog: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:SHAPing:COEFficients:CATalog?')
		return Conversions.str_to_str_list(response)

	def load(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:SHAPing:COEFficients:LOAD \n
		Snippet: driver.source.iq.output.analog.envelope.shaping.coefficients.load(filename = '1') \n
		Loads the selected polynomial file. \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:SHAPing:COEFficients:LOAD {param}')

	def set_store(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:SHAPing:COEFficients:STORe \n
		Snippet: driver.source.iq.output.analog.envelope.shaping.coefficients.set_store(filename = '1') \n
		Saves the polynomial function as polynomial file. \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:SHAPing:COEFficients:STORe {param}')

	def get_value(self) -> List[float]:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:SHAPing:COEFficients \n
		Snippet: value: List[float] = driver.source.iq.output.analog.envelope.shaping.coefficients.get_value() \n
		Sets the polynomial coefficients. \n
			:return: ipartq_out_env_poly_coeffs: No help available
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:SHAPing:COEFficients?')
		return response

	def set_value(self, ipartq_out_env_poly_coeffs: List[float]) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:SHAPing:COEFficients \n
		Snippet: driver.source.iq.output.analog.envelope.shaping.coefficients.set_value(ipartq_out_env_poly_coeffs = [1.1, 2.2, 3.3]) \n
		Sets the polynomial coefficients. \n
			:param ipartq_out_env_poly_coeffs: No help available
		"""
		param = Conversions.list_to_csv_str(ipartq_out_env_poly_coeffs)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:SHAPing:COEFficients {param}')
