from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Min:
	"""Min commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("min", core, parent)

	def get_t_1(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut:T2MI:MIN:T1 \n
		Snippet: value: float = driver.source.bb.t2Dvb.inputPy.t2Mi.min.get_t_1() \n
		Queries the current value of minimum time parameters Tmin1/Tmin2/Tmin3. \n
			:return: min_t_1: float Range: -99.999999 to 99.999999, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INPut:T2MI:MIN:T1?')
		return Conversions.str_to_float(response)

	def get_t_2(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut:T2MI:MIN:T2 \n
		Snippet: value: float = driver.source.bb.t2Dvb.inputPy.t2Mi.min.get_t_2() \n
		Queries the current value of minimum time parameters Tmin1/Tmin2/Tmin3. \n
			:return: min_t_2: float Range: -99.999999 to 99.999999, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INPut:T2MI:MIN:T2?')
		return Conversions.str_to_float(response)

	def get_t_3(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut:T2MI:MIN:T3 \n
		Snippet: value: float = driver.source.bb.t2Dvb.inputPy.t2Mi.min.get_t_3() \n
		Queries the current value of minimum time parameters Tmin1/Tmin2/Tmin3. \n
			:return: min_t_3: float Range: -99.999999 to 99.999999, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INPut:T2MI:MIN:T3?')
		return Conversions.str_to_float(response)
