from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


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
		"""SCPI: [SOURce<HW>]:SWEep:[FREQuency]:DWELl \n
		Snippet: value: float = driver.source.sweep.frequency.get_dwell() \n
		Sets the dwell time for a frequency sweep step. \n
			:return: dwell: float Range: 1E-3 to 100, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:FREQuency:DWELl?')
		return Conversions.str_to_float(response)

	def set_dwell(self, dwell: float) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:[FREQuency]:DWELl \n
		Snippet: driver.source.sweep.frequency.set_dwell(dwell = 1.0) \n
		Sets the dwell time for a frequency sweep step. \n
			:param dwell: float Range: 1E-3 to 100, Unit: s
		"""
		param = Conversions.decimal_value_to_str(dwell)
		self._core.io.write(f'SOURce<HwInstance>:SWEep:FREQuency:DWELl {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.AutoManStep:
		"""SCPI: [SOURce<HW>]:SWEep:[FREQuency]:MODE \n
		Snippet: value: enums.AutoManStep = driver.source.sweep.frequency.get_mode() \n
		Sets the cycle mode for the frequency sweep. \n
			:return: mode: AUTO| MANual| STEP AUTO Each trigger event triggers exactly one complete sweep. MANual The trigger system is not active. You can trigger every step individually by input of the frequencies with the command [:SOURcehw]:FREQuency:MANual. STEP Each trigger event triggers one sweep step. The frequency increases by the value entered with [:SOURcehw]:SWEep[:FREQuency]:STEP[:LINear] (linear spacing) or [:SOURcehw]:SWEep[:FREQuency]:STEP:LOGarithmic (logarithmic spacing) .
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:FREQuency:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManStep)

	def set_mode(self, mode: enums.AutoManStep) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:[FREQuency]:MODE \n
		Snippet: driver.source.sweep.frequency.set_mode(mode = enums.AutoManStep.AUTO) \n
		Sets the cycle mode for the frequency sweep. \n
			:param mode: AUTO| MANual| STEP AUTO Each trigger event triggers exactly one complete sweep. MANual The trigger system is not active. You can trigger every step individually by input of the frequencies with the command [:SOURcehw]:FREQuency:MANual. STEP Each trigger event triggers one sweep step. The frequency increases by the value entered with [:SOURcehw]:SWEep[:FREQuency]:STEP[:LINear] (linear spacing) or [:SOURcehw]:SWEep[:FREQuency]:STEP:LOGarithmic (logarithmic spacing) .
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AutoManStep)
		self._core.io.write(f'SOURce<HwInstance>:SWEep:FREQuency:MODE {param}')

	def get_points(self) -> int:
		"""SCPI: [SOURce<HW>]:SWEep:[FREQuency]:POINts \n
		Snippet: value: int = driver.source.sweep.frequency.get_points() \n
		Sets the number of steps within the RF frequency sweep range. See 'Correlating parameters in sweep mode'. Two separate
		POINts values are used for linear or logarithmic sweep spacing (LIN | LOG) . The command always affects the currently set
		sweep spacing. \n
			:return: points: integer Range: 2 to Max
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:FREQuency:POINts?')
		return Conversions.str_to_int(response)

	def set_points(self, points: int) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:[FREQuency]:POINts \n
		Snippet: driver.source.sweep.frequency.set_points(points = 1) \n
		Sets the number of steps within the RF frequency sweep range. See 'Correlating parameters in sweep mode'. Two separate
		POINts values are used for linear or logarithmic sweep spacing (LIN | LOG) . The command always affects the currently set
		sweep spacing. \n
			:param points: integer Range: 2 to Max
		"""
		param = Conversions.decimal_value_to_str(points)
		self._core.io.write(f'SOURce<HwInstance>:SWEep:FREQuency:POINts {param}')

	def get_retrace(self) -> bool:
		"""SCPI: [SOURce<HW>]:SWEep:[FREQuency]:RETRace \n
		Snippet: value: bool = driver.source.sweep.frequency.get_retrace() \n
		Activates that the signal changes to the start frequency value while it is waiting for the next trigger event. You can
		enable this feature, when you are working with sawtooth shapes in sweep mode 'Single' or 'External Single'. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:FREQuency:RETRace?')
		return Conversions.str_to_bool(response)

	def set_retrace(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:[FREQuency]:RETRace \n
		Snippet: driver.source.sweep.frequency.set_retrace(state = False) \n
		Activates that the signal changes to the start frequency value while it is waiting for the next trigger event. You can
		enable this feature, when you are working with sawtooth shapes in sweep mode 'Single' or 'External Single'. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:SWEep:FREQuency:RETRace {param}')

	def get_running(self) -> bool:
		"""SCPI: [SOURce<HW>]:SWEep:[FREQuency]:RUNNing \n
		Snippet: value: bool = driver.source.sweep.frequency.get_running() \n
		Queries the current sweep state. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:FREQuency:RUNNing?')
		return Conversions.str_to_bool(response)

	# noinspection PyTypeChecker
	def get_shape(self) -> enums.SweCyclMode:
		"""SCPI: [SOURce<HW>]:SWEep:[FREQuency]:SHAPe \n
		Snippet: value: enums.SweCyclMode = driver.source.sweep.frequency.get_shape() \n
		Determines the waveform shape for a frequency sweep sequence. \n
			:return: shape: SAWTooth| TRIangle
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:FREQuency:SHAPe?')
		return Conversions.str_to_scalar_enum(response, enums.SweCyclMode)

	def set_shape(self, shape: enums.SweCyclMode) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:[FREQuency]:SHAPe \n
		Snippet: driver.source.sweep.frequency.set_shape(shape = enums.SweCyclMode.SAWTooth) \n
		Determines the waveform shape for a frequency sweep sequence. \n
			:param shape: SAWTooth| TRIangle
		"""
		param = Conversions.enum_scalar_to_str(shape, enums.SweCyclMode)
		self._core.io.write(f'SOURce<HwInstance>:SWEep:FREQuency:SHAPe {param}')

	# noinspection PyTypeChecker
	def get_spacing(self) -> enums.Spacing:
		"""SCPI: [SOURce<HW>]:SWEep:[FREQuency]:SPACing \n
		Snippet: value: enums.Spacing = driver.source.sweep.frequency.get_spacing() \n
		Selects the mode for the calculation of the frequency intervals, with which the current frequency at each step is
		increased or decreased. The keyword [:FREQuency] can be omitted; then the command is SCPI-compliant. \n
			:return: spacing: LINear| LOGarithmic LINear Sets a fixed frequency value as step width and adds it to the current frequency. The linear step width is entered in Hz, see [:SOURcehw]:SWEep[:FREQuency]:STEP[:LINear]. LOGarithmic Sets a constant fraction of the current frequency as step width and adds it to the current frequency. The logarithmic step width is entered in %, see [:SOURcehw]:SWEep[:FREQuency]:STEP:LOGarithmic.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:FREQuency:SPACing?')
		return Conversions.str_to_scalar_enum(response, enums.Spacing)

	def set_spacing(self, spacing: enums.Spacing) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:[FREQuency]:SPACing \n
		Snippet: driver.source.sweep.frequency.set_spacing(spacing = enums.Spacing.LINear) \n
		Selects the mode for the calculation of the frequency intervals, with which the current frequency at each step is
		increased or decreased. The keyword [:FREQuency] can be omitted; then the command is SCPI-compliant. \n
			:param spacing: LINear| LOGarithmic LINear Sets a fixed frequency value as step width and adds it to the current frequency. The linear step width is entered in Hz, see [:SOURcehw]:SWEep[:FREQuency]:STEP[:LINear]. LOGarithmic Sets a constant fraction of the current frequency as step width and adds it to the current frequency. The logarithmic step width is entered in %, see [:SOURcehw]:SWEep[:FREQuency]:STEP:LOGarithmic.
		"""
		param = Conversions.enum_scalar_to_str(spacing, enums.Spacing)
		self._core.io.write(f'SOURce<HwInstance>:SWEep:FREQuency:SPACing {param}')

	def clone(self) -> 'Frequency':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frequency(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
