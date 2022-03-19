from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Simulation:
	"""Simulation commands group definition. 18 total commands, 5 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("simulation", core, parent)

	@property
	def analyzer(self):
		"""analyzer commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_analyzer'):
			from .Analyzer import Analyzer
			self._analyzer = Analyzer(self._core, self._cmd_group)
		return self._analyzer

	@property
	def calibration(self):
		"""calibration commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_calibration'):
			from .Calibration import Calibration
			self._calibration = Calibration(self._core, self._cmd_group)
		return self._calibration

	@property
	def latency(self):
		"""latency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_latency'):
			from .Latency import Latency
			self._latency = Latency(self._core, self._cmd_group)
		return self._latency

	@property
	def level(self):
		"""level commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_level'):
			from .Level import Level
			self._level = Level(self._core, self._cmd_group)
		return self._level

	@property
	def minRange(self):
		"""minRange commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_minRange'):
			from .MinRange import MinRange
			self._minRange = MinRange(self._core, self._cmd_group)
		return self._minRange

	# noinspection PyTypeChecker
	def get_connector(self) -> enums.TmastConn:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:CONNector \n
		Snippet: value: enums.TmastConn = driver.source.regenerator.simulation.get_connector() \n
		Queries the instrument connector used to set the frequency [:SOURce<hw>]:REGenerator:SIMulation:FREQuency. \n
			:return: connector: RFA| RFB| BBMM1| BBMM2| IQOUT1| IQOUT2| FAD1| FAD2| FAD3| FAD4| DEF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:SIMulation:CONNector?')
		return Conversions.str_to_scalar_enum(response, enums.TmastConn)

	def get_frequency(self) -> float:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:FREQuency \n
		Snippet: value: float = driver.source.regenerator.simulation.get_frequency() \n
		Queries the RF frequency that is used for the calculation of the Doppler shift and the PRx. \n
			:return: frequency: float Range: 100E3 to 100E9
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:SIMulation:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, frequency: float) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:FREQuency \n
		Snippet: driver.source.regenerator.simulation.set_frequency(frequency = 1.0) \n
		Queries the RF frequency that is used for the calculation of the Doppler shift and the PRx. \n
			:param frequency: float Range: 100E3 to 100E9
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:SIMulation:FREQuency {param}')

	def get_prf(self) -> int:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:PRF \n
		Snippet: value: int = driver.source.regenerator.simulation.get_prf() \n
		Sets the pulse repetition frequency (PRF) . \n
			:return: prf: integer Range: 1 to 1E6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:SIMulation:PRF?')
		return Conversions.str_to_int(response)

	def set_prf(self, prf: int) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:PRF \n
		Snippet: driver.source.regenerator.simulation.set_prf(prf = 1) \n
		Sets the pulse repetition frequency (PRF) . \n
			:param prf: integer Range: 1 to 1E6
		"""
		param = Conversions.decimal_value_to_str(prf)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:SIMulation:PRF {param}')

	def get_pri(self) -> float:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:PRI \n
		Snippet: value: float = driver.source.regenerator.simulation.get_pri() \n
		Sets the pulse repetition frequency (PRI) . \n
			:return: sim_pri: float Range: 3.74742e-5 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:SIMulation:PRI?')
		return Conversions.str_to_float(response)

	def set_pri(self, sim_pri: float) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:PRI \n
		Snippet: driver.source.regenerator.simulation.set_pri(sim_pri = 1.0) \n
		Sets the pulse repetition frequency (PRI) . \n
			:param sim_pri: float Range: 3.74742e-5 to 1
		"""
		param = Conversions.decimal_value_to_str(sim_pri)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:SIMulation:PRI {param}')

	# noinspection PyTypeChecker
	def get_range(self) -> enums.RegSimRange:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:RANGe \n
		Snippet: value: enums.RegSimRange = driver.source.regenerator.simulation.get_range() \n
		No command help available \n
			:return: range_py: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:SIMulation:RANGe?')
		return Conversions.str_to_scalar_enum(response, enums.RegSimRange)

	def set_range(self, range_py: enums.RegSimRange) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:RANGe \n
		Snippet: driver.source.regenerator.simulation.set_range(range_py = enums.RegSimRange.L74K) \n
		No command help available \n
			:param range_py: No help available
		"""
		param = Conversions.enum_scalar_to_str(range_py, enums.RegSimRange)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:SIMulation:RANGe {param}')

	def get_speriod(self) -> float:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:SPERiod \n
		Snippet: value: float = driver.source.regenerator.simulation.get_speriod() \n
		Set the time which the radar needs for one scan. \n
			:return: sim_scan_period: float Range: 3.74742e-5 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:SIMulation:SPERiod?')
		return Conversions.str_to_float(response)

	def set_speriod(self, sim_scan_period: float) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:SPERiod \n
		Snippet: driver.source.regenerator.simulation.set_speriod(sim_scan_period = 1.0) \n
		Set the time which the radar needs for one scan. \n
			:param sim_scan_period: float Range: 3.74742e-5 to 10
		"""
		param = Conversions.decimal_value_to_str(sim_scan_period)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:SIMulation:SPERiod {param}')

	def clone(self) -> 'Simulation':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Simulation(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
