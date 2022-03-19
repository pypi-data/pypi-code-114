from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pramp:
	"""Pramp commands group definition. 47 total commands, 5 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pramp", core, parent)

	@property
	def clock(self):
		"""clock commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_clock'):
			from .Clock import Clock
			self._clock = Clock(self._core, self._cmd_group)
		return self._clock

	@property
	def ramp(self):
		"""ramp commands group. 5 Sub-classes, 10 commands."""
		if not hasattr(self, '_ramp'):
			from .Ramp import Ramp
			self._ramp = Ramp(self._core, self._cmd_group)
		return self._ramp

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

	@property
	def trigger(self):
		"""trigger commands group. 5 Sub-classes, 5 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	@property
	def waveform(self):
		"""waveform commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_waveform'):
			from .Waveform import Waveform
			self._waveform = Waveform(self._core, self._cmd_group)
		return self._waveform

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:PRESet \n
		Snippet: driver.source.bb.pramp.preset() \n
		Sets the parameters of the power sweep to their default values (*RST values specified for the commands) . Not affected is
		the state set with the command [:SOURce<hw>]:BB:PRAMp:STATe. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:PRAMp:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:PRESet \n
		Snippet: driver.source.bb.pramp.preset_with_opc() \n
		Sets the parameters of the power sweep to their default values (*RST values specified for the commands) . Not affected is
		the state set with the command [:SOURce<hw>]:BB:PRAMp:STATe. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:PRAMp:PRESet', opc_timeout_ms)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:STATe \n
		Snippet: value: bool = driver.source.bb.pramp.get_state() \n
		Activates power sweep signal generation, and deactivates all digital standards, digital modulation modes and other sweeps
		in the corresponding path. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PRAMp:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:STATe \n
		Snippet: driver.source.bb.pramp.set_state(state = False) \n
		Activates power sweep signal generation, and deactivates all digital standards, digital modulation modes and other sweeps
		in the corresponding path. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:PRAMp:STATe {param}')

	def clone(self) -> 'Pramp':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pramp(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
