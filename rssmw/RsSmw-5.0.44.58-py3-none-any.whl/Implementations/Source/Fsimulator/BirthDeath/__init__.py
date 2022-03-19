from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BirthDeath:
	"""BirthDeath commands group definition. 13 total commands, 3 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("birthDeath", core, parent)

	@property
	def delay(self):
		"""delay commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_delay'):
			from .Delay import Delay
			self._delay = Delay(self._core, self._cmd_group)
		return self._delay

	@property
	def hopping(self):
		"""hopping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hopping'):
			from .Hopping import Hopping
			self._hopping = Hopping(self._core, self._cmd_group)
		return self._hopping

	@property
	def path(self):
		"""path commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_path'):
			from .Path import Path
			self._path = Path(self._core, self._cmd_group)
		return self._path

	def get_fratio(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:BIRThdeath:FRATio \n
		Snippet: value: float = driver.source.fsimulator.birthDeath.get_fratio() \n
		Sets the ratio of the actual Doppler frequency to the set Doppler frequency with birth death propagation fading. \n
			:return: fratio: float Range: -1 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:BIRThdeath:FRATio?')
		return Conversions.str_to_float(response)

	def set_fratio(self, fratio: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:BIRThdeath:FRATio \n
		Snippet: driver.source.fsimulator.birthDeath.set_fratio(fratio = 1.0) \n
		Sets the ratio of the actual Doppler frequency to the set Doppler frequency with birth death propagation fading. \n
			:param fratio: float Range: -1 to 1
		"""
		param = Conversions.decimal_value_to_str(fratio)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:BIRThdeath:FRATio {param}')

	def get_positions(self) -> int:
		"""SCPI: [SOURce<HW>]:FSIMulator:BIRThdeath:POSitions \n
		Snippet: value: int = driver.source.fsimulator.birthDeath.get_positions() \n
		Sets the number of possible hop positions in the delay range. 0 us < (...:BIRT:POS – 1) x ...:DEL:GRID + ...:DEL:MIN < 40
		us \n
			:return: positions: integer Range: 3 to 50
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:BIRThdeath:POSitions?')
		return Conversions.str_to_int(response)

	def set_positions(self, positions: int) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:BIRThdeath:POSitions \n
		Snippet: driver.source.fsimulator.birthDeath.set_positions(positions = 1) \n
		Sets the number of possible hop positions in the delay range. 0 us < (...:BIRT:POS – 1) x ...:DEL:GRID + ...:DEL:MIN < 40
		us \n
			:param positions: integer Range: 3 to 50
		"""
		param = Conversions.decimal_value_to_str(positions)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:BIRThdeath:POSitions {param}')

	def get_soffset(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:BIRThdeath:SOFFset \n
		Snippet: value: float = driver.source.fsimulator.birthDeath.get_soffset() \n
		Sets the time until the start of the next birth death event. With dual-channel fading, this allows the user to
		intentionally displace the birth death events of the two faders with respect to one another. \n
			:return: soffset: float Range: 0 to 429
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:BIRThdeath:SOFFset?')
		return Conversions.str_to_float(response)

	def set_soffset(self, soffset: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:BIRThdeath:SOFFset \n
		Snippet: driver.source.fsimulator.birthDeath.set_soffset(soffset = 1.0) \n
		Sets the time until the start of the next birth death event. With dual-channel fading, this allows the user to
		intentionally displace the birth death events of the two faders with respect to one another. \n
			:param soffset: float Range: 0 to 429
		"""
		param = Conversions.decimal_value_to_str(soffset)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:BIRThdeath:SOFFset {param}')

	def get_speed(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:BIRThdeath:SPEed \n
		Snippet: value: float = driver.source.fsimulator.birthDeath.get_speed() \n
		Sets the speed of the moving receiver for birth death propagation. The default speed unit is m/s. Units different than
		the default one must be specified. \n
			:return: speed: float Range: 0 to dynamic, Unit: m/s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:BIRThdeath:SPEed?')
		return Conversions.str_to_float(response)

	def set_speed(self, speed: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:BIRThdeath:SPEed \n
		Snippet: driver.source.fsimulator.birthDeath.set_speed(speed = 1.0) \n
		Sets the speed of the moving receiver for birth death propagation. The default speed unit is m/s. Units different than
		the default one must be specified. \n
			:param speed: float Range: 0 to dynamic, Unit: m/s
		"""
		param = Conversions.decimal_value_to_str(speed)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:BIRThdeath:SPEed {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:BIRThdeath:STATe \n
		Snippet: value: bool = driver.source.fsimulator.birthDeath.get_state() \n
		This command selects the birth death propagation fading configuration and switches the fading simulation on and off. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:BIRThdeath:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:BIRThdeath:STATe \n
		Snippet: driver.source.fsimulator.birthDeath.set_state(state = False) \n
		This command selects the birth death propagation fading configuration and switches the fading simulation on and off. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:BIRThdeath:STATe {param}')

	def clone(self) -> 'BirthDeath':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BirthDeath(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
