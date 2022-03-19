from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class File:
	"""File commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("file", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:SHAPing:FILE:CATalog \n
		Snippet: value: List[str] = driver.source.iq.output.analog.envelope.shaping.file.get_catalog() \n
		Queries the available table shaping files in the default directory. Only files with the file extension *.iq_lut or *.
		iq_lutpv are listed. \n
			:return: catalog: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:SHAPing:FILE:CATalog?')
		return Conversions.str_to_str_list(response)

	def get_data(self) -> List[float]:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:SHAPing:FILE:DATA \n
		Snippet: value: List[float] = driver.source.iq.output.analog.envelope.shaping.file.get_data() \n
		Defines the shaping function in a raw data format. See also [:SOURce<hw>]:IQ:OUTPut[:ANALog]:ENVelope:SHAPing:PV:FILE:NEW. \n
			:return: ipartq_out_env_shape_data: No help available
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:SHAPing:FILE:DATA?')
		return response

	def set_data(self, ipartq_out_env_shape_data: List[float]) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:SHAPing:FILE:DATA \n
		Snippet: driver.source.iq.output.analog.envelope.shaping.file.set_data(ipartq_out_env_shape_data = [1.1, 2.2, 3.3]) \n
		Defines the shaping function in a raw data format. See also [:SOURce<hw>]:IQ:OUTPut[:ANALog]:ENVelope:SHAPing:PV:FILE:NEW. \n
			:param ipartq_out_env_shape_data: No help available
		"""
		param = Conversions.list_to_csv_str(ipartq_out_env_shape_data)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:SHAPing:FILE:DATA {param}')

	def set_new(self, ipartd_pi_db_iq_out_env_shape_data_new_file: List[float]) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:SHAPing:FILE:NEW \n
		Snippet: driver.source.iq.output.analog.envelope.shaping.file.set_new(ipartd_pi_db_iq_out_env_shape_data_new_file = [1.1, 2.2, 3.3]) \n
		Stores the shaping values into a file with the selected file name and loads it. The file is stored in the default
		directory or in the directory specified with the absolute file path. If the file does not yet exist, a new file is
		created. The file extension is assigned automatically. \n
			:param ipartd_pi_db_iq_out_env_shape_data_new_file: No help available
		"""
		param = Conversions.list_to_csv_str(ipartd_pi_db_iq_out_env_shape_data_new_file)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:SHAPing:FILE:NEW {param}')

	def get_select(self) -> str:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:SHAPing:FILE:[SELect] \n
		Snippet: value: str = driver.source.iq.output.analog.envelope.shaping.file.get_select() \n
		Selects an envelope shaping file (extension *.iq_lut or *.iq_lutpv) . \n
			:return: filename: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:SHAPing:FILE:SELect?')
		return trim_str_response(response)

	def set_select(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:SHAPing:FILE:[SELect] \n
		Snippet: driver.source.iq.output.analog.envelope.shaping.file.set_select(filename = '1') \n
		Selects an envelope shaping file (extension *.iq_lut or *.iq_lutpv) . \n
			:param filename: string
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:SHAPing:FILE:SELect {param}')
