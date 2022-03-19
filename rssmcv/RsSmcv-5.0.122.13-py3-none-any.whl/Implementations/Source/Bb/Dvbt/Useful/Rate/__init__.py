from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rate:
	"""Rate commands group definition. 4 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rate", core, parent)

	@property
	def max(self):
		"""max commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_max'):
			from .Max import Max
			self._max = Max(self._core, self._cmd_group)
		return self._max

	def get_low(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DVBT:USEFul:[RATE]:LOW \n
		Snippet: value: float = driver.source.bb.dvbt.useful.rate.get_low() \n
		Queries the data rate of useful data ruseful of the external transport stream. The data rate is measured at the input of
		the installed input interface. \n
			:return: use_drlp: float Range: 0 to 9999999999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:USEFul:RATE:LOW?')
		return Conversions.str_to_float(response)

	def get_high(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DVBT:USEFul:[RATE]:[HIGH] \n
		Snippet: value: float = driver.source.bb.dvbt.useful.rate.get_high() \n
		Queries the data rate of useful data ruseful of the external transport stream. The data rate is measured at the input of
		the installed input interface. \n
			:return: use_drhp: float Range: 0 to 9999999999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:USEFul:RATE:HIGH?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Rate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
