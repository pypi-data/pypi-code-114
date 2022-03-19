from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Calibrated:
	"""Calibrated commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("calibrated", core, parent)

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	def get_frequency(self) -> float:
		"""SCPI: SOURce<HW>:RFALignment:CALibrated:FREQuency \n
		Snippet: value: float = driver.source.rfAlignment.calibrated.get_frequency() \n
		Queries the frequency for that the calibration data is valid. \n
			:return: calibrated_freq: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:RFALignment:CALibrated:FREQuency?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Calibrated':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Calibrated(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
