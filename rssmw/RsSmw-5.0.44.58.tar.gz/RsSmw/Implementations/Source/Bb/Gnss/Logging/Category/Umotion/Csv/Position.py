from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Position:
	"""Position commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("position", core, parent)

	def get_ecef(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:POSition:ECEF \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.umotion.csv.position.get_ecef() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:POSition:ECEF?')
		return Conversions.str_to_bool(response)

	def set_ecef(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:POSition:ECEF \n
		Snippet: driver.source.bb.gnss.logging.category.umotion.csv.position.set_ecef(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:POSition:ECEF {param}')

	def get_enu(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:POSition:ENU \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.umotion.csv.position.get_enu() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:POSition:ENU?')
		return Conversions.str_to_bool(response)

	def set_enu(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:POSition:ENU \n
		Snippet: driver.source.bb.gnss.logging.category.umotion.csv.position.set_enu(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:POSition:ENU {param}')

	def get_lla(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:POSition:LLA \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.umotion.csv.position.get_lla() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:POSition:LLA?')
		return Conversions.str_to_bool(response)

	def set_lla(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:POSition:LLA \n
		Snippet: driver.source.bb.gnss.logging.category.umotion.csv.position.set_lla(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:POSition:LLA {param}')
