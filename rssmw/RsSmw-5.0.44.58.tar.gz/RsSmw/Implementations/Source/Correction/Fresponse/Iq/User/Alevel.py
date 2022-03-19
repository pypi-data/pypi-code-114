from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Alevel:
	"""Alevel commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alevel", core, parent)

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:ALEVel:VALue \n
		Snippet: value: float = driver.source.correction.fresponse.iq.user.alevel.get_value() \n
		No command help available \n
			:return: freq_cor_iq_absolute_val: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:ALEVel:VALue?')
		return Conversions.str_to_float(response)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:ALEVel:[STATe] \n
		Snippet: value: bool = driver.source.correction.fresponse.iq.user.alevel.get_state() \n
		No command help available \n
			:return: freq_corr_iq_al_sta: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:ALEVel:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, freq_corr_iq_al_sta: bool) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:ALEVel:[STATe] \n
		Snippet: driver.source.correction.fresponse.iq.user.alevel.set_state(freq_corr_iq_al_sta = False) \n
		No command help available \n
			:param freq_corr_iq_al_sta: No help available
		"""
		param = Conversions.bool_to_str(freq_corr_iq_al_sta)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:ALEVel:STATe {param}')
