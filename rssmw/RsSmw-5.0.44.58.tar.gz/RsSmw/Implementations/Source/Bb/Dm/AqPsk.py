from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AqPsk:
	"""AqPsk commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aqPsk", core, parent)

	def get_angle(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DM:AQPSk:ANGLe \n
		Snippet: value: float = driver.source.bb.dm.aqPsk.get_angle() \n
		For AQPSK modulation, sets the angle alpha between the point (0,0) and the I axis. \n
			:return: angle: float Range: 0 to 180, Unit: Deg
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:AQPSk:ANGLe?')
		return Conversions.str_to_float(response)

	def set_angle(self, angle: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:AQPSk:ANGLe \n
		Snippet: driver.source.bb.dm.aqPsk.set_angle(angle = 1.0) \n
		For AQPSK modulation, sets the angle alpha between the point (0,0) and the I axis. \n
			:param angle: float Range: 0 to 180, Unit: Deg
		"""
		param = Conversions.decimal_value_to_str(angle)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:AQPSk:ANGLe {param}')
