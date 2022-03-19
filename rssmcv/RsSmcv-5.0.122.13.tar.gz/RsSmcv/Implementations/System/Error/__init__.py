from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Error:
	"""Error commands group definition. 7 total commands, 2 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("error", core, parent)

	@property
	def code(self):
		"""code commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_code'):
			from .Code import Code
			self._code = Code(self._core, self._cmd_group)
		return self._code

	@property
	def history(self):
		"""history commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_history'):
			from .History import History
			self._history = History(self._core, self._cmd_group)
		return self._history

	def get_all(self) -> str:
		"""SCPI: SYSTem:ERRor:ALL \n
		Snippet: value: str = driver.system.error.get_all() \n
		Queries the error/event queue for all unread items and removes them from the queue. \n
			:return: all: string Error/event_number,'Error/event_description[;Device-dependent info]' A comma separated list of error number and a short description of the error in FIFO order. If the queue is empty, the response is 0,'No error' Positive error numbers are instrument-dependent. Negative error numbers are reserved by the SCPI standard. Volatile errors are reported once, at the time they appear. Identical errors are reported repeatedly only if the original error has already been retrieved from (and hence not any more present in) the error queue.
		"""
		response = self._core.io.query_str('SYSTem:ERRor:ALL?')
		return trim_str_response(response)

	def get_count(self) -> str:
		"""SCPI: SYSTem:ERRor:COUNt \n
		Snippet: value: str = driver.system.error.get_count() \n
		Queries the number of entries in the error queue. \n
			:return: count: integer 0 The error queue is empty.
		"""
		response = self._core.io.query_str('SYSTem:ERRor:COUNt?')
		return trim_str_response(response)

	def get_static(self) -> str:
		"""SCPI: SYSTem:ERRor:STATic \n
		Snippet: value: str = driver.system.error.get_static() \n
		Returns a list of all errors existing at the time when the query is started. This list corresponds to the display on the
		info page under manual control. \n
			:return: static_errors: string
		"""
		response = self._core.io.query_str('SYSTem:ERRor:STATic?')
		return trim_str_response(response)

	def clone(self) -> 'Error':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Error(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
