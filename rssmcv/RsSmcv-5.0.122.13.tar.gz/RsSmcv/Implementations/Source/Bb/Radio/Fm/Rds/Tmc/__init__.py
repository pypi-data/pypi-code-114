from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tmc:
	"""Tmc commands group definition. 8 total commands, 3 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tmc", core, parent)

	@property
	def apply(self):
		"""apply commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apply'):
			from .Apply import Apply
			self._apply = Apply(self._core, self._cmd_group)
		return self._apply

	@property
	def g3A(self):
		"""g3A commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_g3A'):
			from .G3A import G3A
			self._g3A = G3A(self._core, self._cmd_group)
		return self._g3A

	@property
	def g8A(self):
		"""g8A commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_g8A'):
			from .G8A import G8A
			self._g8A = G8A(self._core, self._cmd_group)
		return self._g8A

	def get_ready(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:TMC:READy \n
		Snippet: value: bool = driver.source.bb.radio.fm.rds.tmc.get_ready() \n
		No command help available \n
			:return: tmc_ready: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:TMC:READy?')
		return Conversions.str_to_bool(response)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:TMC:[STATe] \n
		Snippet: value: bool = driver.source.bb.radio.fm.rds.tmc.get_state() \n
		Enables the traffic message channel. \n
			:return: tmc_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:TMC:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, tmc_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:TMC:[STATe] \n
		Snippet: driver.source.bb.radio.fm.rds.tmc.set_state(tmc_state = False) \n
		Enables the traffic message channel. \n
			:param tmc_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(tmc_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:TMC:STATe {param}')

	def clone(self) -> 'Tmc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tmc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
