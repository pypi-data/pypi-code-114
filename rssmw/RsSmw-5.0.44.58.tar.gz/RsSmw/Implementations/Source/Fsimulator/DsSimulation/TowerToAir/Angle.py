from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Angle:
	"""Angle commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("angle", core, parent)

	def get_climb(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:ANGLe:CLIMb \n
		Snippet: value: float = driver.source.fsimulator.dsSimulation.towerToAir.angle.get_climb() \n
		No command help available \n
			:return: angle_climb: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:ANGLe:CLIMb?')
		return Conversions.str_to_float(response)

	def set_climb(self, angle_climb: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:ANGLe:CLIMb \n
		Snippet: driver.source.fsimulator.dsSimulation.towerToAir.angle.set_climb(angle_climb = 1.0) \n
		No command help available \n
			:param angle_climb: No help available
		"""
		param = Conversions.decimal_value_to_str(angle_climb)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:ANGLe:CLIMb {param}')

	def get_descent(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:ANGLe:DESCent \n
		Snippet: value: float = driver.source.fsimulator.dsSimulation.towerToAir.angle.get_descent() \n
		No command help available \n
			:return: angle_descent: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:ANGLe:DESCent?')
		return Conversions.str_to_float(response)

	def set_descent(self, angle_descent: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:ANGLe:DESCent \n
		Snippet: driver.source.fsimulator.dsSimulation.towerToAir.angle.set_descent(angle_descent = 1.0) \n
		No command help available \n
			:param angle_descent: No help available
		"""
		param = Conversions.decimal_value_to_str(angle_descent)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:ANGLe:DESCent {param}')
