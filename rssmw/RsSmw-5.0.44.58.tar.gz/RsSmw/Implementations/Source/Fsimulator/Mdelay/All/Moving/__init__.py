from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Moving:
	"""Moving commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("moving", core, parent)

	@property
	def delay(self):
		"""delay commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_delay'):
			from .Delay import Delay
			self._delay = Delay(self._core, self._cmd_group)
		return self._delay

	def get_vperiod(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:ALL:MOVing:VPERiod \n
		Snippet: value: float = driver.source.fsimulator.mdelay.all.moving.get_vperiod() \n
		Sets the speed of the delay variation of the moving fading paths for moving propagation with all moving channels.
		A complete cycle comprises one pass through this 'Variation Period'. \n
			:return: vperiod: float Range: 5 to 200
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MDELay:ALL:MOVing:VPERiod?')
		return Conversions.str_to_float(response)

	def set_vperiod(self, vperiod: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:ALL:MOVing:VPERiod \n
		Snippet: driver.source.fsimulator.mdelay.all.moving.set_vperiod(vperiod = 1.0) \n
		Sets the speed of the delay variation of the moving fading paths for moving propagation with all moving channels.
		A complete cycle comprises one pass through this 'Variation Period'. \n
			:param vperiod: float Range: 5 to 200
		"""
		param = Conversions.decimal_value_to_str(vperiod)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MDELay:ALL:MOVing:VPERiod {param}')

	def clone(self) -> 'Moving':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Moving(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
