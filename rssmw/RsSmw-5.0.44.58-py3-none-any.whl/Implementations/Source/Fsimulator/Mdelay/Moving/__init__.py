from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Moving:
	"""Moving commands group definition. 5 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("moving", core, parent)

	@property
	def delay(self):
		"""delay commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_delay'):
			from .Delay import Delay
			self._delay = Delay(self._core, self._cmd_group)
		return self._delay

	def get_loss(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:MOVing:LOSS \n
		Snippet: value: float = driver.source.fsimulator.mdelay.moving.get_loss() \n
		Sets the insertion loss of the moving path for moving propagation. \n
			:return: loss: float Range: 0 to 50
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MDELay:MOVing:LOSS?')
		return Conversions.str_to_float(response)

	def set_loss(self, loss: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:MOVing:LOSS \n
		Snippet: driver.source.fsimulator.mdelay.moving.set_loss(loss = 1.0) \n
		Sets the insertion loss of the moving path for moving propagation. \n
			:param loss: float Range: 0 to 50
		"""
		param = Conversions.decimal_value_to_str(loss)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MDELay:MOVing:LOSS {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:MOVing:STATe \n
		Snippet: value: bool = driver.source.fsimulator.mdelay.moving.get_state() \n
		This command activates the moving fading path for moving propagation. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MDELay:MOVing:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:MOVing:STATe \n
		Snippet: driver.source.fsimulator.mdelay.moving.set_state(state = False) \n
		This command activates the moving fading path for moving propagation. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MDELay:MOVing:STATe {param}')

	def get_vperiod(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:MOVing:VPERiod \n
		Snippet: value: float = driver.source.fsimulator.mdelay.moving.get_vperiod() \n
		This command sets the speed of the delay variation of the moving fading path for moving propagation. A complete cycle
		comprises one pass through this 'Variation Period'. \n
			:return: vperiod: float Range: 10 to 500
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MDELay:MOVing:VPERiod?')
		return Conversions.str_to_float(response)

	def set_vperiod(self, vperiod: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:MOVing:VPERiod \n
		Snippet: driver.source.fsimulator.mdelay.moving.set_vperiod(vperiod = 1.0) \n
		This command sets the speed of the delay variation of the moving fading path for moving propagation. A complete cycle
		comprises one pass through this 'Variation Period'. \n
			:param vperiod: float Range: 10 to 500
		"""
		param = Conversions.decimal_value_to_str(vperiod)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MDELay:MOVing:VPERiod {param}')

	def clone(self) -> 'Moving':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Moving(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
