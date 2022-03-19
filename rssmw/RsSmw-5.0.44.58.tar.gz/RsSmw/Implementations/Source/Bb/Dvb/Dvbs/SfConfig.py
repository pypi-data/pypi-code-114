from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SfConfig:
	"""SfConfig commands group definition. 16 total commands, 0 Subgroups, 16 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sfConfig", core, parent)

	def get_csf_length(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:CSFLength \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.sfConfig.get_csf_length() \n
		No command help available \n
			:return: calculated_sfl: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:CSFLength?')
		return Conversions.str_to_int(response)

	def get_cu_length(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:CULength \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.sfConfig.get_cu_length() \n
		No command help available \n
			:return: cu_length: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:CULength?')
		return Conversions.str_to_int(response)

	def get_dsf(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:DSF \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.sfConfig.get_dsf() \n
		No command help available \n
			:return: pilot_filed_dis: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:DSF?')
		return Conversions.str_to_int(response)

	def get_ehf_size(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:EHFSize \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.sfConfig.get_ehf_size() \n
		No command help available \n
			:return: ehf_size: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:EHFSize?')
		return Conversions.str_to_int(response)

	def get_npay(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:NPAY \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.sfConfig.get_npay() \n
		No command help available \n
			:return: npay: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:NPAY?')
		return Conversions.str_to_int(response)

	def set_npay(self, npay: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:NPAY \n
		Snippet: driver.source.bb.dvb.dvbs.sfConfig.set_npay(npay = 1) \n
		No command help available \n
			:param npay: No help available
		"""
		param = Conversions.decimal_value_to_str(npay)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:NPAY {param}')

	def get_nref(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:NREF \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.sfConfig.get_nref() \n
		No command help available \n
			:return: nref: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:NREF?')
		return Conversions.str_to_int(response)

	def set_nref(self, nref: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:NREF \n
		Snippet: driver.source.bb.dvb.dvbs.sfConfig.set_nref(nref = 1) \n
		No command help available \n
			:param nref: No help available
		"""
		param = Conversions.decimal_value_to_str(nref)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:NREF {param}')

	def get_plength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:PLENgth \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.sfConfig.get_plength() \n
		No command help available \n
			:return: postamble_length: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:PLENgth?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_pli(self) -> enums.DvbS2Xsfpli:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:PLI \n
		Snippet: value: enums.DvbS2Xsfpli = driver.source.bb.dvb.dvbs.sfConfig.get_pli() \n
		No command help available \n
			:return: pli: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:PLI?')
		return Conversions.str_to_scalar_enum(response, enums.DvbS2Xsfpli)

	def set_pli(self, pli: enums.DvbS2Xsfpli) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:PLI \n
		Snippet: driver.source.bb.dvb.dvbs.sfConfig.set_pli(pli = enums.DvbS2Xsfpli.HEFF) \n
		No command help available \n
			:param pli: No help available
		"""
		param = Conversions.enum_scalar_to_str(pli, enums.DvbS2Xsfpli)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:PLI {param}')

	def get_psf(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:PSF \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.sfConfig.get_psf() \n
		No command help available \n
			:return: pilot_field_size: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:PSF?')
		return Conversions.str_to_int(response)

	def get_pstate(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:PSTate \n
		Snippet: value: bool = driver.source.bb.dvb.dvbs.sfConfig.get_pstate() \n
		No command help available \n
			:return: sf_pilot_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:PSTate?')
		return Conversions.str_to_bool(response)

	def set_pstate(self, sf_pilot_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:PSTate \n
		Snippet: driver.source.bb.dvb.dvbs.sfConfig.set_pstate(sf_pilot_state = False) \n
		No command help available \n
			:param sf_pilot_state: No help available
		"""
		param = Conversions.bool_to_str(sf_pilot_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:PSTate {param}')

	def get_pwh(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:PWH \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.sfConfig.get_pwh() \n
		No command help available \n
			:return: sf_pilot_wh: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:PWH?')
		return Conversions.str_to_int(response)

	def set_pwh(self, sf_pilot_wh: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:PWH \n
		Snippet: driver.source.bb.dvb.dvbs.sfConfig.set_pwh(sf_pilot_wh = 1) \n
		No command help available \n
			:param sf_pilot_wh: No help available
		"""
		param = Conversions.decimal_value_to_str(sf_pilot_wh)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:PWH {param}')

	# noinspection PyTypeChecker
	def get_sffi(self) -> enums.DvbS2XsfFormat:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:SFFI \n
		Snippet: value: enums.DvbS2XsfFormat = driver.source.bb.dvb.dvbs.sfConfig.get_sffi() \n
		No command help available \n
			:return: sffi: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:SFFI?')
		return Conversions.str_to_scalar_enum(response, enums.DvbS2XsfFormat)

	def set_sffi(self, sffi: enums.DvbS2XsfFormat) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:SFFI \n
		Snippet: driver.source.bb.dvb.dvbs.sfConfig.set_sffi(sffi = enums.DvbS2XsfFormat.SFFI0) \n
		No command help available \n
			:param sffi: No help available
		"""
		param = Conversions.enum_scalar_to_str(sffi, enums.DvbS2XsfFormat)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:SFFI {param}')

	def get_sf_length(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:SFLength \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.sfConfig.get_sf_length() \n
		No command help available \n
			:return: sf_length: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:SFLength?')
		return Conversions.str_to_int(response)

	def set_sf_length(self, sf_length: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:SFLength \n
		Snippet: driver.source.bb.dvb.dvbs.sfConfig.set_sf_length(sf_length = 1) \n
		No command help available \n
			:param sf_length: No help available
		"""
		param = Conversions.decimal_value_to_str(sf_length)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:SFLength {param}')

	def get_sosf(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:SOSF \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.sfConfig.get_sosf() \n
		No command help available \n
			:return: sosf: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:SOSF?')
		return Conversions.str_to_int(response)

	def set_sosf(self, sosf: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:SOSF \n
		Snippet: driver.source.bb.dvb.dvbs.sfConfig.set_sosf(sosf = 1) \n
		No command help available \n
			:param sosf: No help available
		"""
		param = Conversions.decimal_value_to_str(sosf)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:SOSF {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:STATe \n
		Snippet: value: bool = driver.source.bb.dvb.dvbs.sfConfig.get_state() \n
		No command help available \n
			:return: sf_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, sf_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:STATe \n
		Snippet: driver.source.bb.dvb.dvbs.sfConfig.set_state(sf_state = False) \n
		No command help available \n
			:param sf_state: No help available
		"""
		param = Conversions.bool_to_str(sf_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:STATe {param}')

	def get_stwh(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:STWH \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.sfConfig.get_stwh() \n
		No command help available \n
			:return: st: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:STWH?')
		return Conversions.str_to_int(response)

	def set_stwh(self, st: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFConfig:STWH \n
		Snippet: driver.source.bb.dvb.dvbs.sfConfig.set_stwh(st = 1) \n
		No command help available \n
			:param st: No help available
		"""
		param = Conversions.decimal_value_to_str(st)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:SFConfig:STWH {param}')
