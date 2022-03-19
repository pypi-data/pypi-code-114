from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Carrier:
	"""Carrier commands group definition. 8 total commands, 4 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("carrier", core, parent)

	@property
	def listPy(self):
		"""listPy commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPy
			self._listPy = ListPy(self._core, self._cmd_group)
		return self._listPy

	@property
	def phase(self):
		"""phase commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phase'):
			from .Phase import Phase
			self._phase = Phase(self._core, self._cmd_group)
		return self._phase

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def get_count(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CARRier:COUNt \n
		Snippet: value: int = driver.source.bb.mccw.carrier.get_count() \n
		No command help available \n
			:return: count: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:MCCW:CARRier:COUNt?')
		return Conversions.str_to_int(response)

	def set_count(self, count: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CARRier:COUNt \n
		Snippet: driver.source.bb.mccw.carrier.set_count(count = 1) \n
		No command help available \n
			:param count: No help available
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'SOURce<HwInstance>:BB:MCCW:CARRier:COUNt {param}')

	def get_spacing(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CARRier:SPACing \n
		Snippet: value: float = driver.source.bb.mccw.carrier.get_spacing() \n
		No command help available \n
			:return: spacing: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:MCCW:CARRier:SPACing?')
		return Conversions.str_to_float(response)

	def set_spacing(self, spacing: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CARRier:SPACing \n
		Snippet: driver.source.bb.mccw.carrier.set_spacing(spacing = 1.0) \n
		No command help available \n
			:param spacing: No help available
		"""
		param = Conversions.decimal_value_to_str(spacing)
		self._core.io.write(f'SOURce<HwInstance>:BB:MCCW:CARRier:SPACing {param}')

	def clone(self) -> 'Carrier':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Carrier(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
