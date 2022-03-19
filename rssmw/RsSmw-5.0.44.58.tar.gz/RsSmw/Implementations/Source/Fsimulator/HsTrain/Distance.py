from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Distance:
	"""Distance commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("distance", core, parent)

	def get_minimum(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:HSTRain:DISTance:MINimum \n
		Snippet: value: float = driver.source.fsimulator.hsTrain.distance.get_minimum() \n
		Sets the parameter Dmin, i.e. the distance between the BS and the railway track. \n
			:return: minimum: float Range: 1 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:HSTRain:DISTance:MINimum?')
		return Conversions.str_to_float(response)

	def set_minimum(self, minimum: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:HSTRain:DISTance:MINimum \n
		Snippet: driver.source.fsimulator.hsTrain.distance.set_minimum(minimum = 1.0) \n
		Sets the parameter Dmin, i.e. the distance between the BS and the railway track. \n
			:param minimum: float Range: 1 to 100
		"""
		param = Conversions.decimal_value_to_str(minimum)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:HSTRain:DISTance:MINimum {param}')

	def get_start(self) -> int:
		"""SCPI: [SOURce<HW>]:FSIMulator:HSTRain:DISTance:STARt \n
		Snippet: value: int = driver.source.fsimulator.hsTrain.distance.get_start() \n
		Sets the parameter DS, i.e. the initial distance DS/2 between the train and the BS at the beginning of the simulation. \n
			:return: start: integer Range: 20 to 2000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:HSTRain:DISTance:STARt?')
		return Conversions.str_to_int(response)

	def set_start(self, start: int) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:HSTRain:DISTance:STARt \n
		Snippet: driver.source.fsimulator.hsTrain.distance.set_start(start = 1) \n
		Sets the parameter DS, i.e. the initial distance DS/2 between the train and the BS at the beginning of the simulation. \n
			:param start: integer Range: 20 to 2000
		"""
		param = Conversions.decimal_value_to_str(start)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:HSTRain:DISTance:STARt {param}')
