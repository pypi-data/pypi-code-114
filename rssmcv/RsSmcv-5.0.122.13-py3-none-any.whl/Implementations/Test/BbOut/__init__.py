from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BbOut:
	"""BbOut commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bbOut", core, parent)

	@property
	def ttest(self):
		"""ttest commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ttest'):
			from .Ttest import Ttest
			self._ttest = Ttest(self._core, self._cmd_group)
		return self._ttest

	def get_lrate(self) -> float:
		"""SCPI: TEST<HW>:BBOut:LRATe \n
		Snippet: value: float = driver.test.bbOut.get_lrate() \n
		No command help available \n
			:return: lrate: No help available
		"""
		response = self._core.io.query_str('TEST<HwInstance>:BBOut:LRATe?')
		return Conversions.str_to_float(response)

	def set_lrate(self, lrate: float) -> None:
		"""SCPI: TEST<HW>:BBOut:LRATe \n
		Snippet: driver.test.bbOut.set_lrate(lrate = 1.0) \n
		No command help available \n
			:param lrate: No help available
		"""
		param = Conversions.decimal_value_to_str(lrate)
		self._core.io.write(f'TEST<HwInstance>:BBOut:LRATe {param}')

	def clone(self) -> 'BbOut':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BbOut(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
