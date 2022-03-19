from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HsTrain:
	"""HsTrain commands group definition. 11 total commands, 3 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hsTrain", core, parent)

	@property
	def distance(self):
		"""distance commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_distance'):
			from .Distance import Distance
			self._distance = Distance(self._core, self._cmd_group)
		return self._distance

	@property
	def downlink(self):
		"""downlink commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .Downlink import Downlink
			self._downlink = Downlink(self._core, self._cmd_group)
		return self._downlink

	@property
	def path(self):
		"""path commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_path'):
			from .Path import Path
			self._path = Path(self._core, self._cmd_group)
		return self._path

	def get_fdoppler(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:HSTRain:FDOPpler \n
		Snippet: value: float = driver.source.fsimulator.hsTrain.get_fdoppler() \n
		Queries the maximum Doppler Shift for the selected configuration. \n
			:return: fdoppler: float Range: 0 to 1000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:HSTRain:FDOPpler?')
		return Conversions.str_to_float(response)

	def get_kfactor(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:HSTRain:KFACtor \n
		Snippet: value: float = driver.source.fsimulator.hsTrain.get_kfactor() \n
		Sets the Rician factor K for high speed train scenario 2. \n
			:return: kfactor: float Range: -30 to 30
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:HSTRain:KFACtor?')
		return Conversions.str_to_float(response)

	def set_kfactor(self, kfactor: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:HSTRain:KFACtor \n
		Snippet: driver.source.fsimulator.hsTrain.set_kfactor(kfactor = 1.0) \n
		Sets the Rician factor K for high speed train scenario 2. \n
			:param kfactor: float Range: -30 to 30
		"""
		param = Conversions.decimal_value_to_str(kfactor)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:HSTRain:KFACtor {param}')

	# noinspection PyTypeChecker
	def get_profile(self) -> enums.FadingProfileB:
		"""SCPI: [SOURce<HW>]:FSIMulator:HSTRain:PROFile \n
		Snippet: value: enums.FadingProfileB = driver.source.fsimulator.hsTrain.get_profile() \n
		Determines the fading profile for the selected scenario. The fading profile determines which transmission path is
		simulated. \n
			:return: profile: SPATh| PDOPpler| RAYLeigh
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:HSTRain:PROFile?')
		return Conversions.str_to_scalar_enum(response, enums.FadingProfileB)

	def set_profile(self, profile: enums.FadingProfileB) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:HSTRain:PROFile \n
		Snippet: driver.source.fsimulator.hsTrain.set_profile(profile = enums.FadingProfileB.BELLindoor) \n
		Determines the fading profile for the selected scenario. The fading profile determines which transmission path is
		simulated. \n
			:param profile: SPATh| PDOPpler| RAYLeigh
		"""
		param = Conversions.enum_scalar_to_str(profile, enums.FadingProfileB)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:HSTRain:PROFile {param}')

	def get_soffset(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:HSTRain:SOFFset \n
		Snippet: value: float = driver.source.fsimulator.hsTrain.get_soffset() \n
		No command help available \n
			:return: start_offset: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:HSTRain:SOFFset?')
		return Conversions.str_to_float(response)

	def set_soffset(self, start_offset: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:HSTRain:SOFFset \n
		Snippet: driver.source.fsimulator.hsTrain.set_soffset(start_offset = 1.0) \n
		No command help available \n
			:param start_offset: No help available
		"""
		param = Conversions.decimal_value_to_str(start_offset)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:HSTRain:SOFFset {param}')

	def get_speed(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:HSTRain:SPEed \n
		Snippet: value: float = driver.source.fsimulator.hsTrain.get_speed() \n
		Sets the velocity parameter , i.e. the speed of the moving receiver in m/s. \n
			:return: speed: float Range: 0.001 to dynamic
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:HSTRain:SPEed?')
		return Conversions.str_to_float(response)

	def set_speed(self, speed: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:HSTRain:SPEed \n
		Snippet: driver.source.fsimulator.hsTrain.set_speed(speed = 1.0) \n
		Sets the velocity parameter , i.e. the speed of the moving receiver in m/s. \n
			:param speed: float Range: 0.001 to dynamic
		"""
		param = Conversions.decimal_value_to_str(speed)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:HSTRain:SPEed {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:HSTRain:STATe \n
		Snippet: value: bool = driver.source.fsimulator.hsTrain.get_state() \n
		Activates/deactivates simulation of High Speed Train propagation according to the selected scenario 1 or 3. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:HSTRain:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:HSTRain:STATe \n
		Snippet: driver.source.fsimulator.hsTrain.set_state(state = False) \n
		Activates/deactivates simulation of High Speed Train propagation according to the selected scenario 1 or 3. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:HSTRain:STATe {param}')

	def clone(self) -> 'HsTrain':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = HsTrain(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
