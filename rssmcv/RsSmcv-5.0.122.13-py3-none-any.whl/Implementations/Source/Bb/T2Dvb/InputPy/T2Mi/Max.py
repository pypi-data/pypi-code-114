from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Max:
	"""Max commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("max", core, parent)

	def get_t_1(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut:T2MI:MAX:T1 \n
		Snippet: value: float = driver.source.bb.t2Dvb.inputPy.t2Mi.max.get_t_1() \n
		Queries the current value of the maximum time parameters Tmax1/Tmax2/Tmax3/Tmax4. \n
			:return: max_t_1: float Range: -99.999999 to 99.999999, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INPut:T2MI:MAX:T1?')
		return Conversions.str_to_float(response)

	def get_t_2(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut:T2MI:MAX:T2 \n
		Snippet: value: float = driver.source.bb.t2Dvb.inputPy.t2Mi.max.get_t_2() \n
		Queries the current value of the maximum time parameters Tmax1/Tmax2/Tmax3/Tmax4. \n
			:return: max_t_2: float Range: -99.999999 to 99.999999, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INPut:T2MI:MAX:T2?')
		return Conversions.str_to_float(response)

	def get_t_3(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut:T2MI:MAX:T3 \n
		Snippet: value: float = driver.source.bb.t2Dvb.inputPy.t2Mi.max.get_t_3() \n
		Queries the current value of the maximum time parameters Tmax1/Tmax2/Tmax3/Tmax4. \n
			:return: max_t_3: float Range: -99.999999 to 99.999999, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INPut:T2MI:MAX:T3?')
		return Conversions.str_to_float(response)

	def get_t_4(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut:T2MI:MAX:T4 \n
		Snippet: value: float = driver.source.bb.t2Dvb.inputPy.t2Mi.max.get_t_4() \n
		Queries the current value of the maximum time parameters Tmax1/Tmax2/Tmax3/Tmax4. \n
			:return: max_t_4: float Range: -99.999999 to 99.999999, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INPut:T2MI:MAX:T4?')
		return Conversions.str_to_float(response)
