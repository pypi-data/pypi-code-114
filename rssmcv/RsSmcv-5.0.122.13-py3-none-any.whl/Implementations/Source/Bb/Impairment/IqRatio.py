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
		"""SCPI: [SOURce<HW>]:BB:IMPairment:IQRatio:[MAGNitude] \n
		Snippet: value: float = driver.source.bb.impairment.iqRatio.get_magnitude() \n
		No command help available \n
			:return: ipartq_ratio: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:IMPairment:IQRatio:MAGNitude?')
		return Conversions.str_to_float(response)

	def set_magnitude(self, ipartq_ratio: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:IMPairment:IQRatio:[MAGNitude] \n
		Snippet: driver.source.bb.impairment.iqRatio.set_magnitude(ipartq_ratio = 1.0) \n
		No command help available \n
			:param ipartq_ratio: float Range: -1 to 1
		"""
		param = Conversions.decimal_value_to_str(ipartq_ratio)
		self._core.io.write(f'SOURce<HwInstance>:BB:IMPairment:IQRatio:MAGNitude {param}')
