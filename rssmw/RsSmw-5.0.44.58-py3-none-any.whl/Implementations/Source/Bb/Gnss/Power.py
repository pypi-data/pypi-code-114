from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def get_reference(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:POWer:REFerence \n
		Snippet: value: float = driver.source.bb.gnss.power.get_reference() \n
		Sets the power level that is used as a reference for the calculation of the power level of the satellites. \n
			:return: reference_power: float Range: -145 to 20
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:POWer:REFerence?')
		return Conversions.str_to_float(response)

	def set_reference(self, reference_power: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:POWer:REFerence \n
		Snippet: driver.source.bb.gnss.power.set_reference(reference_power = 1.0) \n
		Sets the power level that is used as a reference for the calculation of the power level of the satellites. \n
			:param reference_power: float Range: -145 to 20
		"""
		param = Conversions.decimal_value_to_str(reference_power)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:POWer:REFerence {param}')
