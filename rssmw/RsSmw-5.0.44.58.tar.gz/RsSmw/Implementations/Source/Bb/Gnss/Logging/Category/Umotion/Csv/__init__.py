from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Csv:
	"""Csv commands group definition. 21 total commands, 6 Subgroups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("csv", core, parent)

	@property
	def acceleration(self):
		"""acceleration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_acceleration'):
			from .Acceleration import Acceleration
			self._acceleration = Acceleration(self._core, self._cmd_group)
		return self._acceleration

	@property
	def attitude(self):
		"""attitude commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_attitude'):
			from .Attitude import Attitude
			self._attitude = Attitude(self._core, self._cmd_group)
		return self._attitude

	@property
	def jerk(self):
		"""jerk commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_jerk'):
			from .Jerk import Jerk
			self._jerk = Jerk(self._core, self._cmd_group)
		return self._jerk

	@property
	def position(self):
		"""position commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_position'):
			from .Position import Position
			self._position = Position(self._core, self._cmd_group)
		return self._position

	@property
	def select(self):
		"""select commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_select'):
			from .Select import Select
			self._select = Select(self._core, self._cmd_group)
		return self._select

	@property
	def velocity(self):
		"""velocity commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_velocity'):
			from .Velocity import Velocity
			self._velocity = Velocity(self._core, self._cmd_group)
		return self._velocity

	def get_aoffset(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:AOFFset \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.umotion.csv.get_aoffset() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:AOFFset?')
		return Conversions.str_to_bool(response)

	def set_aoffset(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:AOFFset \n
		Snippet: driver.source.bb.gnss.logging.category.umotion.csv.set_aoffset(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:AOFFset {param}')

	def get_gdop(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:GDOP \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.umotion.csv.get_gdop() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:GDOP?')
		return Conversions.str_to_bool(response)

	def set_gdop(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:GDOP \n
		Snippet: driver.source.bb.gnss.logging.category.umotion.csv.set_gdop(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:GDOP {param}')

	def get_gspeed(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:GSPeed \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.umotion.csv.get_gspeed() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:GSPeed?')
		return Conversions.str_to_bool(response)

	def set_gspeed(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:GSPeed \n
		Snippet: driver.source.bb.gnss.logging.category.umotion.csv.set_gspeed(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:GSPeed {param}')

	def get_hdop(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:HDOP \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.umotion.csv.get_hdop() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:HDOP?')
		return Conversions.str_to_bool(response)

	def set_hdop(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:HDOP \n
		Snippet: driver.source.bb.gnss.logging.category.umotion.csv.set_hdop(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:HDOP {param}')

	def get_pdop(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:PDOP \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.umotion.csv.get_pdop() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:PDOP?')
		return Conversions.str_to_bool(response)

	def set_pdop(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:PDOP \n
		Snippet: driver.source.bb.gnss.logging.category.umotion.csv.set_pdop(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:PDOP {param}')

	def get_svs(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:SVS \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.umotion.csv.get_svs() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:SVS?')
		return Conversions.str_to_bool(response)

	def set_svs(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:SVS \n
		Snippet: driver.source.bb.gnss.logging.category.umotion.csv.set_svs(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:SVS {param}')

	def get_tdop(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:TDOP \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.umotion.csv.get_tdop() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:TDOP?')
		return Conversions.str_to_bool(response)

	def set_tdop(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:TDOP \n
		Snippet: driver.source.bb.gnss.logging.category.umotion.csv.set_tdop(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:TDOP {param}')

	def get_vdop(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:VDOP \n
		Snippet: value: bool = driver.source.bb.gnss.logging.category.umotion.csv.get_vdop() \n
		Enables the parameter for logging. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:VDOP?')
		return Conversions.str_to_bool(response)

	def set_vdop(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:CATegory:UMOTion:[CSV]:VDOP \n
		Snippet: driver.source.bb.gnss.logging.category.umotion.csv.set_vdop(state = False) \n
		Enables the parameter for logging. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:CATegory:UMOTion:CSV:VDOP {param}')

	def clone(self) -> 'Csv':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Csv(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
