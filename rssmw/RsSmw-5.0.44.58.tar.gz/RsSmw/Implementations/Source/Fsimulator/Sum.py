from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sum:
	"""Sum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sum", core, parent)

	def get_ratio(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:SUM:RATio \n
		Snippet: value: float = driver.source.fsimulator.sum.get_ratio() \n
		No command help available \n
			:return: ratio: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SUM:RATio?')
		return Conversions.str_to_float(response)

	def set_ratio(self, ratio: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SUM:RATio \n
		Snippet: driver.source.fsimulator.sum.set_ratio(ratio = 1.0) \n
		No command help available \n
			:param ratio: No help available
		"""
		param = Conversions.decimal_value_to_str(ratio)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SUM:RATio {param}')
