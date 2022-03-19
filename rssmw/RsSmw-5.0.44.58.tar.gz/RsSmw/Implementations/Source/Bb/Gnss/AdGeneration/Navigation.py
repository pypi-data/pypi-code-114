from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Navigation:
	"""Navigation commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("navigation", core, parent)

	def get_create(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:NAVigation:CREate \n
		Snippet: value: str = driver.source.bb.gnss.adGeneration.navigation.get_create() \n
		Saves the current assistance data settings into the selected navigation file. Assistance data settings are saved as
		navigation file with the specific file extensions *.rs_nav or into RINEX files with extension .10n. Refer to 'MMEMory
		Subsystem' for general information on file handling in the default and in a specific directory. \n
			:return: filename: string Filename or complete file path
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:ADGeneration:NAVigation:CREate?')
		return trim_str_response(response)

	def set_create(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:NAVigation:CREate \n
		Snippet: driver.source.bb.gnss.adGeneration.navigation.set_create(filename = '1') \n
		Saves the current assistance data settings into the selected navigation file. Assistance data settings are saved as
		navigation file with the specific file extensions *.rs_nav or into RINEX files with extension .10n. Refer to 'MMEMory
		Subsystem' for general information on file handling in the default and in a specific directory. \n
			:param filename: string Filename or complete file path
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ADGeneration:NAVigation:CREate {param}')

	# noinspection PyTypeChecker
	def get_dformat(self) -> enums.NavDataFormat:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:NAVigation:DFORmat \n
		Snippet: value: enums.NavDataFormat = driver.source.bb.gnss.adGeneration.navigation.get_dformat() \n
		Sets format of the generated navigation data file. \n
			:return: data_format: LNAV| CNAV
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:ADGeneration:NAVigation:DFORmat?')
		return Conversions.str_to_scalar_enum(response, enums.NavDataFormat)

	def set_dformat(self, data_format: enums.NavDataFormat) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:NAVigation:DFORmat \n
		Snippet: driver.source.bb.gnss.adGeneration.navigation.set_dformat(data_format = enums.NavDataFormat.CNAV) \n
		Sets format of the generated navigation data file. \n
			:param data_format: LNAV| CNAV
		"""
		param = Conversions.enum_scalar_to_str(data_format, enums.NavDataFormat)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ADGeneration:NAVigation:DFORmat {param}')
