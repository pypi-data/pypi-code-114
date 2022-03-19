from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Point:
	"""Point commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("point", core, parent)

	@property
	def configuration(self):
		"""configuration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_configuration'):
			from .Configuration import Configuration
			self._configuration = Configuration(self._core, self._cmd_group)
		return self._configuration

	def get_catalog(self) -> List[str]:
		"""SCPI: DIAGnostic<HW>:POINt:CATalog \n
		Snippet: value: List[str] = driver.diagnostic.point.get_catalog() \n
		Queries the test points available in the instrument. For more information, see R&S SMCV100B Service Manual. \n
			:return: catalog: string List of comma-separated values, each representing a test point
		"""
		response = self._core.io.query_str('DIAGnostic<HwInstance>:POINt:CATalog?')
		return Conversions.str_to_str_list(response)

	def clone(self) -> 'Point':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Point(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
