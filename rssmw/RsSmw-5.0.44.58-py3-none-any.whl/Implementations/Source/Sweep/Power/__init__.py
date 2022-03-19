from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 10 total commands, 3 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def execute(self):
		"""execute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_execute'):
			from .Execute import Execute
			self._execute = Execute(self._core, self._cmd_group)
		return self._execute

	@property
	def spacing(self):
		"""spacing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spacing'):
			from .Spacing import Spacing
			self._spacing = Spacing(self._core, self._cmd_group)
		return self._spacing

	@property
	def step(self):
		"""step commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_step'):
			from .Step import Step
			self._step = Step(self._core, self._cmd_group)
		return self._step

	# noinspection PyTypeChecker
	def get_amode(self) -> enums.PowerAttMode:
		"""SCPI: [SOURce<HW>]:SWEep:POWer:AMODe \n
		Snippet: value: enums.PowerAttMode = driver.source.sweep.power.get_amode() \n
		Selects the power attenuator mode for the level sweep. \n
			:return: amode: NORMal| HPOWer NORMal Performs the level settings in the range of the built-in attenuator. HPOWer Performs the level settings in the high level range.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:POWer:AMODe?')
		return Conversions.str_to_scalar_enum(response, enums.PowerAttMode)

	def set_amode(self, amode: enums.PowerAttMode) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:POWer:AMODe \n
		Snippet: driver.source.sweep.power.set_amode(amode = enums.PowerAttMode.AUTO) \n
		Selects the power attenuator mode for the level sweep. \n
			:param amode: NORMal| HPOWer NORMal Performs the level settings in the range of the built-in attenuator. HPOWer Performs the level settings in the high level range.
		"""
		param = Conversions.enum_scalar_to_str(amode, enums.PowerAttMode)
		self._core.io.write(f'SOURce<HwInstance>:SWEep:POWer:AMODe {param}')

	def get_dwell(self) -> float:
		"""SCPI: [SOURce<HW>]:SWEep:POWer:DWELl \n
		Snippet: value: float = driver.source.sweep.power.get_dwell() \n
		Sets the dwell time for a level sweep step. \n
			:return: dwell: float Range: 0.001 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:POWer:DWELl?')
		return Conversions.str_to_float(response)

	def set_dwell(self, dwell: float) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:POWer:DWELl \n
		Snippet: driver.source.sweep.power.set_dwell(dwell = 1.0) \n
		Sets the dwell time for a level sweep step. \n
			:param dwell: float Range: 0.001 to 100
		"""
		param = Conversions.decimal_value_to_str(dwell)
		self._core.io.write(f'SOURce<HwInstance>:SWEep:POWer:DWELl {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.AutoManStep:
		"""SCPI: [SOURce<HW>]:SWEep:POWer:MODE \n
		Snippet: value: enums.AutoManStep = driver.source.sweep.power.get_mode() \n
		Sets the cycle mode for the level sweep. \n
			:return: mode: AUTO| MANual| STEP AUTO Each trigger triggers exactly one complete sweep. MANual The trigger system is not active. You can trigger every step individually with the command [:SOURcehw]:POWer:MANual. The level value increases at each step by the value that you define with [:SOURcehw]:POWer:STEP[:INCRement]. Values directly entered with the command [:SOURcehw]:POWer:MANual are not taken into account. STEP Each trigger triggers one sweep step only. The level increases by the value entered with [:SOURcehw]:POWer:STEP[:INCRement].
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:POWer:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManStep)

	def set_mode(self, mode: enums.AutoManStep) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:POWer:MODE \n
		Snippet: driver.source.sweep.power.set_mode(mode = enums.AutoManStep.AUTO) \n
		Sets the cycle mode for the level sweep. \n
			:param mode: AUTO| MANual| STEP AUTO Each trigger triggers exactly one complete sweep. MANual The trigger system is not active. You can trigger every step individually with the command [:SOURcehw]:POWer:MANual. The level value increases at each step by the value that you define with [:SOURcehw]:POWer:STEP[:INCRement]. Values directly entered with the command [:SOURcehw]:POWer:MANual are not taken into account. STEP Each trigger triggers one sweep step only. The level increases by the value entered with [:SOURcehw]:POWer:STEP[:INCRement].
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AutoManStep)
		self._core.io.write(f'SOURce<HwInstance>:SWEep:POWer:MODE {param}')

	def get_points(self) -> int:
		"""SCPI: [SOURce<HW>]:SWEep:POWer:POINts \n
		Snippet: value: int = driver.source.sweep.power.get_points() \n
		Sets the number of steps within the RF level sweep range. See 'Correlating parameters in sweep mode'. \n
			:return: points: integer Range: 2 to Max
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:POWer:POINts?')
		return Conversions.str_to_int(response)

	def set_points(self, points: int) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:POWer:POINts \n
		Snippet: driver.source.sweep.power.set_points(points = 1) \n
		Sets the number of steps within the RF level sweep range. See 'Correlating parameters in sweep mode'. \n
			:param points: integer Range: 2 to Max
		"""
		param = Conversions.decimal_value_to_str(points)
		self._core.io.write(f'SOURce<HwInstance>:SWEep:POWer:POINts {param}')

	def get_retrace(self) -> bool:
		"""SCPI: [SOURce<HW>]:SWEep:POWer:RETRace \n
		Snippet: value: bool = driver.source.sweep.power.get_retrace() \n
		Activates that the signal changes to the start frequency value while it is waiting for the next trigger event. You can
		enable this feature, when you are working with sawtooth shapes in sweep mode 'Single' or 'External Single'. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:POWer:RETRace?')
		return Conversions.str_to_bool(response)

	def set_retrace(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:POWer:RETRace \n
		Snippet: driver.source.sweep.power.set_retrace(state = False) \n
		Activates that the signal changes to the start frequency value while it is waiting for the next trigger event. You can
		enable this feature, when you are working with sawtooth shapes in sweep mode 'Single' or 'External Single'. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:SWEep:POWer:RETRace {param}')

	def get_running(self) -> bool:
		"""SCPI: [SOURce<HW>]:SWEep:POWer:RUNNing \n
		Snippet: value: bool = driver.source.sweep.power.get_running() \n
		Queries the current sweep state. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:POWer:RUNNing?')
		return Conversions.str_to_bool(response)

	# noinspection PyTypeChecker
	def get_shape(self) -> enums.SweCyclMode:
		"""SCPI: [SOURce<HW>]:SWEep:POWer:SHAPe \n
		Snippet: value: enums.SweCyclMode = driver.source.sweep.power.get_shape() \n
		Determines the waveform shape for a frequency sweep sequence. \n
			:return: shape: SAWTooth| TRIangle
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:POWer:SHAPe?')
		return Conversions.str_to_scalar_enum(response, enums.SweCyclMode)

	def set_shape(self, shape: enums.SweCyclMode) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:POWer:SHAPe \n
		Snippet: driver.source.sweep.power.set_shape(shape = enums.SweCyclMode.SAWTooth) \n
		Determines the waveform shape for a frequency sweep sequence. \n
			:param shape: SAWTooth| TRIangle
		"""
		param = Conversions.enum_scalar_to_str(shape, enums.SweCyclMode)
		self._core.io.write(f'SOURce<HwInstance>:SWEep:POWer:SHAPe {param}')

	def clone(self) -> 'Power':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Power(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
