from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions
from .. import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Unit:
	"""Unit commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("unit", core, parent)

	# noinspection PyTypeChecker
	def get_angle(self) -> enums.UnitAngle:
		"""SCPI: UNIT:ANGLe \n
		Snippet: value: enums.UnitAngle = driver.unit.get_angle() \n
		Sets the default unit for phase modulation angle. The command affects no other parameters, such as RF phase, or the
		manual control or display. \n
			:return: angle: DEGree| DEGRee| RADian
		"""
		response = self._core.io.query_str('UNIT:ANGLe?')
		return Conversions.str_to_scalar_enum(response, enums.UnitAngle)

	def set_angle(self, angle: enums.UnitAngle) -> None:
		"""SCPI: UNIT:ANGLe \n
		Snippet: driver.unit.set_angle(angle = enums.UnitAngle.DEGree) \n
		Sets the default unit for phase modulation angle. The command affects no other parameters, such as RF phase, or the
		manual control or display. \n
			:param angle: DEGree| DEGRee| RADian
		"""
		param = Conversions.enum_scalar_to_str(angle, enums.UnitAngle)
		self._core.io.write(f'UNIT:ANGLe {param}')

	# noinspection PyTypeChecker
	def get_power(self) -> enums.UnitPower:
		"""SCPI: UNIT:POWer \n
		Snippet: value: enums.UnitPower = driver.unit.get_power() \n
		Sets the default unit for all power parameters. This setting affects the GUI, as well as all remote control commands that
		determine power values. \n
			:return: power: V| DBUV| DBM
		"""
		response = self._core.io.query_str('UNIT:POWer?')
		return Conversions.str_to_scalar_enum(response, enums.UnitPower)

	def set_power(self, power: enums.UnitPower) -> None:
		"""SCPI: UNIT:POWer \n
		Snippet: driver.unit.set_power(power = enums.UnitPower.DBM) \n
		Sets the default unit for all power parameters. This setting affects the GUI, as well as all remote control commands that
		determine power values. \n
			:param power: V| DBUV| DBM
		"""
		param = Conversions.enum_scalar_to_str(power, enums.UnitPower)
		self._core.io.write(f'UNIT:POWer {param}')

	# noinspection PyTypeChecker
	def get_velocity(self) -> enums.UnitSpeed:
		"""SCPI: UNIT:VELocity \n
		Snippet: value: enums.UnitSpeed = driver.unit.get_velocity() \n
		No command help available \n
			:return: velocity: No help available
		"""
		response = self._core.io.query_str('UNIT:VELocity?')
		return Conversions.str_to_scalar_enum(response, enums.UnitSpeed)

	def set_velocity(self, velocity: enums.UnitSpeed) -> None:
		"""SCPI: UNIT:VELocity \n
		Snippet: driver.unit.set_velocity(velocity = enums.UnitSpeed.KMH) \n
		No command help available \n
			:param velocity: No help available
		"""
		param = Conversions.enum_scalar_to_str(velocity, enums.UnitSpeed)
		self._core.io.write(f'UNIT:VELocity {param}')
