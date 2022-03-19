from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Types import DataType
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bert:
	"""Bert commands group definition. 19 total commands, 2 Subgroups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bert", core, parent)

	@property
	def setup(self):
		"""setup commands group. 2 Sub-classes, 6 commands."""
		if not hasattr(self, '_setup'):
			from .Setup import Setup
			self._setup = Setup(self._core, self._cmd_group)
		return self._setup

	@property
	def trigger(self):
		"""trigger commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	def load(self, filename: str) -> None:
		"""SCPI: BERT:LOAD \n
		Snippet: driver.bert.load(filename = '1') \n
		Loads the selected file from the default or the specified directory. Loaded are files with extension *.ber_bler Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:param filename: string Filename or complete file path; file extension can be omitted
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'BERT:LOAD {param}')

	def preset(self) -> None:
		"""SCPI: BERT:PRESet \n
		Snippet: driver.bert.preset() \n
		Sets the parameters of the BERT/BLER test generator to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command .method RsSmw.Bert.state/method RsSmw.Bler.state. \n
		"""
		self._core.io.write(f'BERT:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: BERT:PRESet \n
		Snippet: driver.bert.preset_with_opc() \n
		Sets the parameters of the BERT/BLER test generator to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command .method RsSmw.Bert.state/method RsSmw.Bler.state. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'BERT:PRESet', opc_timeout_ms)

	# noinspection PyTypeChecker
	class ResultStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Num_Data_Bits: int: integer Number of checked data bits.
			- Num_Errors: int: integer Number of error bits.
			- Error_Rate: List[float]: float If no termination criterion has been reached since the beginning of the measurement, display the current quotient of NumErrors (number of error bits) and NumBlock (number of data bits) . When at least one final result has been reached in continuous measurement, display the most recent final result.
			- Meas_Finished: int: integer Status of measurement. 1 Measurement has been terminated, i.e. stopped or the defined number of data bits or error bits has been reached. 0 Measurement has not been terminated.
			- Clock_Detected: int: integer Status of clock line. 1 Clock line active. 0 Clock line not active.
			- Data_Detected: int: integer Status of data line. 1 Data line active. Only clocked data is detected. If the clock signal is missing, a data change is also not detected. 0 Data line is not active.
			- Synchronized: int: integer 1 The measurement is synchronized and the ratio is assumed realistic. That is, the clock and data lines are active and the following apples: NumErrors/NumBlock 0.1. 0 The measurement is not synchronized."""
		__meta_args_list = [
			ArgStruct.scalar_int('Num_Data_Bits'),
			ArgStruct.scalar_int('Num_Errors'),
			ArgStruct('Error_Rate', DataType.FloatList, None, False, True, 1),
			ArgStruct.scalar_int('Meas_Finished'),
			ArgStruct.scalar_int('Clock_Detected'),
			ArgStruct.scalar_int('Data_Detected'),
			ArgStruct.scalar_int('Synchronized')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Num_Data_Bits: int = None
			self.Num_Errors: int = None
			self.Error_Rate: List[float] = None
			self.Meas_Finished: int = None
			self.Clock_Detected: int = None
			self.Data_Detected: int = None
			self.Synchronized: int = None

	def get_result(self) -> ResultStruct:
		"""SCPI: BERT:RESult \n
		Snippet: value: ResultStruct = driver.bert.get_result() \n
		Queries the result of the last BLER measurement and responds with seven results, separated by commas.
		The first measurement following the start also queries intermediate results for the number of data bits, error bits and
		error rate. For method RsSmw.Bler.Trigger.modeAUTO, only the final results of each single measurement are queried in the
		following measurements. Note: The restart of a new measurement is delayed until the first measurement result has been
		queried. The resulting brief measurement interruption is irrelevant because the subsequent measurement is synchronized
		within 24 data bits. \n
			:return: structure: for return value, see the help for ResultStruct structure arguments.
		"""
		return self._core.io.query_struct('BERT:RESult?', self.__class__.ResultStruct())

	def start(self) -> None:
		"""SCPI: BERT:STARt \n
		Snippet: driver.bert.start() \n
		Starts a continuous measurement. \n
		"""
		self._core.io.write(f'BERT:STARt')

	def start_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: BERT:STARt \n
		Snippet: driver.bert.start_with_opc() \n
		Starts a continuous measurement. \n
		Same as start, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'BERT:STARt', opc_timeout_ms)

	def get_state(self) -> bool:
		"""SCPI: BERT:STATe \n
		Snippet: value: bool = driver.bert.get_state() \n
		Activates/deactivates the measurement. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('BERT:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: BERT:STATe \n
		Snippet: driver.bert.set_state(state = False) \n
		Activates/deactivates the measurement. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'BERT:STATe {param}')

	def stop(self) -> None:
		"""SCPI: BERT:STOP \n
		Snippet: driver.bert.stop() \n
		Stops an ongoing measurement. \n
		"""
		self._core.io.write(f'BERT:STOP')

	def stop_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: BERT:STOP \n
		Snippet: driver.bert.stop_with_opc() \n
		Stops an ongoing measurement. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'BERT:STOP', opc_timeout_ms)

	def set_store(self, filename: str) -> None:
		"""SCPI: BERT:STORe \n
		Snippet: driver.bert.set_store(filename = '1') \n
		Saves the current settings into the selected file; the file extension (*.ber_bler) is assigned automatically. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:param filename: 'filename' Filename or complete file path.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'BERT:STORe {param}')

	# noinspection PyTypeChecker
	def get_unit(self) -> enums.BertUnit:
		"""SCPI: BERT:UNIT \n
		Snippet: value: enums.BertUnit = driver.bert.get_unit() \n
		No command help available \n
			:return: unit: No help available
		"""
		response = self._core.io.query_str('BERT:UNIT?')
		return Conversions.str_to_scalar_enum(response, enums.BertUnit)

	def set_unit(self, unit: enums.BertUnit) -> None:
		"""SCPI: BERT:UNIT \n
		Snippet: driver.bert.set_unit(unit = enums.BertUnit.ENGineering) \n
		No command help available \n
			:param unit: No help available
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.BertUnit)
		self._core.io.write(f'BERT:UNIT {param}')

	def clone(self) -> 'Bert':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Bert(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
