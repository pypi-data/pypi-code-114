from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Restart:
	"""Restart commands group definition. 7 total commands, 3 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("restart", core, parent)

	@property
	def arm(self):
		"""arm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_arm'):
			from .Arm import Arm
			self._arm = Arm(self._core, self._cmd_group)
		return self._arm

	@property
	def execute(self):
		"""execute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_execute'):
			from .Execute import Execute
			self._execute = Execute(self._core, self._cmd_group)
		return self._execute

	@property
	def synchronize(self):
		"""synchronize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_synchronize'):
			from .Synchronize import Synchronize
			self._synchronize = Synchronize(self._core, self._cmd_group)
		return self._synchronize

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.RegTrigMode:
		"""SCPI: [SOURce<HW>]:REGenerator:RESTart:MODE \n
		Snippet: value: enums.RegTrigMode = driver.source.regenerator.restart.get_mode() \n
		Selects the event which leads to a restart of the REG simulation. \n
			:return: mode: AUTO| AAUTo AUTO The signal generation starts after the REG is enabled. The signal is generated continuously; all configured objects are simulated. AAUT Simulation starts upon trigger event ([:SOURcehw]:REGenerator:RESTart:EXECute) . Then the signal is generated continuously; all configured objects are simulated.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:RESTart:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.RegTrigMode)

	def set_mode(self, mode: enums.RegTrigMode) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:RESTart:MODE \n
		Snippet: driver.source.regenerator.restart.set_mode(mode = enums.RegTrigMode.AAUTo) \n
		Selects the event which leads to a restart of the REG simulation. \n
			:param mode: AUTO| AAUTo AUTO The signal generation starts after the REG is enabled. The signal is generated continuously; all configured objects are simulated. AAUT Simulation starts upon trigger event ([:SOURcehw]:REGenerator:RESTart:EXECute) . Then the signal is generated continuously; all configured objects are simulated.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.RegTrigMode)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:RESTart:MODE {param}')

	# noinspection PyTypeChecker
	def get_rmode(self) -> enums.TrigRunMode:
		"""SCPI: [SOURce<HW>]:REGenerator:RESTart:RMODe \n
		Snippet: value: enums.TrigRunMode = driver.source.regenerator.restart.get_rmode() \n
		Queries the status of signal generation for all trigger modes. \n
			:return: rmode: STOP| RUN
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:RESTart:RMODe?')
		return Conversions.str_to_scalar_enum(response, enums.TrigRunMode)

	# noinspection PyTypeChecker
	def get_source(self) -> enums.TrigSourReg:
		"""SCPI: [SOURce<HW>]:REGenerator:RESTart:SOURce \n
		Snippet: value: enums.TrigSourReg = driver.source.regenerator.restart.get_source() \n
		Selects the trigger signal source and determines the way the triggering is executed. \n
			:return: source: INTernal| ERRTA| ERRTB INTernal Internal triggering by the command [:SOURcehw]:REGenerator:RESTart:EXECute. ERRTA|ERRTB External trigger signal via one of the external global trigger connectors. See [:SOURce]:INPut:USERch:SIGNal.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:RESTart:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.TrigSourReg)

	def set_source(self, source: enums.TrigSourReg) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:RESTart:SOURce \n
		Snippet: driver.source.regenerator.restart.set_source(source = enums.TrigSourReg.ERRTA) \n
		Selects the trigger signal source and determines the way the triggering is executed. \n
			:param source: INTernal| ERRTA| ERRTB INTernal Internal triggering by the command [:SOURcehw]:REGenerator:RESTart:EXECute. ERRTA|ERRTB External trigger signal via one of the external global trigger connectors. See [:SOURce]:INPut:USERch:SIGNal.
		"""
		param = Conversions.enum_scalar_to_str(source, enums.TrigSourReg)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:RESTart:SOURce {param}')

	def get_st_attenuation(self) -> float:
		"""SCPI: [SOURce<HW>]:REGenerator:RESTart:STATtenuation \n
		Snippet: value: float = driver.source.regenerator.restart.get_st_attenuation() \n
		If [:SOURce<hw>]:REGenerator:RESTart:MODEAAUT, sets the attenuation applied on the output signal during the time the
		signal generation is stopped. \n
			:return: stop_time_att: float Range: 0 to 60
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:RESTart:STATtenuation?')
		return Conversions.str_to_float(response)

	def set_st_attenuation(self, stop_time_att: float) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:RESTart:STATtenuation \n
		Snippet: driver.source.regenerator.restart.set_st_attenuation(stop_time_att = 1.0) \n
		If [:SOURce<hw>]:REGenerator:RESTart:MODEAAUT, sets the attenuation applied on the output signal during the time the
		signal generation is stopped. \n
			:param stop_time_att: float Range: 0 to 60
		"""
		param = Conversions.decimal_value_to_str(stop_time_att)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:RESTart:STATtenuation {param}')

	def clone(self) -> 'Restart':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Restart(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
