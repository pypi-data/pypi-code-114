from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Unit:
	"""Unit commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("unit", core, parent)

	# noinspection PyTypeChecker
	def get_angle(self) -> enums.UnitAngle:
		"""SCPI: [SOURce<HW>]:REGenerator:UNIT:ANGLe \n
		Snippet: value: enums.UnitAngle = driver.source.regenerator.unit.get_angle() \n
		Sets the default unit for the parameter as displayed in the dialog. Note: This command changes only the units displayed
		in the graphical user interface. While configuring the angle via remote control, the angle units must be specified. \n
			:return: unit: DEGree| DEGRee| RADian
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:UNIT:ANGLe?')
		return Conversions.str_to_scalar_enum(response, enums.UnitAngle)

	def set_angle(self, unit: enums.UnitAngle) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:UNIT:ANGLe \n
		Snippet: driver.source.regenerator.unit.set_angle(unit = enums.UnitAngle.DEGree) \n
		Sets the default unit for the parameter as displayed in the dialog. Note: This command changes only the units displayed
		in the graphical user interface. While configuring the angle via remote control, the angle units must be specified. \n
			:param unit: DEGree| DEGRee| RADian
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.UnitAngle)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:UNIT:ANGLe {param}')

	# noinspection PyTypeChecker
	def get_length(self) -> enums.UnitLengthReg:
		"""SCPI: [SOURce<HW>]:REGenerator:UNIT:LENGth \n
		Snippet: value: enums.UnitLengthReg = driver.source.regenerator.unit.get_length() \n
		Sets the default unit for the parameter as displayed in the dialog. Note: This command changes only the units displayed
		in the graphical user interface. While configuring the range or the distance via remote control, the units must be
		specified. \n
			:return: unit: MI| NM| KM| M
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:UNIT:LENGth?')
		return Conversions.str_to_scalar_enum(response, enums.UnitLengthReg)

	def set_length(self, unit: enums.UnitLengthReg) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:UNIT:LENGth \n
		Snippet: driver.source.regenerator.unit.set_length(unit = enums.UnitLengthReg.KM) \n
		Sets the default unit for the parameter as displayed in the dialog. Note: This command changes only the units displayed
		in the graphical user interface. While configuring the range or the distance via remote control, the units must be
		specified. \n
			:param unit: MI| NM| KM| M
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.UnitLengthReg)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:UNIT:LENGth {param}')

	# noinspection PyTypeChecker
	def get_velocity(self) -> enums.UnitSpeed:
		"""SCPI: [SOURce<HW>]:REGenerator:UNIT:VELocity \n
		Snippet: value: enums.UnitSpeed = driver.source.regenerator.unit.get_velocity() \n
		Sets the default unit for the parameter as displayed in the dialog. Note: This command changes only the units displayed
		in the graphical user interface. While configuring the velocity via remote control, the velocity units must be specified. \n
			:return: unit: MPS| KMH| MPH| NMPH
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:UNIT:VELocity?')
		return Conversions.str_to_scalar_enum(response, enums.UnitSpeed)

	def set_velocity(self, unit: enums.UnitSpeed) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:UNIT:VELocity \n
		Snippet: driver.source.regenerator.unit.set_velocity(unit = enums.UnitSpeed.KMH) \n
		Sets the default unit for the parameter as displayed in the dialog. Note: This command changes only the units displayed
		in the graphical user interface. While configuring the velocity via remote control, the velocity units must be specified. \n
			:param unit: MPS| KMH| MPH| NMPH
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.UnitSpeed)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:UNIT:VELocity {param}')
