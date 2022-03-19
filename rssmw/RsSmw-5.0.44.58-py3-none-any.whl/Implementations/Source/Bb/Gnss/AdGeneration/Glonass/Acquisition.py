from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Acquisition:
	"""Acquisition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("acquisition", core, parent)

	# noinspection PyTypeChecker
	def get_dformat(self) -> enums.AcqDataFormatGlonass:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:GLONass:ACQuisition:DFORmat \n
		Snippet: value: enums.AcqDataFormatGlonass = driver.source.bb.gnss.adGeneration.glonass.acquisition.get_dformat() \n
		No command help available \n
			:return: data_format: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:ADGeneration:GLONass:ACQuisition:DFORmat?')
		return Conversions.str_to_scalar_enum(response, enums.AcqDataFormatGlonass)

	def set_dformat(self, data_format: enums.AcqDataFormatGlonass) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:GLONass:ACQuisition:DFORmat \n
		Snippet: driver.source.bb.gnss.adGeneration.glonass.acquisition.set_dformat(data_format = enums.AcqDataFormatGlonass.G3GPP) \n
		No command help available \n
			:param data_format: No help available
		"""
		param = Conversions.enum_scalar_to_str(data_format, enums.AcqDataFormatGlonass)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ADGeneration:GLONass:ACQuisition:DFORmat {param}')
