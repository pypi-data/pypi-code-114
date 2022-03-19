from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 32 total commands, 7 Subgroups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	@property
	def dexchange(self):
		"""dexchange commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_dexchange'):
			from .Dexchange import Dexchange
			self._dexchange = Dexchange(self._core, self._cmd_group)
		return self._dexchange

	@property
	def dwell(self):
		"""dwell commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_dwell'):
			from .Dwell import Dwell
			self._dwell = Dwell(self._core, self._cmd_group)
		return self._dwell

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def index(self):
		"""index commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_index'):
			from .Index import Index
			self._index = Index(self._core, self._cmd_group)
		return self._index

	@property
	def learn(self):
		"""learn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_learn'):
			from .Learn import Learn
			self._learn = Learn(self._core, self._cmd_group)
		return self._learn

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def trigger(self):
		"""trigger commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:LIST:CATalog \n
		Snippet: value: List[str] = driver.source.listPy.get_catalog() \n
		Queries the available list files in the specified directory. \n
			:return: catalog: string List of list filenames, separated by commas
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LIST:CATalog?')
		return Conversions.str_to_str_list(response)

	def delete(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:LIST:DELete \n
		Snippet: driver.source.listPy.delete(filename = '1') \n
		Deletes the specified list. Refer to 'Accessing files in the default or in a specified directory' for general information
		on file handling in the default and in a specific directory. \n
			:param filename: string Filename or complete file path; file extension is optional.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:LIST:DELete {param}')

	def delete_all(self) -> None:
		"""SCPI: [SOURce<HW>]:LIST:DELete:ALL \n
		Snippet: driver.source.listPy.delete_all() \n
		Deletes all lists in the set directory.
			INTRO_CMD_HELP: This command can only be executed, if: \n
			- No list file is selected.
			- List mode is disabled. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:LIST:DELete:ALL')

	def delete_all_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:LIST:DELete:ALL \n
		Snippet: driver.source.listPy.delete_all_with_opc() \n
		Deletes all lists in the set directory.
			INTRO_CMD_HELP: This command can only be executed, if: \n
			- No list file is selected.
			- List mode is disabled. \n
		Same as delete_all, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:LIST:DELete:ALL', opc_timeout_ms)

	def get_free(self) -> int:
		"""SCPI: [SOURce<HW>]:LIST:FREE \n
		Snippet: value: int = driver.source.listPy.get_free() \n
		Queries the amount of free memory (in bytes) for list mode lists. \n
			:return: free: integer Range: 0 to INT_MAX
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LIST:FREE?')
		return Conversions.str_to_int(response)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.AutoStep:
		"""SCPI: [SOURce<HW>]:LIST:MODE \n
		Snippet: value: enums.AutoStep = driver.source.listPy.get_mode() \n
		Sets the list mode. The instrument processes the list according to the selected mode and trigger source.
		See LIST:TRIG:SOUR AUTO, SING or EXT for the description of the trigger source settings. \n
			:return: mode: AUTO| STEP AUTO Each trigger event triggers a complete list cycle. STEP Each trigger event triggers only one step in the list processing cycle. The list is processed in ascending order.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LIST:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AutoStep)

	def set_mode(self, mode: enums.AutoStep) -> None:
		"""SCPI: [SOURce<HW>]:LIST:MODE \n
		Snippet: driver.source.listPy.set_mode(mode = enums.AutoStep.AUTO) \n
		Sets the list mode. The instrument processes the list according to the selected mode and trigger source.
		See LIST:TRIG:SOUR AUTO, SING or EXT for the description of the trigger source settings. \n
			:param mode: AUTO| STEP AUTO Each trigger event triggers a complete list cycle. STEP Each trigger event triggers only one step in the list processing cycle. The list is processed in ascending order.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AutoStep)
		self._core.io.write(f'SOURce<HwInstance>:LIST:MODE {param}')

	def reset(self) -> None:
		"""SCPI: [SOURce<HW>]:LIST:RESet \n
		Snippet: driver.source.listPy.reset() \n
		Jumps to the beginning of the list. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:LIST:RESet')

	def reset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:LIST:RESet \n
		Snippet: driver.source.listPy.reset_with_opc() \n
		Jumps to the beginning of the list. \n
		Same as reset, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:LIST:RESet', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_rmode(self) -> enums.LmodRunMode:
		"""SCPI: [SOURce<HW>]:LIST:RMODe \n
		Snippet: value: enums.LmodRunMode = driver.source.listPy.get_rmode() \n
		Selects the run mode for processing the list. \n
			:return: rmode: LEARned| LIVE LEARned Generates the signal by replaying the previously learned and saved data from the temporary memory. LIVE Generates the signal by processing the list directly.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LIST:RMODe?')
		return Conversions.str_to_scalar_enum(response, enums.LmodRunMode)

	def set_rmode(self, rmode: enums.LmodRunMode) -> None:
		"""SCPI: [SOURce<HW>]:LIST:RMODe \n
		Snippet: driver.source.listPy.set_rmode(rmode = enums.LmodRunMode.LEARned) \n
		Selects the run mode for processing the list. \n
			:param rmode: LEARned| LIVE LEARned Generates the signal by replaying the previously learned and saved data from the temporary memory. LIVE Generates the signal by processing the list directly.
		"""
		param = Conversions.enum_scalar_to_str(rmode, enums.LmodRunMode)
		self._core.io.write(f'SOURce<HwInstance>:LIST:RMODe {param}')

	def get_running(self) -> bool:
		"""SCPI: [SOURce<HW>]:LIST:RUNNing \n
		Snippet: value: bool = driver.source.listPy.get_running() \n
		Queries the current state of the list mode. \n
			:return: state: 1| ON| 0| OFF 1 Signal generation based on the list mode is active.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LIST:RUNNing?')
		return Conversions.str_to_bool(response)

	def get_select(self) -> str:
		"""SCPI: [SOURce<HW>]:LIST:SELect \n
		Snippet: value: str = driver.source.listPy.get_select() \n
		Selects or creates a data list in list mode. If the list with the selected name does not exist, a new list is created. \n
			:return: filename: string Filename or complete file path; file extension can be omitted.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LIST:SELect?')
		return trim_str_response(response)

	def set_select(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:LIST:SELect \n
		Snippet: driver.source.listPy.set_select(filename = '1') \n
		Selects or creates a data list in list mode. If the list with the selected name does not exist, a new list is created. \n
			:param filename: string Filename or complete file path; file extension can be omitted.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:LIST:SELect {param}')

	def clone(self) -> 'ListPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
