from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Speed:
	"""Speed commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("speed", core, parent)

	# noinspection PyTypeChecker
	def get_unit(self) -> enums.UnitSpeed:
		"""SCPI: [SOURce<HW>]:FSIMulator:SPEed:UNIT \n
		Snippet: value: enums.UnitSpeed = driver.source.fsimulator.speed.get_unit() \n
		This command chooses the default unit for the parameter speed as displayed in the dialog. Note: The remote control
		command changes only the units displayed in the graphical user interface. While configuring the speed via remote control,
		the speed units must be specified. \n
			:return: unit: MPS| KMH| MPH| NMPH
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SPEed:UNIT?')
		return Conversions.str_to_scalar_enum(response, enums.UnitSpeed)

	def set_unit(self, unit: enums.UnitSpeed) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SPEed:UNIT \n
		Snippet: driver.source.fsimulator.speed.set_unit(unit = enums.UnitSpeed.KMH) \n
		This command chooses the default unit for the parameter speed as displayed in the dialog. Note: The remote control
		command changes only the units displayed in the graphical user interface. While configuring the speed via remote control,
		the speed units must be specified. \n
			:param unit: MPS| KMH| MPH| NMPH
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.UnitSpeed)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SPEed:UNIT {param}')
