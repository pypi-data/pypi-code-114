from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rate:
	"""Rate commands group definition. 6 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rate", core, parent)

	@property
	def max(self):
		"""max commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_max'):
			from .Max import Max
			self._max = Max(self._core, self._cmd_group)
		return self._max

	def get_a(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:USEFul:[RATE]:A \n
		Snippet: value: int = driver.source.bb.isdbt.useful.rate.get_a() \n
		Displays the data rate measured in the specific layer. \n
			:return: meas_use_drate_a: integer Range: 0 to 9999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:USEFul:RATE:A?')
		return Conversions.str_to_int(response)

	def get_b(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:USEFul:[RATE]:B \n
		Snippet: value: int = driver.source.bb.isdbt.useful.rate.get_b() \n
		Displays the data rate measured in the specific layer. \n
			:return: meas_use_drate_b: integer Range: 0 to 9999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:USEFul:RATE:B?')
		return Conversions.str_to_int(response)

	def get_c(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:USEFul:[RATE]:C \n
		Snippet: value: int = driver.source.bb.isdbt.useful.rate.get_c() \n
		Displays the data rate measured in the specific layer. \n
			:return: meas_use_drata_c: integer Range: 0 to 9999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:USEFul:RATE:C?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Rate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
