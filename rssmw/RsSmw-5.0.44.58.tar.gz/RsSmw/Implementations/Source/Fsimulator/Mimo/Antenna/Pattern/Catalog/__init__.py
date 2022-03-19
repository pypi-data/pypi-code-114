from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	@property
	def user(self):
		"""user commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_user'):
			from .User import User
			self._user = User(self._core, self._cmd_group)
		return self._user

	def get_value(self) -> List[str]:
		"""SCPI: [SOURce]:FSIMulator:MIMO:ANTenna:PATTern:CATalog \n
		Snippet: value: List[str] = driver.source.fsimulator.mimo.antenna.pattern.catalog.get_value() \n
		Queries the available predefined antenna pattern files (*.ant_pat) . To query the user-defined antenna pattern files, use
		the command [:SOURce]:FSIMulator:MIMO:ANTenna:PATTern:CATalog:USER?. \n
			:return: catalog: string Files names without file extension.
		"""
		response = self._core.io.query_str('SOURce:FSIMulator:MIMO:ANTenna:PATTern:CATalog?')
		return Conversions.str_to_str_list(response)

	def clone(self) -> 'Catalog':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Catalog(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
