from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mccw:
	"""Mccw commands group definition. 43 total commands, 5 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mccw", core, parent)

	@property
	def carrier(self):
		"""carrier commands group. 4 Sub-classes, 2 commands."""
		if not hasattr(self, '_carrier'):
			from .Carrier import Carrier
			self._carrier = Carrier(self._core, self._cmd_group)
		return self._carrier

	@property
	def cfactor(self):
		"""cfactor commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_cfactor'):
			from .Cfactor import Cfactor
			self._cfactor = Cfactor(self._core, self._cmd_group)
		return self._cfactor

	@property
	def clock(self):
		"""clock commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_clock'):
			from .Clock import Clock
			self._clock = Clock(self._core, self._cmd_group)
		return self._clock

	@property
	def edit(self):
		"""edit commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_edit'):
			from .Edit import Edit
			self._edit = Edit(self._core, self._cmd_group)
		return self._edit

	@property
	def trigger(self):
		"""trigger commands group. 5 Sub-classes, 4 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:MCCW:PRESet \n
		Snippet: driver.source.bb.mccw.preset() \n
		Sets all multi carrier signal parameters to their default values. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:MCCW:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:MCCW:PRESet \n
		Snippet: driver.source.bb.mccw.preset_with_opc() \n
		Sets all multi carrier signal parameters to their default values. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:MCCW:PRESet', opc_timeout_ms)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:MCCW:STATe \n
		Snippet: value: bool = driver.source.bb.mccw.get_state() \n
		Enables/disables the multi carrier CW signal. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:MCCW:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:MCCW:STATe \n
		Snippet: driver.source.bb.mccw.set_state(state = False) \n
		Enables/disables the multi carrier CW signal. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:MCCW:STATe {param}')

	def clone(self) -> 'Mccw':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mccw(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
