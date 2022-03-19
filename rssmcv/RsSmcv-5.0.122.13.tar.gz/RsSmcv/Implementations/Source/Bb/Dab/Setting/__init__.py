from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Setting:
	"""Setting commands group definition. 5 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("setting", core, parent)

	@property
	def store(self):
		"""store commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_store'):
			from .Store import Store
			self._store = Store(self._core, self._cmd_group)
		return self._store

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:DAB:SETTing:CATalog \n
		Snippet: value: List[str] = driver.source.bb.dab.setting.get_catalog() \n
		No command help available \n
			:return: catalog: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DAB:SETTing:CATalog?')
		return Conversions.str_to_str_list(response)

	def delete(self, file: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:DAB:SETTing:DELete \n
		Snippet: driver.source.bb.dab.setting.delete(file = '1') \n
		No command help available \n
			:param file: No help available
		"""
		param = Conversions.value_to_quoted_str(file)
		self._core.io.write(f'SOURce<HwInstance>:BB:DAB:SETTing:DELete {param}')

	def load(self, load: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:DAB:SETTing:LOAD \n
		Snippet: driver.source.bb.dab.setting.load(load = '1') \n
		No command help available \n
			:param load: No help available
		"""
		param = Conversions.value_to_quoted_str(load)
		self._core.io.write(f'SOURce<HwInstance>:BB:DAB:SETTing:LOAD {param}')

	def clone(self) -> 'Setting':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Setting(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
