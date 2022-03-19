from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 16 total commands, 3 Subgroups, 13 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def add(self):
		"""add commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_add'):
			from .Add import Add
			self._add = Add(self._core, self._cmd_group)
		return self._add

	@property
	def change(self):
		"""change commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_change'):
			from .Change import Change
			self._change = Change(self._core, self._cmd_group)
		return self._change

	@property
	def execute(self):
		"""execute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_execute'):
			from .Execute import Execute
			self._execute = Execute(self._core, self._cmd_group)
		return self._execute

	def abort(self) -> None:
		"""SCPI: [SOURce]:BB:MEASurement:POWer:ABORt \n
		Snippet: driver.source.bb.measurement.power.abort() \n
		Stops the current measurement. \n
		"""
		self._core.io.write(f'SOURce:BB:MEASurement:POWer:ABORt')

	def abort_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce]:BB:MEASurement:POWer:ABORt \n
		Snippet: driver.source.bb.measurement.power.abort_with_opc() \n
		Stops the current measurement. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce:BB:MEASurement:POWer:ABORt', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_acquisition(self) -> enums.BbMeasPowAcq:
		"""SCPI: [SOURce]:BB:MEASurement:POWer:ACQuisition \n
		Snippet: value: enums.BbMeasPowAcq = driver.source.bb.measurement.power.get_acquisition() \n
		Sets the acquisition method. \n
			:return: acquistion: NOMinal| CONTinuous| GATed| MGATed
		"""
		response = self._core.io.query_str('SOURce:BB:MEASurement:POWer:ACQuisition?')
		return Conversions.str_to_scalar_enum(response, enums.BbMeasPowAcq)

	def set_acquisition(self, acquistion: enums.BbMeasPowAcq) -> None:
		"""SCPI: [SOURce]:BB:MEASurement:POWer:ACQuisition \n
		Snippet: driver.source.bb.measurement.power.set_acquisition(acquistion = enums.BbMeasPowAcq.CONTinuous) \n
		Sets the acquisition method. \n
			:param acquistion: NOMinal| CONTinuous| GATed| MGATed
		"""
		param = Conversions.enum_scalar_to_str(acquistion, enums.BbMeasPowAcq)
		self._core.io.write(f'SOURce:BB:MEASurement:POWer:ACQuisition {param}')

	def delete(self) -> None:
		"""SCPI: [SOURce]:BB:MEASurement:POWer:DELete \n
		Snippet: driver.source.bb.measurement.power.delete() \n
		Removes the selected measurement from the list. \n
		"""
		self._core.io.write(f'SOURce:BB:MEASurement:POWer:DELete')

	def delete_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce]:BB:MEASurement:POWer:DELete \n
		Snippet: driver.source.bb.measurement.power.delete_with_opc() \n
		Removes the selected measurement from the list. \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce:BB:MEASurement:POWer:DELete', opc_timeout_ms)

	def get_duration(self) -> float:
		"""SCPI: [SOURce]:BB:MEASurement:POWer:DURation \n
		Snippet: value: float = driver.source.bb.measurement.power.get_duration() \n
		Sets the measurement's time of a single measurement. \n
			:return: duration: float Range: 1E-3 to 5400
		"""
		response = self._core.io.query_str('SOURce:BB:MEASurement:POWer:DURation?')
		return Conversions.str_to_float(response)

	def set_duration(self, duration: float) -> None:
		"""SCPI: [SOURce]:BB:MEASurement:POWer:DURation \n
		Snippet: driver.source.bb.measurement.power.set_duration(duration = 1.0) \n
		Sets the measurement's time of a single measurement. \n
			:param duration: float Range: 1E-3 to 5400
		"""
		param = Conversions.decimal_value_to_str(duration)
		self._core.io.write(f'SOURce:BB:MEASurement:POWer:DURation {param}')

	# noinspection PyTypeChecker
	def get_gsource(self) -> enums.BbMeasPowGateSour:
		"""SCPI: [SOURce]:BB:MEASurement:POWer:GSOurce \n
		Snippet: value: enums.BbMeasPowGateSour = driver.source.bb.measurement.power.get_gsource() \n
		Determines the marker signal defining the signal part to be evaluated. The available values depend on the selected
		acquisition ([:SOURce]:BB:MEASurement:POWer:ACQuisition) . \n
			:return: gate_source: NONE| MARK1| MARK2| MARK3| MGATed NONE Default value for nominal and continuous acquisition. MARK1|MARK2|MARK3 Marker signal as defined in the baseband MGATed Reserved for multi gated acquisition
		"""
		response = self._core.io.query_str('SOURce:BB:MEASurement:POWer:GSOurce?')
		return Conversions.str_to_scalar_enum(response, enums.BbMeasPowGateSour)

	def set_gsource(self, gate_source: enums.BbMeasPowGateSour) -> None:
		"""SCPI: [SOURce]:BB:MEASurement:POWer:GSOurce \n
		Snippet: driver.source.bb.measurement.power.set_gsource(gate_source = enums.BbMeasPowGateSour.MARK1) \n
		Determines the marker signal defining the signal part to be evaluated. The available values depend on the selected
		acquisition ([:SOURce]:BB:MEASurement:POWer:ACQuisition) . \n
			:param gate_source: NONE| MARK1| MARK2| MARK3| MGATed NONE Default value for nominal and continuous acquisition. MARK1|MARK2|MARK3 Marker signal as defined in the baseband MGATed Reserved for multi gated acquisition
		"""
		param = Conversions.enum_scalar_to_str(gate_source, enums.BbMeasPowGateSour)
		self._core.io.write(f'SOURce:BB:MEASurement:POWer:GSOurce {param}')

	def get_index(self) -> int:
		"""SCPI: [SOURce]:BB:MEASurement:POWer:INDex \n
		Snippet: value: int = driver.source.bb.measurement.power.get_index() \n
		Selects the measurement index the subsequent settings apply to, for example changing, starting or removing form the list
		of measurements. \n
			:return: meas_index: integer Range: 1 to dynamic
		"""
		response = self._core.io.query_str('SOURce:BB:MEASurement:POWer:INDex?')
		return Conversions.str_to_int(response)

	def set_index(self, meas_index: int) -> None:
		"""SCPI: [SOURce]:BB:MEASurement:POWer:INDex \n
		Snippet: driver.source.bb.measurement.power.set_index(meas_index = 1) \n
		Selects the measurement index the subsequent settings apply to, for example changing, starting or removing form the list
		of measurements. \n
			:param meas_index: integer Range: 1 to dynamic
		"""
		param = Conversions.decimal_value_to_str(meas_index)
		self._core.io.write(f'SOURce:BB:MEASurement:POWer:INDex {param}')

	# noinspection PyTypeChecker
	def get_output(self) -> enums.BbMeasPowOutp:
		"""SCPI: [SOURce]:BB:MEASurement:POWer:OUTPut \n
		Snippet: value: enums.BbMeasPowOutp = driver.source.bb.measurement.power.get_output() \n
		Defines the output point the measurement are performed at. \n
			:return: output: RFA| RFB| IQOUT1| IQOUT2| BBMM1| BBMM2
		"""
		response = self._core.io.query_str('SOURce:BB:MEASurement:POWer:OUTPut?')
		return Conversions.str_to_scalar_enum(response, enums.BbMeasPowOutp)

	def set_output(self, output: enums.BbMeasPowOutp) -> None:
		"""SCPI: [SOURce]:BB:MEASurement:POWer:OUTPut \n
		Snippet: driver.source.bb.measurement.power.set_output(output = enums.BbMeasPowOutp.BBMM1) \n
		Defines the output point the measurement are performed at. \n
			:param output: RFA| RFB| IQOUT1| IQOUT2| BBMM1| BBMM2
		"""
		param = Conversions.enum_scalar_to_str(output, enums.BbMeasPowOutp)
		self._core.io.write(f'SOURce:BB:MEASurement:POWer:OUTPut {param}')

	def get_peak(self) -> List[float]:
		"""SCPI: [SOURce]:BB:MEASurement:POWer:PEAK \n
		Snippet: value: List[float] = driver.source.bb.measurement.power.get_peak() \n
		Queries the peak power of the baseband signal at the measurement point determined with the command
		[:SOURce]:BB:MEASurement:POWer:OUTPut. \n
			:return: peak_power: Peak_SubMes#1,Peak_SubMes#2,... Returns the peak power of the measured signal or if a multi-gated acquisition is used, a string of measured values with one value per performed submeasurement Range: -145 to 30
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce:BB:MEASurement:POWer:PEAK?')
		return response

	def get_progress(self) -> float:
		"""SCPI: [SOURce]:BB:MEASurement:POWer:PROGress \n
		Snippet: value: float = driver.source.bb.measurement.power.get_progress() \n
		Queries the status of the initiated measurement. The query returns a value that indicates the task progress in percent. \n
			:return: progress: float Range: 0 to 100
		"""
		response = self._core.io.query_str('SOURce:BB:MEASurement:POWer:PROGress?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_rmode(self) -> enums.BlerTrigMode:
		"""SCPI: [SOURce]:BB:MEASurement:POWer:RMODe \n
		Snippet: value: enums.BlerTrigMode = driver.source.bb.measurement.power.get_rmode() \n
		Determines whether a single or a continuous measurement is executed. \n
			:return: run_mode: SINGle| AUTO
		"""
		response = self._core.io.query_str('SOURce:BB:MEASurement:POWer:RMODe?')
		return Conversions.str_to_scalar_enum(response, enums.BlerTrigMode)

	def set_rmode(self, run_mode: enums.BlerTrigMode) -> None:
		"""SCPI: [SOURce]:BB:MEASurement:POWer:RMODe \n
		Snippet: driver.source.bb.measurement.power.set_rmode(run_mode = enums.BlerTrigMode.AUTO) \n
		Determines whether a single or a continuous measurement is executed. \n
			:param run_mode: SINGle| AUTO
		"""
		param = Conversions.enum_scalar_to_str(run_mode, enums.BlerTrigMode)
		self._core.io.write(f'SOURce:BB:MEASurement:POWer:RMODe {param}')

	def get_rms(self) -> List[float]:
		"""SCPI: [SOURce]:BB:MEASurement:POWer:RMS \n
		Snippet: value: List[float] = driver.source.bb.measurement.power.get_rms() \n
		Queries the RMS power of the baseband signal at the measurement point determined with the command
		[:SOURce]:BB:MEASurement:POWer:OUTPut. \n
			:return: rms_power: Power_SubMes#1,Level_SubMes#2,... Returns the power of the measured signal or if a multi-gated acquisition is used, a string of measured values with one value per performed submeasurement Range: -145 to 30
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce:BB:MEASurement:POWer:RMS?')
		return response

	def get_rstate(self) -> bool:
		"""SCPI: [SOURce]:BB:MEASurement:POWer:RSTate \n
		Snippet: value: bool = driver.source.bb.measurement.power.get_rstate() \n
		Queries the state (running/stopped) of the current measurement. \n
			:return: run_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce:BB:MEASurement:POWer:RSTate?')
		return Conversions.str_to_bool(response)

	# noinspection PyTypeChecker
	def get_source(self) -> enums.BbMeasPowSour:
		"""SCPI: [SOURce]:BB:MEASurement:POWer:SOURce \n
		Snippet: value: enums.BbMeasPowSour = driver.source.bb.measurement.power.get_source() \n
		Defines the measurement signal source. \n
			:return: source: BBA| BBB| BBC| BBD| BBINA| BBINB| FADINPA| FADINPB| FADINPC| FADINPD| FADOUTA| FADOUTB| FADOUTC| FADOUTD| AWGNA| AWGNB| AWGNC| AWGND| STREAMA| STREAMB| STREAMC| STREAMD
		"""
		response = self._core.io.query_str('SOURce:BB:MEASurement:POWer:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.BbMeasPowSour)

	def set_source(self, source: enums.BbMeasPowSour) -> None:
		"""SCPI: [SOURce]:BB:MEASurement:POWer:SOURce \n
		Snippet: driver.source.bb.measurement.power.set_source(source = enums.BbMeasPowSour.AWGNA) \n
		Defines the measurement signal source. \n
			:param source: BBA| BBB| BBC| BBD| BBINA| BBINB| FADINPA| FADINPB| FADINPC| FADINPD| FADOUTA| FADOUTB| FADOUTC| FADOUTD| AWGNA| AWGNB| AWGNC| AWGND| STREAMA| STREAMB| STREAMC| STREAMD
		"""
		param = Conversions.enum_scalar_to_str(source, enums.BbMeasPowSour)
		self._core.io.write(f'SOURce:BB:MEASurement:POWer:SOURce {param}')

	def clone(self) -> 'Power':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Power(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
