from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Request:
	"""Request commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("request", core, parent)

	@property
	def shared(self):
		"""shared commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_shared'):
			from .Shared import Shared
			self._shared = Shared(self._core, self._cmd_group)
		return self._shared

	def get_exclusive(self) -> int:
		"""SCPI: SYSTem:LOCK:REQuest:[EXCLusive] \n
		Snippet: value: int = driver.system.lock.request.get_exclusive() \n
		Queries whether a lock for exclusive access to the instrument via ethernet exists. If successful, the query returns a 1,
		otherwise 0. \n
			:return: success: integer
		"""
		response = self._core.io.query_str('SYSTem:LOCK:REQuest:EXCLusive?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Request':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Request(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
