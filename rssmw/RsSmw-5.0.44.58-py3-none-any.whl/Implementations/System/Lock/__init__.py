from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lock:
	"""Lock commands group definition. 10 total commands, 5 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lock", core, parent)

	@property
	def name(self):
		"""name commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_name'):
			from .Name import Name
			self._name = Name(self._core, self._cmd_group)
		return self._name

	@property
	def owner(self):
		"""owner commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_owner'):
			from .Owner import Owner
			self._owner = Owner(self._core, self._cmd_group)
		return self._owner

	@property
	def release(self):
		"""release commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_release'):
			from .Release import Release
			self._release = Release(self._core, self._cmd_group)
		return self._release

	@property
	def request(self):
		"""request commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_request'):
			from .Request import Request
			self._request = Request(self._core, self._cmd_group)
		return self._request

	@property
	def shared(self):
		"""shared commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_shared'):
			from .Shared import Shared
			self._shared = Shared(self._core, self._cmd_group)
		return self._shared

	def get_timeout(self) -> int:
		"""SCPI: SYSTem:LOCK:TIMeout \n
		Snippet: value: int = driver.system.lock.get_timeout() \n
		No command help available \n
			:return: time_ms: No help available
		"""
		response = self._core.io.query_str('SYSTem:LOCK:TIMeout?')
		return Conversions.str_to_int(response)

	def set_timeout(self, time_ms: int) -> None:
		"""SCPI: SYSTem:LOCK:TIMeout \n
		Snippet: driver.system.lock.set_timeout(time_ms = 1) \n
		No command help available \n
			:param time_ms: No help available
		"""
		param = Conversions.decimal_value_to_str(time_ms)
		self._core.io.write(f'SYSTem:LOCK:TIMeout {param}')

	def clone(self) -> 'Lock':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Lock(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
