from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	# noinspection PyTypeChecker
	def get_vsb_frequency(self) -> enums.AtscmhGeneralVsbFrequency:
		"""SCPI: [SOURce<HW>]:BB:ATSM:FREQuency:VSBFrequency \n
		Snippet: value: enums.AtscmhGeneralVsbFrequency = driver.source.bb.atsm.frequency.get_vsb_frequency() \n
		Sets the vestigial sideband (VSB) reference frequency point. \n
			:return: vsb_frequency: PILot| CENTer
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ATSM:FREQuency:VSBFrequency?')
		return Conversions.str_to_scalar_enum(response, enums.AtscmhGeneralVsbFrequency)

	def set_vsb_frequency(self, vsb_frequency: enums.AtscmhGeneralVsbFrequency) -> None:
		"""SCPI: [SOURce<HW>]:BB:ATSM:FREQuency:VSBFrequency \n
		Snippet: driver.source.bb.atsm.frequency.set_vsb_frequency(vsb_frequency = enums.AtscmhGeneralVsbFrequency.CENTer) \n
		Sets the vestigial sideband (VSB) reference frequency point. \n
			:param vsb_frequency: PILot| CENTer
		"""
		param = Conversions.enum_scalar_to_str(vsb_frequency, enums.AtscmhGeneralVsbFrequency)
		self._core.io.write(f'SOURce<HwInstance>:BB:ATSM:FREQuency:VSBFrequency {param}')
