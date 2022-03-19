from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 6 total commands, 2 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	@property
	def hddStreaming(self):
		"""hddStreaming commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_hddStreaming'):
			from .HddStreaming import HddStreaming
			self._hddStreaming = HddStreaming(self._core, self._cmd_group)
		return self._hddStreaming

	@property
	def pattern(self):
		"""pattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import Pattern
			self._pattern = Pattern(self._core, self._cmd_group)
		return self._pattern

	def get_dselect(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:SIRius:DATA:DSELect \n
		Snippet: value: str = driver.source.bb.sirius.data.get_dselect() \n
		No command help available \n
			:return: dselect: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:SIRius:DATA:DSELect?')
		return trim_str_response(response)

	def set_dselect(self, dselect: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:SIRius:DATA:DSELect \n
		Snippet: driver.source.bb.sirius.data.set_dselect(dselect = '1') \n
		No command help available \n
			:param dselect: No help available
		"""
		param = Conversions.value_to_quoted_str(dselect)
		self._core.io.write(f'SOURce<HwInstance>:BB:SIRius:DATA:DSELect {param}')

	def get_edate(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:SIRius:DATA:EDATe \n
		Snippet: value: str = driver.source.bb.sirius.data.get_edate() \n
		No command help available \n
			:return: edate: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:SIRius:DATA:EDATe?')
		return trim_str_response(response)

	# noinspection PyTypeChecker
	def get_value(self) -> enums.DataSourceA:
		"""SCPI: [SOURce<HW>]:BB:SIRius:DATA \n
		Snippet: value: enums.DataSourceA = driver.source.bb.sirius.data.get_value() \n
		No command help available \n
			:return: data: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:SIRius:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.DataSourceA)

	def set_value(self, data: enums.DataSourceA) -> None:
		"""SCPI: [SOURce<HW>]:BB:SIRius:DATA \n
		Snippet: driver.source.bb.sirius.data.set_value(data = enums.DataSourceA.DLISt) \n
		No command help available \n
			:param data: No help available
		"""
		param = Conversions.enum_scalar_to_str(data, enums.DataSourceA)
		self._core.io.write(f'SOURce<HwInstance>:BB:SIRius:DATA {param}')

	def clone(self) -> 'Data':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Data(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
