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
		"""SCPI: [SOURce<HW>]:BB:IMPairment:QUADrature:[ANGLe] \n
		Snippet: value: float = driver.source.bb.impairment.quadrature.get_angle() \n
		Sets a quadrature offset (phase angle) between the I and Q vectors deviating from the ideal 90 degrees.
		A positive quadrature offset results in a phase angle greater than 90 degrees. \n
			:return: angle: float Range: -10 to 10, Unit: DEG
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:IMPairment:QUADrature:ANGLe?')
		return Conversions.str_to_float(response)

	def set_angle(self, angle: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:IMPairment:QUADrature:[ANGLe] \n
		Snippet: driver.source.bb.impairment.quadrature.set_angle(angle = 1.0) \n
		Sets a quadrature offset (phase angle) between the I and Q vectors deviating from the ideal 90 degrees.
		A positive quadrature offset results in a phase angle greater than 90 degrees. \n
			:param angle: float Range: -10 to 10, Unit: DEG
		"""
		param = Conversions.decimal_value_to_str(angle)
		self._core.io.write(f'SOURce<HwInstance>:BB:IMPairment:QUADrature:ANGLe {param}')
