from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Help:
	"""Help commands group definition. 4 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("help", core, parent)

	@property
	def syntax(self):
		"""syntax commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_syntax'):
			from .Syntax import Syntax
			self._syntax = Syntax(self._core, self._cmd_group)
		return self._syntax

	def export(self) -> None:
		"""SCPI: SYSTem:HELP:EXPort \n
		Snippet: driver.system.help.export() \n
		Saves the online help as zip archive in the user directory. \n
		"""
		self._core.io.write(f'SYSTem:HELP:EXPort')

	def export_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:HELP:EXPort \n
		Snippet: driver.system.help.export_with_opc() \n
		Saves the online help as zip archive in the user directory. \n
		Same as export, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:HELP:EXPort', opc_timeout_ms)

	def get_headers(self) -> str:
		"""SCPI: SYSTem:HELP:HEADers \n
		Snippet: value: str = driver.system.help.get_headers() \n
		No command help available \n
			:return: headers: No help available
		"""
		response = self._core.io.query_str('SYSTem:HELP:HEADers?')
		return trim_str_response(response)

	def clone(self) -> 'Help':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Help(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
