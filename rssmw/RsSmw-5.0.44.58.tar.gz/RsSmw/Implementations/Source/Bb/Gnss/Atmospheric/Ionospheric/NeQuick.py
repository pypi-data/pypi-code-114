from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NeQuick:
	"""NeQuick commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("neQuick", core, parent)

	def get_sflux(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:IONospheric:NEQuick:SFLux \n
		Snippet: value: float = driver.source.bb.gnss.atmospheric.ionospheric.neQuick.get_sflux() \n
		Sets the solar flux level. \n
			:return: solar_flux: float Range: 0 to 300
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:ATMospheric:IONospheric:NEQuick:SFLux?')
		return Conversions.str_to_float(response)

	def set_sflux(self, solar_flux: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:IONospheric:NEQuick:SFLux \n
		Snippet: driver.source.bb.gnss.atmospheric.ionospheric.neQuick.set_sflux(solar_flux = 1.0) \n
		Sets the solar flux level. \n
			:param solar_flux: float Range: 0 to 300
		"""
		param = Conversions.decimal_value_to_str(solar_flux)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:IONospheric:NEQuick:SFLux {param}')

	def get_sun_spot(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:IONospheric:NEQuick:SUNSpot \n
		Snippet: value: float = driver.source.bb.gnss.atmospheric.ionospheric.neQuick.get_sun_spot() \n
		Sets the sunspot number. \n
			:return: sunspot_number: float Range: -99.636 to 248.870
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:ATMospheric:IONospheric:NEQuick:SUNSpot?')
		return Conversions.str_to_float(response)

	def set_sun_spot(self, sunspot_number: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:IONospheric:NEQuick:SUNSpot \n
		Snippet: driver.source.bb.gnss.atmospheric.ionospheric.neQuick.set_sun_spot(sunspot_number = 1.0) \n
		Sets the sunspot number. \n
			:param sunspot_number: float Range: -99.636 to 248.870
		"""
		param = Conversions.decimal_value_to_str(sunspot_number)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:IONospheric:NEQuick:SUNSpot {param}')

	def get_umsn(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:IONospheric:NEQuick:UMSN \n
		Snippet: value: bool = driver.source.bb.gnss.atmospheric.ionospheric.neQuick.get_umsn() \n
		Enables the instrument to use the measured sunspot number value. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:ATMospheric:IONospheric:NEQuick:UMSN?')
		return Conversions.str_to_bool(response)

	def set_umsn(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:IONospheric:NEQuick:UMSN \n
		Snippet: driver.source.bb.gnss.atmospheric.ionospheric.neQuick.set_umsn(state = False) \n
		Enables the instrument to use the measured sunspot number value. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ATMospheric:IONospheric:NEQuick:UMSN {param}')
