from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqRatio:
	"""IqRatio commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqRatio", core, parent)

	def get_magnitude(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:IMPairment:IQRatio:[MAGNitude] \n
		Snippet: value: float = driver.source.iq.impairment.iqRatio.get_magnitude() \n
		No command help available \n
			:return: magnitude: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:IMPairment:IQRatio:MAGNitude?')
		return Conversions.str_to_float(response)

	def set_magnitude(self, magnitude: float) -> None:
		"""SCPI: [SOURce<HW>]:IQ:IMPairment:IQRatio:[MAGNitude] \n
		Snippet: driver.source.iq.impairment.iqRatio.set_magnitude(magnitude = 1.0) \n
		No command help available \n
			:param magnitude: No help available
		"""
		param = Conversions.decimal_value_to_str(magnitude)
		self._core.io.write(f'SOURce<HwInstance>:IQ:IMPairment:IQRatio:MAGNitude {param}')
