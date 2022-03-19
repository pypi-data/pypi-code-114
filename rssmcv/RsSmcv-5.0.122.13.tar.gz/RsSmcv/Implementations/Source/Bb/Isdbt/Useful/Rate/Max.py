from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Max:
	"""Max commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("max", core, parent)

	def get_a(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:USEFul:[RATE]:MAX:A \n
		Snippet: value: int = driver.source.bb.isdbt.useful.rate.max.get_a() \n
		Displays the maximum useful data rate in the specific layer. \n
			:return: max_use_drate_a: integer Range: 0 to 999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:USEFul:RATE:MAX:A?')
		return Conversions.str_to_int(response)

	def get_b(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:USEFul:[RATE]:MAX:B \n
		Snippet: value: int = driver.source.bb.isdbt.useful.rate.max.get_b() \n
		Displays the maximum useful data rate in the specific layer. \n
			:return: max_use_drate_b: integer Range: 0 to 999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:USEFul:RATE:MAX:B?')
		return Conversions.str_to_int(response)

	def get_c(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:USEFul:[RATE]:MAX:C \n
		Snippet: value: int = driver.source.bb.isdbt.useful.rate.max.get_c() \n
		Displays the maximum useful data rate in the specific layer. \n
			:return: max_use_drate_c: integer Range: 0 to 999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:USEFul:RATE:MAX:C?')
		return Conversions.str_to_int(response)
