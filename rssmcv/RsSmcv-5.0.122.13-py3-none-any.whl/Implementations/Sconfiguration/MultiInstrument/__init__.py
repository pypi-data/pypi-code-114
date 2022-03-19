from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiInstrument:
	"""MultiInstrument commands group definition. 5 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("multiInstrument", core, parent)

	@property
	def connector(self):
		"""connector commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_connector'):
			from .Connector import Connector
			self._connector = Connector(self._core, self._cmd_group)
		return self._connector

	@property
	def trigger(self):
		"""trigger commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.MultInstMsMode:
		"""SCPI: SCONfiguration:MULTiinstrument:MODE \n
		Snippet: value: enums.MultInstMsMode = driver.sconfiguration.multiInstrument.get_mode() \n
		No command help available \n
			:return: ms_mode: No help available
		"""
		response = self._core.io.query_str('SCONfiguration:MULTiinstrument:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.MultInstMsMode)

	def set_mode(self, ms_mode: enums.MultInstMsMode) -> None:
		"""SCPI: SCONfiguration:MULTiinstrument:MODE \n
		Snippet: driver.sconfiguration.multiInstrument.set_mode(ms_mode = enums.MultInstMsMode.PRIMary) \n
		No command help available \n
			:param ms_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(ms_mode, enums.MultInstMsMode)
		self._core.io.write(f'SCONfiguration:MULTiinstrument:MODE {param}')

	def get_state(self) -> bool:
		"""SCPI: SCONfiguration:MULTiinstrument:STATe \n
		Snippet: value: bool = driver.sconfiguration.multiInstrument.get_state() \n
		No command help available \n
			:return: trigger_state: No help available
		"""
		response = self._core.io.query_str('SCONfiguration:MULTiinstrument:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, trigger_state: bool) -> None:
		"""SCPI: SCONfiguration:MULTiinstrument:STATe \n
		Snippet: driver.sconfiguration.multiInstrument.set_state(trigger_state = False) \n
		No command help available \n
			:param trigger_state: No help available
		"""
		param = Conversions.bool_to_str(trigger_state)
		self._core.io.write(f'SCONfiguration:MULTiinstrument:STATe {param}')

	def clone(self) -> 'MultiInstrument':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultiInstrument(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
