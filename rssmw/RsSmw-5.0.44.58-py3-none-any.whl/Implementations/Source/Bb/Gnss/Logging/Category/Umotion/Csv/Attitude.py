from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Attitude:
	"""Attitude commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("attitude", core, parent)

	def get_acceleration(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:ATTitude:ACCeleration \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.umotion.csv.attitude.get_acceleration() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:ATTitude:ACCeleration?')
		return Conversions.str_to_bool(response)

	def set_acceleration(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:ATTitude:ACCeleration \n
		Snippet: driver.source.bb.gnss.logging.category.umotion.csv.attitude.set_acceleration(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:ATTitude:ACCeleration {param}')

	def get_jerk(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:ATTitude:JERK \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.umotion.csv.attitude.get_jerk() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:ATTitude:JERK?')
		return Conversions.str_to_bool(response)

	def set_jerk(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:ATTitude:JERK \n
		Snippet: driver.source.bb.gnss.logging.category.umotion.csv.attitude.set_jerk(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:ATTitude:JERK {param}')

	def get_rate(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:ATTitude:RATE \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.umotion.csv.attitude.get_rate() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:ATTitude:RATE?')
		return Conversions.str_to_bool(response)

	def set_rate(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:ATTitude:RATE \n
		Snippet: driver.source.bb.gnss.logging.category.umotion.csv.attitude.set_rate(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:ATTitude:RATE {param}')

	def get_value(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:ATTitude \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.umotion.csv.attitude.get_value() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:ATTitude?')
		return Conversions.str_to_bool(response)

	def set_value(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:ATTitude \n
		Snippet: driver.source.bb.gnss.logging.category.umotion.csv.attitude.set_value(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:ATTitude {param}')
