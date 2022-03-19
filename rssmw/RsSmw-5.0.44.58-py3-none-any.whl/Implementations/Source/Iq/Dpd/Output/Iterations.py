from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iterations:
	"""Iterations commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iterations", core, parent)

	def get_max(self) -> int:
		"""SCPI: [SOURce<HW>]:IQ:DPD:OUTPut:ITERations:MAX \n
		Snippet: value: int = driver.source.iq.dpd.output.iterations.get_max() \n
		Sets the maximum number of performed iterations to achieving the required error set with
		[:SOURce<hw>]:IQ:DPD:OUTPut:ERRor:MAX. \n
			:return: max_iterations: integer Range: 1 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:OUTPut:ITERations:MAX?')
		return Conversions.str_to_int(response)

	def set_max(self, max_iterations: int) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DPD:OUTPut:ITERations:MAX \n
		Snippet: driver.source.iq.dpd.output.iterations.set_max(max_iterations = 1) \n
		Sets the maximum number of performed iterations to achieving the required error set with
		[:SOURce<hw>]:IQ:DPD:OUTPut:ERRor:MAX. \n
			:param max_iterations: integer Range: 1 to 10
		"""
		param = Conversions.decimal_value_to_str(max_iterations)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DPD:OUTPut:ITERations:MAX {param}')
