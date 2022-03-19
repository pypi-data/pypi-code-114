from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Connection:
	"""Connection commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("connection", core, parent)

	@property
	def remote(self):
		"""remote commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_remote'):
			from .Remote import Remote
			self._remote = Remote(self._core, self._cmd_group)
		return self._remote

	@property
	def usb(self):
		"""usb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_usb'):
			from .Usb import Usb
			self._usb = Usb(self._core, self._cmd_group)
		return self._usb

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:FREQuency:CONVerter:EXTernal:CONNection:STATe \n
		Snippet: value: bool = driver.source.frequency.converter.external.connection.get_state() \n
		No command help available \n
			:return: conn_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:CONVerter:EXTernal:CONNection:STATe?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Connection':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Connection(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
