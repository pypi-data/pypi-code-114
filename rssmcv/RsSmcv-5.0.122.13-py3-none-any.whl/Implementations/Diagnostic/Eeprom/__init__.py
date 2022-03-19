from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eeprom:
	"""Eeprom commands group definition. 4 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eeprom", core, parent)

	@property
	def bidentifier(self):
		"""bidentifier commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bidentifier'):
			from .Bidentifier import Bidentifier
			self._bidentifier = Bidentifier(self._core, self._cmd_group)
		return self._bidentifier

	@property
	def customize(self):
		"""customize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_customize'):
			from .Customize import Customize
			self._customize = Customize(self._core, self._cmd_group)
		return self._customize

	@property
	def data(self):
		"""data commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	def delete(self) -> None:
		"""SCPI: DIAGnostic<HW>:EEPRom:DELete \n
		Snippet: driver.diagnostic.eeprom.delete() \n
		No command help available \n
		"""
		self._core.io.write(f'DIAGnostic<HwInstance>:EEPRom:DELete')

	def delete_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: DIAGnostic<HW>:EEPRom:DELete \n
		Snippet: driver.diagnostic.eeprom.delete_with_opc() \n
		No command help available \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsSmcv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'DIAGnostic<HwInstance>:EEPRom:DELete', opc_timeout_ms)

	def clone(self) -> 'Eeprom':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Eeprom(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
