from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


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
		"""SCPI: CALibration<HW>:FREQuency:CONVerter:EXTernal:SELected:CATalog \n
		Snippet: value: List[str] = driver.calibration.frequency.converter.external.selected.get_catalog() \n
		No command help available \n
			:return: freq_conv_cal_sel_step_cat: No help available
		"""
		response = self._core.io.query_str('CALibration<HwInstance>:FREQuency:CONVerter:EXTernal:SELected:CATalog?')
		return Conversions.str_to_str_list(response)

	def get_value(self) -> bool:
		"""SCPI: CALibration<HW>:FREQuency:CONVerter:EXTernal:SELected \n
		Snippet: value: bool = driver.calibration.frequency.converter.external.selected.get_value() \n
		No command help available \n
			:return: success: No help available
		"""
		response = self._core.io.query_str('CALibration<HwInstance>:FREQuency:CONVerter:EXTernal:SELected?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Selected':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Selected(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
