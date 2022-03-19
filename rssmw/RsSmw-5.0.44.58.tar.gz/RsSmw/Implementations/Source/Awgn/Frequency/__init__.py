from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	@property
	def center(self):
		"""center commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_center'):
			from .Center import Center
			self._center = Center(self._core, self._cmd_group)
		return self._center

	def get_result(self) -> float:
		"""SCPI: [SOURce<HW>]:AWGN:FREQuency:RESult \n
		Snippet: value: float = driver.source.awgn.frequency.get_result() \n
		Queries the actual frequency of the sine wave. \n
			:return: result: float Range: -40E6 to 40E6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AWGN:FREQuency:RESult?')
		return Conversions.str_to_float(response)

	def get_target(self) -> float:
		"""SCPI: [SOURce<HW>]:AWGN:FREQuency:TARGet \n
		Snippet: value: float = driver.source.awgn.frequency.get_target() \n
		Sets the desired frequency of the sine wave. \n
			:return: target: float Range: -40E6 to 40E6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AWGN:FREQuency:TARGet?')
		return Conversions.str_to_float(response)

	def set_target(self, target: float) -> None:
		"""SCPI: [SOURce<HW>]:AWGN:FREQuency:TARGet \n
		Snippet: driver.source.awgn.frequency.set_target(target = 1.0) \n
		Sets the desired frequency of the sine wave. \n
			:param target: float Range: -40E6 to 40E6
		"""
		param = Conversions.decimal_value_to_str(target)
		self._core.io.write(f'SOURce<HwInstance>:AWGN:FREQuency:TARGet {param}')

	def clone(self) -> 'Frequency':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frequency(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
