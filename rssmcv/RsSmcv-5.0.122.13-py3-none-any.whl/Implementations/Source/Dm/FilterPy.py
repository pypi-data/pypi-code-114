from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPy:
	"""FilterPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("filterPy", core, parent)

	def get_parameter(self) -> float:
		"""SCPI: [SOURce<HW>]:DM:FILTer:PARameter \n
		Snippet: value: float = driver.source.dm.filterPy.get_parameter() \n
		Sets the filter parameter of the currently selected filter type.
		To set the filter type, use command [:SOURce<hw>]:BB:DM:FILTer:TYPE. \n
			:return: parameter: float Range: 0.05 to 2.5
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:DM:FILTer:PARameter?')
		return Conversions.str_to_float(response)

	def set_parameter(self, parameter: float) -> None:
		"""SCPI: [SOURce<HW>]:DM:FILTer:PARameter \n
		Snippet: driver.source.dm.filterPy.set_parameter(parameter = 1.0) \n
		Sets the filter parameter of the currently selected filter type.
		To set the filter type, use command [:SOURce<hw>]:BB:DM:FILTer:TYPE. \n
			:param parameter: float Range: 0.05 to 2.5
		"""
		param = Conversions.decimal_value_to_str(parameter)
		self._core.io.write(f'SOURce<HwInstance>:DM:FILTer:PARameter {param}')
