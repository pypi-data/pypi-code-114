from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 8 total commands, 3 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("carrier", core, parent)

	@property
	def execute(self):
		"""execute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_execute'):
			from .Execute import Execute
			self._execute = Execute(self._core, self._cmd_group)
		return self._execute

	@property
	def phase(self):
		"""phase commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_phase'):
			from .Phase import Phase
			self._phase = Phase(self._core, self._cmd_group)
		return self._phase

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	def get_start(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:MCCW:EDIT:CARRier:STARt \n
		Snippet: value: int = driver.source.bb.mccw.edit.carrier.get_start() \n
		No command help available \n
			:return: start: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:MCCW:EDIT:CARRier:STARt?')
		return Conversions.str_to_int(response)

	def set_start(self, start: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:MCCW:EDIT:CARRier:STARt \n
		Snippet: driver.source.bb.mccw.edit.carrier.set_start(start = 1) \n
		No command help available \n
			:param start: No help available
		"""
		param = Conversions.decimal_value_to_str(start)
		self._core.io.write(f'SOURce<HwInstance>:BB:MCCW:EDIT:CARRier:STARt {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:MCCW:EDIT:CARRier:STATe \n
		Snippet: value: bool = driver.source.bb.mccw.edit.carrier.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:MCCW:EDIT:CARRier:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:MCCW:EDIT:CARRier:STATe \n
		Snippet: driver.source.bb.mccw.edit.carrier.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:MCCW:EDIT:CARRier:STATe {param}')

	def get_stop(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:MCCW:EDIT:CARRier:STOP \n
		Snippet: value: int = driver.source.bb.mccw.edit.carrier.get_stop() \n
		No command help available \n
			:return: stop: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:MCCW:EDIT:CARRier:STOP?')
		return Conversions.str_to_int(response)

	def set_stop(self, stop: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:MCCW:EDIT:CARRier:STOP \n
		Snippet: driver.source.bb.mccw.edit.carrier.set_stop(stop = 1) \n
		No command help available \n
			:param stop: No help available
		"""
		param = Conversions.decimal_value_to_str(stop)
		self._core.io.write(f'SOURce<HwInstance>:BB:MCCW:EDIT:CARRier:STOP {param}')

	def clone(self) -> 'Carrier':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Carrier(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
