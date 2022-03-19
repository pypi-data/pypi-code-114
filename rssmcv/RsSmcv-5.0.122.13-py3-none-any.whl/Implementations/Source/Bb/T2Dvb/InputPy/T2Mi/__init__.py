from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class T2Mi:
	"""T2Mi commands group definition. 13 total commands, 3 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("t2Mi", core, parent)

	@property
	def max(self):
		"""max commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_max'):
			from .Max import Max
			self._max = Max(self._core, self._cmd_group)
		return self._max

	@property
	def min(self):
		"""min commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_min'):
			from .Min import Min
			self._min = Min(self._core, self._cmd_group)
		return self._min

	@property
	def resetLog(self):
		"""resetLog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_resetLog'):
			from .ResetLog import ResetLog
			self._resetLog = ResetLog(self._core, self._cmd_group)
		return self._resetLog

	def get_analyzer(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut:T2MI:ANALyzer \n
		Snippet: value: str = driver.source.bb.t2Dvb.inputPy.t2Mi.get_analyzer() \n
		Queries the status of the T2-MI analyzer by an error message. \n
			:return: analyzer: string No error Implies correct behavior of the analyzer.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INPut:T2MI:ANALyzer?')
		return trim_str_response(response)

	def get_interface(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut:T2MI:INTerface \n
		Snippet: value: bool = driver.source.bb.t2Dvb.inputPy.t2Mi.get_interface() \n
		Activates the T2-MI modulator interface. \n
			:return: interface: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INPut:T2MI:INTerface?')
		return Conversions.str_to_bool(response)

	def set_interface(self, interface: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut:T2MI:INTerface \n
		Snippet: driver.source.bb.t2Dvb.inputPy.t2Mi.set_interface(interface = False) \n
		Activates the T2-MI modulator interface. \n
			:param interface: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(interface)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:INPut:T2MI:INTerface {param}')

	# noinspection PyTypeChecker
	def get_measure_mode(self) -> enums.Dvbt2InputSignalMeasurementMode:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut:T2MI:MEASuremode \n
		Snippet: value: enums.Dvbt2InputSignalMeasurementMode = driver.source.bb.t2Dvb.inputPy.t2Mi.get_measure_mode() \n
		Specifies the measurement mode to configure the evaluation of T2-MI timing parameters. \n
			:return: measure_mode: ABSOLUTE| DELTA
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INPut:T2MI:MEASuremode?')
		return Conversions.str_to_scalar_enum(response, enums.Dvbt2InputSignalMeasurementMode)

	def set_measure_mode(self, measure_mode: enums.Dvbt2InputSignalMeasurementMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut:T2MI:MEASuremode \n
		Snippet: driver.source.bb.t2Dvb.inputPy.t2Mi.set_measure_mode(measure_mode = enums.Dvbt2InputSignalMeasurementMode.ABSOLUTE) \n
		Specifies the measurement mode to configure the evaluation of T2-MI timing parameters. \n
			:param measure_mode: ABSOLUTE| DELTA
		"""
		param = Conversions.enum_scalar_to_str(measure_mode, enums.Dvbt2InputSignalMeasurementMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:INPut:T2MI:MEASuremode {param}')

	def get_pid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut:T2MI:PID \n
		Snippet: value: int = driver.source.bb.t2Dvb.inputPy.t2Mi.get_pid() \n
		Sets the . The PID belongs to MPEG transport stream packets, that contain T2-MI data. \n
			:return: pid: integer Range: #H0 to #H1FFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INPut:T2MI:PID?')
		return Conversions.str_to_int(response)

	def set_pid(self, pid: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut:T2MI:PID \n
		Snippet: driver.source.bb.t2Dvb.inputPy.t2Mi.set_pid(pid = 1) \n
		Sets the . The PID belongs to MPEG transport stream packets, that contain T2-MI data. \n
			:param pid: integer Range: #H0 to #H1FFF
		"""
		param = Conversions.decimal_value_to_str(pid)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:INPut:T2MI:PID {param}')

	def get_sid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut:T2MI:SID \n
		Snippet: value: int = driver.source.bb.t2Dvb.inputPy.t2Mi.get_sid() \n
		Sets the T2-MI transport . Use the SID, when transmitting a composite signal, in accordance with annex I of the
		specification . \n
			:return: sid: integer Range: #H0 to #H7
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:INPut:T2MI:SID?')
		return Conversions.str_to_int(response)

	def set_sid(self, sid: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:INPut:T2MI:SID \n
		Snippet: driver.source.bb.t2Dvb.inputPy.t2Mi.set_sid(sid = 1) \n
		Sets the T2-MI transport . Use the SID, when transmitting a composite signal, in accordance with annex I of the
		specification . \n
			:param sid: integer Range: #H0 to #H7
		"""
		param = Conversions.decimal_value_to_str(sid)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:INPut:T2MI:SID {param}')

	def clone(self) -> 'T2Mi':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = T2Mi(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
