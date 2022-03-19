from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spc:
	"""Spc commands group definition. 6 total commands, 0 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spc", core, parent)

	def get_crange(self) -> float:
		"""SCPI: [SOURce<HW>]:POWer:SPC:CRANge \n
		Snippet: value: float = driver.source.power.spc.get_crange() \n
		No command help available \n
			:return: pow_cntrl_crange: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:SPC:CRANge?')
		return Conversions.str_to_float(response)

	def set_crange(self, pow_cntrl_crange: float) -> None:
		"""SCPI: [SOURce<HW>]:POWer:SPC:CRANge \n
		Snippet: driver.source.power.spc.set_crange(pow_cntrl_crange = 1.0) \n
		No command help available \n
			:param pow_cntrl_crange: No help available
		"""
		param = Conversions.decimal_value_to_str(pow_cntrl_crange)
		self._core.io.write(f'SOURce<HwInstance>:POWer:SPC:CRANge {param}')

	def get_delay(self) -> int:
		"""SCPI: [SOURce<HW>]:POWer:SPC:DELay \n
		Snippet: value: int = driver.source.power.spc.get_delay() \n
		No command help available \n
			:return: pow_cntrl_delay: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:SPC:DELay?')
		return Conversions.str_to_int(response)

	def set_delay(self, pow_cntrl_delay: int) -> None:
		"""SCPI: [SOURce<HW>]:POWer:SPC:DELay \n
		Snippet: driver.source.power.spc.set_delay(pow_cntrl_delay = 1) \n
		No command help available \n
			:param pow_cntrl_delay: No help available
		"""
		param = Conversions.decimal_value_to_str(pow_cntrl_delay)
		self._core.io.write(f'SOURce<HwInstance>:POWer:SPC:DELay {param}')

	def get_peak(self) -> bool:
		"""SCPI: [SOURce<HW>]:POWer:SPC:PEAK \n
		Snippet: value: bool = driver.source.power.spc.get_peak() \n
		No command help available \n
			:return: pow_cntrl_peak: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:SPC:PEAK?')
		return Conversions.str_to_bool(response)

	def set_peak(self, pow_cntrl_peak: bool) -> None:
		"""SCPI: [SOURce<HW>]:POWer:SPC:PEAK \n
		Snippet: driver.source.power.spc.set_peak(pow_cntrl_peak = False) \n
		No command help available \n
			:param pow_cntrl_peak: No help available
		"""
		param = Conversions.bool_to_str(pow_cntrl_peak)
		self._core.io.write(f'SOURce<HwInstance>:POWer:SPC:PEAK {param}')

	# noinspection PyTypeChecker
	def get_select(self) -> enums.PowCntrlSelect:
		"""SCPI: [SOURce<HW>]:POWer:SPC:SELect \n
		Snippet: value: enums.PowCntrlSelect = driver.source.power.spc.get_select() \n
		No command help available \n
			:return: pow_cntrl_select: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:SPC:SELect?')
		return Conversions.str_to_scalar_enum(response, enums.PowCntrlSelect)

	def set_select(self, pow_cntrl_select: enums.PowCntrlSelect) -> None:
		"""SCPI: [SOURce<HW>]:POWer:SPC:SELect \n
		Snippet: driver.source.power.spc.set_select(pow_cntrl_select = enums.PowCntrlSelect.SENS1) \n
		No command help available \n
			:param pow_cntrl_select: No help available
		"""
		param = Conversions.enum_scalar_to_str(pow_cntrl_select, enums.PowCntrlSelect)
		self._core.io.write(f'SOURce<HwInstance>:POWer:SPC:SELect {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:POWer:SPC:STATe \n
		Snippet: value: bool = driver.source.power.spc.get_state() \n
		No command help available \n
			:return: pow_cntrl_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:SPC:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, pow_cntrl_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:POWer:SPC:STATe \n
		Snippet: driver.source.power.spc.set_state(pow_cntrl_state = False) \n
		No command help available \n
			:param pow_cntrl_state: No help available
		"""
		param = Conversions.bool_to_str(pow_cntrl_state)
		self._core.io.write(f'SOURce<HwInstance>:POWer:SPC:STATe {param}')

	def get_target(self) -> float:
		"""SCPI: [SOURce<HW>]:POWer:SPC:TARGet \n
		Snippet: value: float = driver.source.power.spc.get_target() \n
		No command help available \n
			:return: pow_cntrl_target: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:SPC:TARGet?')
		return Conversions.str_to_float(response)

	def set_target(self, pow_cntrl_target: float) -> None:
		"""SCPI: [SOURce<HW>]:POWer:SPC:TARGet \n
		Snippet: driver.source.power.spc.set_target(pow_cntrl_target = 1.0) \n
		No command help available \n
			:param pow_cntrl_target: No help available
		"""
		param = Conversions.decimal_value_to_str(pow_cntrl_target)
		self._core.io.write(f'SOURce<HwInstance>:POWer:SPC:TARGet {param}')
