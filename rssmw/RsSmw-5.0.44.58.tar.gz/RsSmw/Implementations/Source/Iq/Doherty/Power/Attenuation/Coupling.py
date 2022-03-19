from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coupling:
	"""Coupling commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coupling", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce]:IQ:DOHerty:POWer:ATTenuation:COUPling:[STATe] \n
		Snippet: value: bool = driver.source.iq.doherty.power.attenuation.coupling.get_state() \n
		If enabled, the digital attenuation values set with the command [:SOURce<hw>]:IQ:DOHerty:POWer:ATTenuation for both
		signals are coupled. The difference between the values is, however, maintained. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce:IQ:DOHerty:POWer:ATTenuation:COUPling:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce]:IQ:DOHerty:POWer:ATTenuation:COUPling:[STATe] \n
		Snippet: driver.source.iq.doherty.power.attenuation.coupling.set_state(state = False) \n
		If enabled, the digital attenuation values set with the command [:SOURce<hw>]:IQ:DOHerty:POWer:ATTenuation for both
		signals are coupled. The difference between the values is, however, maintained. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce:IQ:DOHerty:POWer:ATTenuation:COUPling:STATe {param}')
