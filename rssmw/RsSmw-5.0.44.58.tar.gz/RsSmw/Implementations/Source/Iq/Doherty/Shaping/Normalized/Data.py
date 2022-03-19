from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:NORMalized:DATA:CATalog \n
		Snippet: value: List[str] = driver.source.iq.doherty.shaping.normalized.data.get_catalog() \n
		Queries the available files with normalized data in the default directory. Only files with the file extension *.dpd_norm
		are listed. \n
			:return: catalog: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DOHerty:SHAPing:NORMalized:DATA:CATalog?')
		return Conversions.str_to_str_list(response)

	def load(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:NORMalized:DATA:LOAD \n
		Snippet: driver.source.iq.doherty.shaping.normalized.data.load(filename = '1') \n
		Loads the selected file. \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DOHerty:SHAPing:NORMalized:DATA:LOAD {param}')

	def set_store(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:NORMalized:DATA:STORe \n
		Snippet: driver.source.iq.doherty.shaping.normalized.data.set_store(filename = '1') \n
		Saves the normalized data in a file. \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DOHerty:SHAPing:NORMalized:DATA:STORe {param}')

	def get_value(self) -> bytes:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:NORMalized:DATA \n
		Snippet: value: bytes = driver.source.iq.doherty.shaping.normalized.data.get_value() \n
		Defines the normalized predistortion function in a raw data format (binary data) . \n
			:return: data: #LengthNoBytesNoBytesNormData # The binary data must start with the sign # LengthNoBytes ASCII format Sets the length of NoBytes, i.e. the number of digits used to write NoBytes NoBytes An ASCII integer value that specifies the number of bytes that follow in the NormData part Each of the NormData parameters is coded with 8 bytes. Then the number of bytes NoBytes is calculated as: NoBytes = 8 + 8 + n(8+8+8) , where n is the number of points NoPoints. NormData PinMaxNoPoints{VinVmaxDeltaVDeltaPhase} Values in binary format, describing the maximum absolute input power Pinmax, the number of subsequent points n and the normalized values Vin/Vmax, ΔV/V, ΔPhase [deg].
		"""
		response = self._core.io.query_bin_block('SOURce<HwInstance>:IQ:DOHerty:SHAPing:NORMalized:DATA?')
		return response

	def set_value(self, data: bytes) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:NORMalized:DATA \n
		Snippet: driver.source.iq.doherty.shaping.normalized.data.set_value(data = b'ABCDEFGH') \n
		Defines the normalized predistortion function in a raw data format (binary data) . \n
			:param data: #LengthNoBytesNoBytesNormData # The binary data must start with the sign # LengthNoBytes ASCII format Sets the length of NoBytes, i.e. the number of digits used to write NoBytes NoBytes An ASCII integer value that specifies the number of bytes that follow in the NormData part Each of the NormData parameters is coded with 8 bytes. Then the number of bytes NoBytes is calculated as: NoBytes = 8 + 8 + n(8+8+8) , where n is the number of points NoPoints. NormData PinMaxNoPoints{VinVmaxDeltaVDeltaPhase} Values in binary format, describing the maximum absolute input power Pinmax, the number of subsequent points n and the normalized values Vin/Vmax, ΔV/V, ΔPhase [deg].
		"""
		self._core.io.write_bin_block('SOURce<HwInstance>:IQ:DOHerty:SHAPing:NORMalized:DATA ', data)
