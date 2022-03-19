from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Quadrature:
	"""Quadrature commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("quadrature", core, parent)

	def get_angle(self) -> float:
		"""SCPI: [SOURce<HW>]:IQ:IMPairment:QUADrature:[ANGLe] \n
		Snippet: value: float = driver.source.iq.impairment.quadrature.get_angle() \n
		No command help available \n
			:return: angle: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:IMPairment:QUADrature:ANGLe?')
		return Conversions.str_to_float(response)

	def set_angle(self, angle: float) -> None:
		"""SCPI: [SOURce<HW>]:IQ:IMPairment:QUADrature:[ANGLe] \n
		Snippet: driver.source.iq.impairment.quadrature.set_angle(angle = 1.0) \n
		No command help available \n
			:param angle: No help available
		"""
		param = Conversions.decimal_value_to_str(angle)
		self._core.io.write(f'SOURce<HwInstance>:IQ:IMPairment:QUADrature:ANGLe {param}')
