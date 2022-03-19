from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Noise:
	"""Noise commands group definition. 6 total commands, 0 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("noise", core, parent)

	def get_noc_1(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:NOISe:NOC1 \n
		Snippet: value: float = driver.source.bb.eutra.noise.get_noc_1() \n
		No command help available \n
			:return: eu_nois_noc_1: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:NOISe:NOC1?')
		return Conversions.str_to_float(response)

	def set_noc_1(self, eu_nois_noc_1: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:NOISe:NOC1 \n
		Snippet: driver.source.bb.eutra.noise.set_noc_1(eu_nois_noc_1 = 1.0) \n
		No command help available \n
			:param eu_nois_noc_1: No help available
		"""
		param = Conversions.decimal_value_to_str(eu_nois_noc_1)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:NOISe:NOC1 {param}')

	def get_noc_2(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:NOISe:NOC2 \n
		Snippet: value: float = driver.source.bb.eutra.noise.get_noc_2() \n
		No command help available \n
			:return: eu_nois_noc_2: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:NOISe:NOC2?')
		return Conversions.str_to_float(response)

	def set_noc_2(self, eu_nois_noc_2: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:NOISe:NOC2 \n
		Snippet: driver.source.bb.eutra.noise.set_noc_2(eu_nois_noc_2 = 1.0) \n
		No command help available \n
			:param eu_nois_noc_2: No help available
		"""
		param = Conversions.decimal_value_to_str(eu_nois_noc_2)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:NOISe:NOC2 {param}')

	def get_noc_3(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:NOISe:NOC3 \n
		Snippet: value: float = driver.source.bb.eutra.noise.get_noc_3() \n
		No command help available \n
			:return: eu_nois_noc_3: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:NOISe:NOC3?')
		return Conversions.str_to_float(response)

	def set_noc_3(self, eu_nois_noc_3: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:NOISe:NOC3 \n
		Snippet: driver.source.bb.eutra.noise.set_noc_3(eu_nois_noc_3 = 1.0) \n
		No command help available \n
			:param eu_nois_noc_3: No help available
		"""
		param = Conversions.decimal_value_to_str(eu_nois_noc_3)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:NOISe:NOC3 {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:NOISe:STATe \n
		Snippet: value: bool = driver.source.bb.eutra.noise.get_state() \n
		No command help available \n
			:return: eu_nois_stat: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:NOISe:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, eu_nois_stat: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:NOISe:STATe \n
		Snippet: driver.source.bb.eutra.noise.set_state(eu_nois_stat = False) \n
		No command help available \n
			:param eu_nois_stat: No help available
		"""
		param = Conversions.bool_to_str(eu_nois_stat)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:NOISe:STATe {param}')

	def get_tmodel(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:NOISe:TMODel \n
		Snippet: value: str = driver.source.bb.eutra.noise.get_tmodel() \n
		No command help available \n
			:return: eu_nois_model: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:NOISe:TMODel?')
		return trim_str_response(response)

	def set_tmodel(self, eu_nois_model: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:NOISe:TMODel \n
		Snippet: driver.source.bb.eutra.noise.set_tmodel(eu_nois_model = '1') \n
		No command help available \n
			:param eu_nois_model: No help available
		"""
		param = Conversions.value_to_quoted_str(eu_nois_model)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:NOISe:TMODel {param}')

	def get_umode(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:NOISe:UMODe \n
		Snippet: value: bool = driver.source.bb.eutra.noise.get_umode() \n
		No command help available \n
			:return: eu_nois_user: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:NOISe:UMODe?')
		return Conversions.str_to_bool(response)

	def set_umode(self, eu_nois_user: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:NOISe:UMODe \n
		Snippet: driver.source.bb.eutra.noise.set_umode(eu_nois_user = False) \n
		No command help available \n
			:param eu_nois_user: No help available
		"""
		param = Conversions.bool_to_str(eu_nois_user)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:NOISe:UMODe {param}')
