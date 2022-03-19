from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 10 total commands, 2 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	@property
	def execute(self):
		"""execute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_execute'):
			from .Execute import Execute
			self._execute = Execute(self._core, self._cmd_group)
		return self._execute

	@property
	def step(self):
		"""step commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_step'):
			from .Step import Step
			self._step = Step(self._core, self._cmd_group)
		return self._step

	def get_dwell(self) -> float:
		"""SCPI: [SOURce<HW>]:LFOutput:SWEep:[FREQuency]:DWELl \n
		Snippet: value: float = driver.source.lfOutput.sweep.frequency.get_dwell() \n
		Sets the dwell time for each frequency step of the sweep. \n
			:return: dwell: float Range: 0.001 to 100, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LFOutput:SWEep:FREQuency:DWELl?')
		return Conversions.str_to_float(response)

	def set_dwell(self, dwell: float) -> None:
		"""SCPI: [SOURce<HW>]:LFOutput:SWEep:[FREQuency]:DWELl \n
		Snippet: driver.source.lfOutput.sweep.frequency.set_dwell(dwell = 1.0) \n
		Sets the dwell time for each frequency step of the sweep. \n
			:param dwell: float Range: 0.001 to 100, Unit: s
		"""
		param = Conversions.decimal_value_to_str(dwell)
		self._core.io.write(f'SOURce<HwInstance>:LFOutput:SWEep:FREQuency:DWELl {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.AutoManStep:
		"""SCPI: [SOURce<HW>]:LFOutput:SWEep:[FREQuency]:MODE \n
		Snippet: value: enums.AutoManStep = driver.source.lfOutput.sweep.frequency.get_mode() \n
		Sets the cycle mode of the LF sweep. \n
			:return: mode: AUTO| MANual| STEP AUTO Performs a complete sweep cycle from the start to the end value when a trigger event occurs. The dwell time determines the time period until the signal switches to the next step. MANual Performs a single sweep step when a manual trigger event occurs. The trigger system is not active. To trigger each frequency step of the sweep individually, use the command [:SOURcehw]:LFOutput:FREQuency:MANual. STEP Each trigger command triggers one sweep step only. The frequency increases by the value set with the coammnds: [:SOURcehw]:LFOutput:SWEep[:FREQuency]:STEP[:LINear] (linear spacing) [:SOURcehw]:LFOutput:SWEep[:FREQuency]:STEP:LOGarithmic(logarithmic spacing)
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LFOutput:SWEep:FREQuency:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManStep)

	def set_mode(self, mode: enums.AutoManStep) -> None:
		"""SCPI: [SOURce<HW>]:LFOutput:SWEep:[FREQuency]:MODE \n
		Snippet: driver.source.lfOutput.sweep.frequency.set_mode(mode = enums.AutoManStep.AUTO) \n
		Sets the cycle mode of the LF sweep. \n
			:param mode: AUTO| MANual| STEP AUTO Performs a complete sweep cycle from the start to the end value when a trigger event occurs. The dwell time determines the time period until the signal switches to the next step. MANual Performs a single sweep step when a manual trigger event occurs. The trigger system is not active. To trigger each frequency step of the sweep individually, use the command [:SOURcehw]:LFOutput:FREQuency:MANual. STEP Each trigger command triggers one sweep step only. The frequency increases by the value set with the coammnds: [:SOURcehw]:LFOutput:SWEep[:FREQuency]:STEP[:LINear] (linear spacing) [:SOURcehw]:LFOutput:SWEep[:FREQuency]:STEP:LOGarithmic(logarithmic spacing)
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AutoManStep)
		self._core.io.write(f'SOURce<HwInstance>:LFOutput:SWEep:FREQuency:MODE {param}')

	def get_points(self) -> int:
		"""SCPI: [SOURce<HW>]:LFOutput:SWEep:[FREQuency]:POINts \n
		Snippet: value: int = driver.source.lfOutput.sweep.frequency.get_points() \n
		Sets the number of steps in an LF sweep. For information on how the value is calculated and the interdependency with
		other parameters, see 'Correlating parameters in sweep mode' \n
			:return: points: integer Range: 2 to POINts
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LFOutput:SWEep:FREQuency:POINts?')
		return Conversions.str_to_int(response)

	def set_points(self, points: int) -> None:
		"""SCPI: [SOURce<HW>]:LFOutput:SWEep:[FREQuency]:POINts \n
		Snippet: driver.source.lfOutput.sweep.frequency.set_points(points = 1) \n
		Sets the number of steps in an LF sweep. For information on how the value is calculated and the interdependency with
		other parameters, see 'Correlating parameters in sweep mode' \n
			:param points: integer Range: 2 to POINts
		"""
		param = Conversions.decimal_value_to_str(points)
		self._core.io.write(f'SOURce<HwInstance>:LFOutput:SWEep:FREQuency:POINts {param}')

	def get_retrace(self) -> bool:
		"""SCPI: [SOURce<HW>]:LFOutput:SWEep:[FREQuency]:RETRace \n
		Snippet: value: bool = driver.source.lfOutput.sweep.frequency.get_retrace() \n
		Activates that the signal changes to the start frequency value while it is waiting for the next trigger event. You can
		enable this feature, when you are working with sawtooth shapes in sweep mode 'Single' or 'External Single'. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LFOutput:SWEep:FREQuency:RETRace?')
		return Conversions.str_to_bool(response)

	def set_retrace(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:LFOutput:SWEep:[FREQuency]:RETRace \n
		Snippet: driver.source.lfOutput.sweep.frequency.set_retrace(state = False) \n
		Activates that the signal changes to the start frequency value while it is waiting for the next trigger event. You can
		enable this feature, when you are working with sawtooth shapes in sweep mode 'Single' or 'External Single'. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:LFOutput:SWEep:FREQuency:RETRace {param}')

	def get_running(self) -> bool:
		"""SCPI: [SOURce<HW>]:LFOutput:SWEep:[FREQuency]:RUNNing \n
		Snippet: value: bool = driver.source.lfOutput.sweep.frequency.get_running() \n
		Queries the current status of the LF frequency sweep mode. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LFOutput:SWEep:FREQuency:RUNNing?')
		return Conversions.str_to_bool(response)

	# noinspection PyTypeChecker
	def get_shape(self) -> enums.SweCyclMode:
		"""SCPI: [SOURce<HW>]:LFOutput:SWEep:[FREQuency]:SHAPe \n
		Snippet: value: enums.SweCyclMode = driver.source.lfOutput.sweep.frequency.get_shape() \n
		Sets the cycle mode for a sweep sequence (shape) . \n
			:return: shape: SAWTooth| TRIangle
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LFOutput:SWEep:FREQuency:SHAPe?')
		return Conversions.str_to_scalar_enum(response, enums.SweCyclMode)

	def set_shape(self, shape: enums.SweCyclMode) -> None:
		"""SCPI: [SOURce<HW>]:LFOutput:SWEep:[FREQuency]:SHAPe \n
		Snippet: driver.source.lfOutput.sweep.frequency.set_shape(shape = enums.SweCyclMode.SAWTooth) \n
		Sets the cycle mode for a sweep sequence (shape) . \n
			:param shape: SAWTooth| TRIangle
		"""
		param = Conversions.enum_scalar_to_str(shape, enums.SweCyclMode)
		self._core.io.write(f'SOURce<HwInstance>:LFOutput:SWEep:FREQuency:SHAPe {param}')

	# noinspection PyTypeChecker
	def get_spacing(self) -> enums.Spacing:
		"""SCPI: [SOURce<HW>]:LFOutput:SWEep:[FREQuency]:SPACing \n
		Snippet: value: enums.Spacing = driver.source.lfOutput.sweep.frequency.get_spacing() \n
		Selects linear or logarithmic sweep spacing. \n
			:return: spacing: LINear| LOGarithmic
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LFOutput:SWEep:FREQuency:SPACing?')
		return Conversions.str_to_scalar_enum(response, enums.Spacing)

	def set_spacing(self, spacing: enums.Spacing) -> None:
		"""SCPI: [SOURce<HW>]:LFOutput:SWEep:[FREQuency]:SPACing \n
		Snippet: driver.source.lfOutput.sweep.frequency.set_spacing(spacing = enums.Spacing.LINear) \n
		Selects linear or logarithmic sweep spacing. \n
			:param spacing: LINear| LOGarithmic
		"""
		param = Conversions.enum_scalar_to_str(spacing, enums.Spacing)
		self._core.io.write(f'SOURce<HwInstance>:LFOutput:SWEep:FREQuency:SPACing {param}')

	def clone(self) -> 'Frequency':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frequency(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
