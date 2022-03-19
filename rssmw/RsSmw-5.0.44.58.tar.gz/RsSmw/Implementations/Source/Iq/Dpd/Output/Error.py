from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Error:
	"""Error commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("error", core, parent)

	def get_max(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:DPD:OUTPut:ERRor:MAX \n
		Snippet: value: float = driver.source.iq.dpd.output.error.get_max() \n
		Sets the allowed maximum error. \n
			:return: maximum_error: float Range: 0.01 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:OUTPut:ERRor:MAX?')
		return Conversions.str_to_float(response)

	def set_max(self, maximum_error: float) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DPD:OUTPut:ERRor:MAX \n
		Snippet: driver.source.iq.dpd.output.error.set_max(maximum_error = 1.0) \n
		Sets the allowed maximum error. \n
			:param maximum_error: float Range: 0.01 to 1
		"""
		param = Conversions.decimal_value_to_str(maximum_error)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DPD:OUTPut:ERRor:MAX {param}')

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:DPD:OUTPut:ERRor \n
		Snippet: value: float = driver.source.iq.dpd.output.error.get_value() \n
		Queries the resulting level error. \n
			:return: achieved_error: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:OUTPut:ERRor?')
		return Conversions.str_to_float(response)
