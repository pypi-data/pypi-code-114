from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pin:
	"""Pin commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pin", core, parent)

	def get_max(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:PIN:MAX \n
		Snippet: value: float = driver.source.iq.output.analog.envelope.pin.get_max() \n
		Sets the maximum value of the input power Pin. \n
			:return: pin_max: float Range: -145 to 20
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:PIN:MAX?')
		return Conversions.str_to_float(response)

	def set_max(self, pin_max: float) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:PIN:MAX \n
		Snippet: driver.source.iq.output.analog.envelope.pin.set_max(pin_max = 1.0) \n
		Sets the maximum value of the input power Pin. \n
			:param pin_max: float Range: -145 to 20
		"""
		param = Conversions.decimal_value_to_str(pin_max)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:PIN:MAX {param}')

	def get_min(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:PIN:MIN \n
		Snippet: value: float = driver.source.iq.output.analog.envelope.pin.get_min() \n
		Sets the minimum value of the input power Pin. \n
			:return: pin_min: float Range: -145 to 20
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:PIN:MIN?')
		return Conversions.str_to_float(response)

	def set_min(self, pin_min: float) -> None:
		"""SCPI: [SOURce<HW>]:IQ:OUTPut:[ANALog]:ENVelope:PIN:MIN \n
		Snippet: driver.source.iq.output.analog.envelope.pin.set_min(pin_min = 1.0) \n
		Sets the minimum value of the input power Pin. \n
			:param pin_min: float Range: -145 to 20
		"""
		param = Conversions.decimal_value_to_str(pin_min)
		self._core.io.write(f'SOURce<HwInstance>:IQ:OUTPut:ANALog:ENVelope:PIN:MIN {param}')
