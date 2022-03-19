from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def sgamma(self):
		"""sgamma commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sgamma'):
			from .Sgamma import Sgamma
			self._sgamma = Sgamma(self._core, self._cmd_group)
		return self._sgamma

	def get_points(self) -> int:
		"""SCPI: [SOURce<HW>]:CORRection:CSET:DATA:POWer:POINts \n
		Snippet: value: int = driver.source.correction.cset.data.power.get_points() \n
		Queries the number of frequency/level values in the selected table. \n
			:return: points: integer Range: 0 to 10000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:CSET:DATA:POWer:POINts?')
		return Conversions.str_to_int(response)

	def get_value(self) -> List[float]:
		"""SCPI: [SOURce<HW>]:CORRection:CSET:DATA:POWer \n
		Snippet: value: List[float] = driver.source.correction.cset.data.power.get_value() \n
		Enters the level values to the table selected with [:SOURce<hw>]:CORRection:CSET[:SELect]. \n
			:return: power: Power#1[, Power#2, ...] String of values with default unit dB. *RST: 0
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce<HwInstance>:CORRection:CSET:DATA:POWer?')
		return response

	def set_value(self, power: List[float]) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:CSET:DATA:POWer \n
		Snippet: driver.source.correction.cset.data.power.set_value(power = [1.1, 2.2, 3.3]) \n
		Enters the level values to the table selected with [:SOURce<hw>]:CORRection:CSET[:SELect]. \n
			:param power: Power#1[, Power#2, ...] String of values with default unit dB. *RST: 0
		"""
		param = Conversions.list_to_csv_str(power)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:CSET:DATA:POWer {param}')

	def clone(self) -> 'Power':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Power(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
