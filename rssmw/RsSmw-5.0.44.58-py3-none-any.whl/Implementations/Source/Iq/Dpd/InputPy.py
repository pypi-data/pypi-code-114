from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputPy:
	"""InputPy commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputPy", core, parent)

	def get_cfactor(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:DPD:INPut:CFACtor \n
		Snippet: value: float = driver.source.iq.dpd.inputPy.get_cfactor() \n
		Queries the measured values the before and after the enabled digital predistortion. \n
			:return: crest_factor: float The query returns -1000 if the calculation is impossible or there are no measurements results available.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:INPut:CFACtor?')
		return Conversions.str_to_float(response)

	def get_level(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:DPD:INPut:LEVel \n
		Snippet: value: float = driver.source.iq.dpd.inputPy.get_level() \n
		Queries the measured values the before and after the enabled digital predistortion. \n
			:return: level: float The query returns -1000 if the calculation is impossible or there are no measurements results available.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:INPut:LEVel?')
		return Conversions.str_to_float(response)

	def get_pep(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:DPD:INPut:PEP \n
		Snippet: value: float = driver.source.iq.dpd.inputPy.get_pep() \n
		Queries the measured values the before and after the enabled digital predistortion. \n
			:return: pep: float The query returns -1000 if the calculation is impossible or there are no measurements results available.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:INPut:PEP?')
		return Conversions.str_to_float(response)
