from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Combined:
	"""Combined commands group definition. 6 total commands, 1 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("combined", core, parent)

	@property
	def execute(self):
		"""execute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_execute'):
			from .Execute import Execute
			self._execute = Execute(self._core, self._cmd_group)
		return self._execute

	def get_count(self) -> int:
		"""SCPI: [SOURce<HW>]:SWEep:COMBined:COUNt \n
		Snippet: value: int = driver.source.sweep.combined.get_count() \n
		Defines the number of sweeps you want to execute. This parameter applies to [:SOURce<hw>]:SWEep:COMBined:MODE > SINGle.
		To start the sweep signal generation, use the command [:SOURce<hw>]:SWEep:COMBined:EXECute. \n
			:return: step_count: integer Range: 1 to SeMAX_INT_STEP-1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:COMBined:COUNt?')
		return Conversions.str_to_int(response)

	def set_count(self, step_count: int) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:COMBined:COUNt \n
		Snippet: driver.source.sweep.combined.set_count(step_count = 1) \n
		Defines the number of sweeps you want to execute. This parameter applies to [:SOURce<hw>]:SWEep:COMBined:MODE > SINGle.
		To start the sweep signal generation, use the command [:SOURce<hw>]:SWEep:COMBined:EXECute. \n
			:param step_count: integer Range: 1 to SeMAX_INT_STEP-1
		"""
		param = Conversions.decimal_value_to_str(step_count)
		self._core.io.write(f'SOURce<HwInstance>:SWEep:COMBined:COUNt {param}')

	def get_dwell(self) -> float:
		"""SCPI: [SOURce<HW>]:SWEep:COMBined:DWELl \n
		Snippet: value: float = driver.source.sweep.combined.get_dwell() \n
		Sets the dwell time for the combined frequency / level sweep. \n
			:return: dwell: float Range: 0.01 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:COMBined:DWELl?')
		return Conversions.str_to_float(response)

	def set_dwell(self, dwell: float) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:COMBined:DWELl \n
		Snippet: driver.source.sweep.combined.set_dwell(dwell = 1.0) \n
		Sets the dwell time for the combined frequency / level sweep. \n
			:param dwell: float Range: 0.01 to 100
		"""
		param = Conversions.decimal_value_to_str(dwell)
		self._core.io.write(f'SOURce<HwInstance>:SWEep:COMBined:DWELl {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.AutoManStep:
		"""SCPI: [SOURce<HW>]:SWEep:COMBined:MODE \n
		Snippet: value: enums.AutoManStep = driver.source.sweep.combined.get_mode() \n
		Sets the cycle mode for the combined frequency / level sweep. \n
			:return: sweep_comb_mode: AUTO| MANual| STEP AUTO Each trigger event triggers exactly one complete sweep. MANual The trigger system is not active. You can trigger every step individually by input of the frequencies with the commands [:SOURcehw]:FREQuency:MANual and [:SOURcehw]:POWer:MANual. STEP Each trigger event triggers one sweep step.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:COMBined:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManStep)

	def set_mode(self, sweep_comb_mode: enums.AutoManStep) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:COMBined:MODE \n
		Snippet: driver.source.sweep.combined.set_mode(sweep_comb_mode = enums.AutoManStep.AUTO) \n
		Sets the cycle mode for the combined frequency / level sweep. \n
			:param sweep_comb_mode: AUTO| MANual| STEP AUTO Each trigger event triggers exactly one complete sweep. MANual The trigger system is not active. You can trigger every step individually by input of the frequencies with the commands [:SOURcehw]:FREQuency:MANual and [:SOURcehw]:POWer:MANual. STEP Each trigger event triggers one sweep step.
		"""
		param = Conversions.enum_scalar_to_str(sweep_comb_mode, enums.AutoManStep)
		self._core.io.write(f'SOURce<HwInstance>:SWEep:COMBined:MODE {param}')

	def get_retrace(self) -> bool:
		"""SCPI: [SOURce<HW>]:SWEep:COMBined:RETRace \n
		Snippet: value: bool = driver.source.sweep.combined.get_retrace() \n
		Activates that the signal changes to the start level value while it is waiting for the next trigger event. You can enable
		this feature, when you are working with sawtooth shapes in sweep mode 'Single' or 'External Single'. \n
			:return: retrace_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:COMBined:RETRace?')
		return Conversions.str_to_bool(response)

	def set_retrace(self, retrace_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:COMBined:RETRace \n
		Snippet: driver.source.sweep.combined.set_retrace(retrace_state = False) \n
		Activates that the signal changes to the start level value while it is waiting for the next trigger event. You can enable
		this feature, when you are working with sawtooth shapes in sweep mode 'Single' or 'External Single'. \n
			:param retrace_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(retrace_state)
		self._core.io.write(f'SOURce<HwInstance>:SWEep:COMBined:RETRace {param}')

	# noinspection PyTypeChecker
	def get_shape(self) -> enums.SweCyclMode:
		"""SCPI: [SOURce<HW>]:SWEep:COMBined:SHAPe \n
		Snippet: value: enums.SweCyclMode = driver.source.sweep.combined.get_shape() \n
		Selects the waveform shape for the combined frequency / level sweep sequence. \n
			:return: shape: SAWTooth| TRIangle
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:COMBined:SHAPe?')
		return Conversions.str_to_scalar_enum(response, enums.SweCyclMode)

	def set_shape(self, shape: enums.SweCyclMode) -> None:
		"""SCPI: [SOURce<HW>]:SWEep:COMBined:SHAPe \n
		Snippet: driver.source.sweep.combined.set_shape(shape = enums.SweCyclMode.SAWTooth) \n
		Selects the waveform shape for the combined frequency / level sweep sequence. \n
			:param shape: SAWTooth| TRIangle
		"""
		param = Conversions.enum_scalar_to_str(shape, enums.SweCyclMode)
		self._core.io.write(f'SOURce<HwInstance>:SWEep:COMBined:SHAPe {param}')

	def clone(self) -> 'Combined':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Combined(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
