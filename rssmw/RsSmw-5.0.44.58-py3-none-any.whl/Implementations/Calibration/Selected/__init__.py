from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Selected:
	"""Selected commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("selected", core, parent)

	@property
	def step(self):
		"""step commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_step'):
			from .Step import Step
			self._step = Step(self._core, self._cmd_group)
		return self._step

	def get_catalog(self) -> List[str]:
		"""SCPI: CALibration<HW>:SELected:CATalog \n
		Snippet: value: List[str] = driver.calibration.selected.get_catalog() \n
		No command help available \n
			:return: catalog: No help available
		"""
		response = self._core.io.query_str('CALibration<HwInstance>:SELected:CATalog?')
		return Conversions.str_to_str_list(response)

	def get_measure(self) -> bool:
		"""SCPI: CALibration<HW>:SELected:[MEASure] \n
		Snippet: value: bool = driver.calibration.selected.get_measure() \n
		No command help available \n
			:return: meas: No help available
		"""
		response = self._core.io.query_str('CALibration<HwInstance>:SELected:MEASure?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Selected':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Selected(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
