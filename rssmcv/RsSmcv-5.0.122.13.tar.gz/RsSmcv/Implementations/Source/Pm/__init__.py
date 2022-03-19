from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pm:
	"""Pm commands group definition. 5 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pm", core, parent)

	@property
	def external(self):
		"""external commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_external'):
			from .External import External
			self._external = External(self._core, self._cmd_group)
		return self._external

	@property
	def internal(self):
		"""internal commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_internal'):
			from .Internal import Internal
			self._internal = Internal(self._core, self._cmd_group)
		return self._internal

	def get_sensitivity(self) -> float:
		"""SCPI: [SOURce<HW>]:PM:SENSitivity \n
		Snippet: value: float = driver.source.pm.get_sensitivity() \n
		No command help available \n
			:return: sensitivity: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PM:SENSitivity?')
		return Conversions.str_to_float(response)

	def get_deviation(self) -> float:
		"""SCPI: [SOURce<HW>]:PM:[DEViation] \n
		Snippet: value: float = driver.source.pm.get_deviation() \n
		No command help available \n
			:return: deviation: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PM:DEViation?')
		return Conversions.str_to_float(response)

	def set_deviation(self, deviation: float) -> None:
		"""SCPI: [SOURce<HW>]:PM:[DEViation] \n
		Snippet: driver.source.pm.set_deviation(deviation = 1.0) \n
		No command help available \n
			:param deviation: No help available
		"""
		param = Conversions.decimal_value_to_str(deviation)
		self._core.io.write(f'SOURce<HwInstance>:PM:DEViation {param}')

	def clone(self) -> 'Pm':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
