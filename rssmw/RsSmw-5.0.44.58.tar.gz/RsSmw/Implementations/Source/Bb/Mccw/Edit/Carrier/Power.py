from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def get_step(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:MCCW:EDIT:CARRier:POWer:STEP \n
		Snippet: value: float = driver.source.bb.mccw.edit.carrier.power.get_step() \n
		Sets the step width by which the starting power of the carriers in the defined carrier range is incremented. \n
			:return: step: float Range: -80 to 80
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:MCCW:EDIT:CARRier:POWer:STEP?')
		return Conversions.str_to_float(response)

	def set_step(self, step: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:MCCW:EDIT:CARRier:POWer:STEP \n
		Snippet: driver.source.bb.mccw.edit.carrier.power.set_step(step = 1.0) \n
		Sets the step width by which the starting power of the carriers in the defined carrier range is incremented. \n
			:param step: float Range: -80 to 80
		"""
		param = Conversions.decimal_value_to_str(step)
		self._core.io.write(f'SOURce<HwInstance>:BB:MCCW:EDIT:CARRier:POWer:STEP {param}')

	def get_start(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:MCCW:EDIT:CARRier:POWer:[STARt] \n
		Snippet: value: float = driver.source.bb.mccw.edit.carrier.power.get_start() \n
		Sets the power/pahse for the starting carrier. The power of the remaining carriers is stepped up or down by the power
		specified with the [:SOURce<hw>]:BB:MCCW:EDIT:CARRier:POWer:STEP command. \n
			:return: start: float Range: -80 to 0
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:MCCW:EDIT:CARRier:POWer:STARt?')
		return Conversions.str_to_float(response)

	def set_start(self, start: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:MCCW:EDIT:CARRier:POWer:[STARt] \n
		Snippet: driver.source.bb.mccw.edit.carrier.power.set_start(start = 1.0) \n
		Sets the power/pahse for the starting carrier. The power of the remaining carriers is stepped up or down by the power
		specified with the [:SOURce<hw>]:BB:MCCW:EDIT:CARRier:POWer:STEP command. \n
			:param start: float Range: -80 to 0
		"""
		param = Conversions.decimal_value_to_str(start)
		self._core.io.write(f'SOURce<HwInstance>:BB:MCCW:EDIT:CARRier:POWer:STARt {param}')
