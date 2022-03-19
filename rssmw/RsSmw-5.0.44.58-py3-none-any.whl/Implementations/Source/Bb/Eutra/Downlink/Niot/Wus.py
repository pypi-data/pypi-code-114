from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Wus:
	"""Wus commands group definition. 7 total commands, 0 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wus", core, parent)

	# noinspection PyTypeChecker
	def get_acd(self) -> enums.EutraNbiotWusDurationFormat:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:WUS:ACD \n
		Snippet: value: enums.EutraNbiotWusDurationFormat = driver.source.bb.eutra.downlink.niot.wus.get_acd() \n
		Sets the duration of WUS in subframes. \n
			:return: nwus_act_d: DN_1| DN_2| DN_4| DN_8| DN_16| DN_32| DN_64| DN_128| DN_256| DN_512| DN_1024
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:NIOT:WUS:ACD?')
		return Conversions.str_to_scalar_enum(response, enums.EutraNbiotWusDurationFormat)

	def set_acd(self, nwus_act_d: enums.EutraNbiotWusDurationFormat) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:WUS:ACD \n
		Snippet: driver.source.bb.eutra.downlink.niot.wus.set_acd(nwus_act_d = enums.EutraNbiotWusDurationFormat.DN_1) \n
		Sets the duration of WUS in subframes. \n
			:param nwus_act_d: DN_1| DN_2| DN_4| DN_8| DN_16| DN_32| DN_64| DN_128| DN_256| DN_512| DN_1024
		"""
		param = Conversions.enum_scalar_to_str(nwus_act_d, enums.EutraNbiotWusDurationFormat)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:WUS:ACD {param}')

	# noinspection PyTypeChecker
	def get_max_duration(self) -> enums.EutraNbiotWusDurationFormat:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:WUS:MAXDuration \n
		Snippet: value: enums.EutraNbiotWusDurationFormat = driver.source.bb.eutra.downlink.niot.wus.get_max_duration() \n
		Sets the maximum WUS duration in subframes. \n
			:return: nwus_max_dur: DN_1| DN_2| DN_4| DN_8| DN_16| DN_32| DN_64| DN_128| DN_256| DN_512| DN_1024
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:NIOT:WUS:MAXDuration?')
		return Conversions.str_to_scalar_enum(response, enums.EutraNbiotWusDurationFormat)

	def set_max_duration(self, nwus_max_dur: enums.EutraNbiotWusDurationFormat) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:WUS:MAXDuration \n
		Snippet: driver.source.bb.eutra.downlink.niot.wus.set_max_duration(nwus_max_dur = enums.EutraNbiotWusDurationFormat.DN_1) \n
		Sets the maximum WUS duration in subframes. \n
			:param nwus_max_dur: DN_1| DN_2| DN_4| DN_8| DN_16| DN_32| DN_64| DN_128| DN_256| DN_512| DN_1024
		"""
		param = Conversions.enum_scalar_to_str(nwus_max_dur, enums.EutraNbiotWusDurationFormat)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:WUS:MAXDuration {param}')

	def get_pow(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:WUS:POW \n
		Snippet: value: float = driver.source.bb.eutra.downlink.niot.wus.get_pow() \n
		Sets the transmit power of NB-IoT wake up signal \n
			:return: nwus_power: float Range: -80 to 10, Unit: dB
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:NIOT:WUS:POW?')
		return Conversions.str_to_float(response)

	def set_pow(self, nwus_power: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:WUS:POW \n
		Snippet: driver.source.bb.eutra.downlink.niot.wus.set_pow(nwus_power = 1.0) \n
		Sets the transmit power of NB-IoT wake up signal \n
			:param nwus_power: float Range: -80 to 10, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(nwus_power)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:WUS:POW {param}')

	def get_psf(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:WUS:PSF \n
		Snippet: value: int = driver.source.bb.eutra.downlink.niot.wus.get_psf() \n
		Queries the first paging occasion in subframes associated with WUS. \n
			:return: nwus_psf: integer Range: 0 to 534593
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:NIOT:WUS:PSF?')
		return Conversions.str_to_int(response)

	def get_sf(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:WUS:SF \n
		Snippet: value: int = driver.source.bb.eutra.downlink.niot.wus.get_sf() \n
		Specifies the first subframe for paging associated with a WUS transmission. \n
			:return: nwus_sf: Integer Range: 0 to 533329
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:NIOT:WUS:SF?')
		return Conversions.str_to_int(response)

	def set_sf(self, nwus_sf: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:WUS:SF \n
		Snippet: driver.source.bb.eutra.downlink.niot.wus.set_sf(nwus_sf = 1) \n
		Specifies the first subframe for paging associated with a WUS transmission. \n
			:param nwus_sf: Integer Range: 0 to 533329
		"""
		param = Conversions.decimal_value_to_str(nwus_sf)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:WUS:SF {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:WUS:STATe \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.niot.wus.get_state() \n
		Enables or disables the NB-IoT wake up signal. \n
			:return: nwus_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:NIOT:WUS:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, nwus_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:WUS:STATe \n
		Snippet: driver.source.bb.eutra.downlink.niot.wus.set_state(nwus_state = False) \n
		Enables or disables the NB-IoT wake up signal. \n
			:param nwus_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(nwus_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:WUS:STATe {param}')

	# noinspection PyTypeChecker
	def get_to(self) -> enums.EutraNbiotWusTimeOffsetFormat:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:WUS:TO \n
		Snippet: value: enums.EutraNbiotWusTimeOffsetFormat = driver.source.bb.eutra.downlink.niot.wus.get_to() \n
		Sets the offset in ms from the end of the configured maximum WUS duration to the associated paging occasion. \n
			:return: nwus_to: TO_40| TO_80| TO160| TO240
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:NIOT:WUS:TO?')
		return Conversions.str_to_scalar_enum(response, enums.EutraNbiotWusTimeOffsetFormat)

	def set_to(self, nwus_to: enums.EutraNbiotWusTimeOffsetFormat) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:WUS:TO \n
		Snippet: driver.source.bb.eutra.downlink.niot.wus.set_to(nwus_to = enums.EutraNbiotWusTimeOffsetFormat.TO_40) \n
		Sets the offset in ms from the end of the configured maximum WUS duration to the associated paging occasion. \n
			:param nwus_to: TO_40| TO_80| TO160| TO240
		"""
		param = Conversions.enum_scalar_to_str(nwus_to, enums.EutraNbiotWusTimeOffsetFormat)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:WUS:TO {param}')
