from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Reference:
	"""Reference commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reference", core, parent)

	def get_delay(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:REFerence:DELay \n
		Snippet: value: float = driver.source.fsimulator.mdelay.reference.get_delay() \n
		This command enters the delay of the reference path for moving propagation. \n
			:return: delay: float Range: 0 to 40E-6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MDELay:REFerence:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, delay: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:REFerence:DELay \n
		Snippet: driver.source.fsimulator.mdelay.reference.set_delay(delay = 1.0) \n
		This command enters the delay of the reference path for moving propagation. \n
			:param delay: float Range: 0 to 40E-6
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MDELay:REFerence:DELay {param}')

	def get_loss(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:REFerence:LOSS \n
		Snippet: value: float = driver.source.fsimulator.mdelay.reference.get_loss() \n
		Sets the loss of the reference path for moving propagation. \n
			:return: loss: float Range: 0 to 50
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MDELay:REFerence:LOSS?')
		return Conversions.str_to_float(response)

	def set_loss(self, loss: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:REFerence:LOSS \n
		Snippet: driver.source.fsimulator.mdelay.reference.set_loss(loss = 1.0) \n
		Sets the loss of the reference path for moving propagation. \n
			:param loss: float Range: 0 to 50
		"""
		param = Conversions.decimal_value_to_str(loss)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MDELay:REFerence:LOSS {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:REFerence:STATe \n
		Snippet: value: bool = driver.source.fsimulator.mdelay.reference.get_state() \n
		This command activates the reference path for moving propagation. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MDELay:REFerence:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:REFerence:STATe \n
		Snippet: driver.source.fsimulator.mdelay.reference.set_state(state = False) \n
		This command activates the reference path for moving propagation. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MDELay:REFerence:STATe {param}')
