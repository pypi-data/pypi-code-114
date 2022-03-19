from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ImportPy:
	"""ImportPy commands group definition. 8 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("importPy", core, parent)

	@property
	def add(self):
		"""add commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_add'):
			from .Add import Add
			self._add = Add(self._core, self._cmd_group)
		return self._add

	@property
	def execute(self):
		"""execute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_execute'):
			from .Execute import Execute
			self._execute = Execute(self._core, self._cmd_group)
		return self._execute

	@property
	def remove(self):
		"""remove commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_remove'):
			from .Remove import Remove
			self._remove = Remove(self._core, self._cmd_group)
		return self._remove

	def get_list_py(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ATMospheric:IONospheric:MOPS:IMPort:LIST \n
		Snippet: value: List[str] = driver.source.bb.gnss.atmospheric.ionospheric.mops.importPy.get_list_py() \n
		Queries all files of the import file list in a comma separated list. \n
			:return: gnss_dcw_in_files: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:ATMospheric:IONospheric:MOPS:IMPort:LIST?')
		return Conversions.str_to_str_list(response)

	def clone(self) -> 'ImportPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ImportPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
