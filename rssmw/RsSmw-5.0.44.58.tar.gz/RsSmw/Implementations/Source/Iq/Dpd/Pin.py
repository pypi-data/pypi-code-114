from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pin:
	"""Pin commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pin", core, parent)

	def get_max(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:DPD:PIN:MAX \n
		Snippet: value: float = driver.source.iq.dpd.pin.get_max() \n
		Sets the value range of the input power. \n
			:return: pep_in_max: float Range: -145 to 20
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:PIN:MAX?')
		return Conversions.str_to_float(response)

	def set_max(self, pep_in_max: float) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DPD:PIN:MAX \n
		Snippet: driver.source.iq.dpd.pin.set_max(pep_in_max = 1.0) \n
		Sets the value range of the input power. \n
			:param pep_in_max: float Range: -145 to 20
		"""
		param = Conversions.decimal_value_to_str(pep_in_max)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DPD:PIN:MAX {param}')

	def get_min(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:DPD:PIN:MIN \n
		Snippet: value: float = driver.source.iq.dpd.pin.get_min() \n
		Sets the value range of the input power. \n
			:return: pep_in_min: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:PIN:MIN?')
		return Conversions.str_to_float(response)

	def set_min(self, pep_in_min: float) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DPD:PIN:MIN \n
		Snippet: driver.source.iq.dpd.pin.set_min(pep_in_min = 1.0) \n
		Sets the value range of the input power. \n
			:param pep_in_min: float Range: -145 to 20
		"""
		param = Conversions.decimal_value_to_str(pep_in_min)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DPD:PIN:MIN {param}')
