from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Delay:
	"""Delay commands group definition. 4 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("delay", core, parent)

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maximum'):
			from .Maximum import Maximum
			self._maximum = Maximum(self._core, self._cmd_group)
		return self._maximum

	@property
	def minimum(self):
		"""minimum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_minimum'):
			from .Minimum import Minimum
			self._minimum = Minimum(self._core, self._cmd_group)
		return self._minimum

	def set(self, delay: float, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DAB:TRIGger:OUTPut<CH>:DELay \n
		Snippet: driver.source.bb.dab.trigger.output.delay.set(delay = 1.0, output = repcap.Output.Default) \n
		No command help available \n
			:param delay: No help available
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(delay)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:DAB:TRIGger:OUTPut{output_cmd_val}:DELay {param}')

	def get(self, output=repcap.Output.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:DAB:TRIGger:OUTPut<CH>:DELay \n
		Snippet: value: float = driver.source.bb.dab.trigger.output.delay.get(output = repcap.Output.Default) \n
		No command help available \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: delay: No help available"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DAB:TRIGger:OUTPut{output_cmd_val}:DELay?')
		return Conversions.str_to_float(response)

	def get_fixed(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DAB:TRIGger:OUTPut:DELay:FIXed \n
		Snippet: value: bool = driver.source.bb.dab.trigger.output.delay.get_fixed() \n
		No command help available \n
			:return: fixed: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DAB:TRIGger:OUTPut:DELay:FIXed?')
		return Conversions.str_to_bool(response)

	def set_fixed(self, fixed: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DAB:TRIGger:OUTPut:DELay:FIXed \n
		Snippet: driver.source.bb.dab.trigger.output.delay.set_fixed(fixed = False) \n
		No command help available \n
			:param fixed: No help available
		"""
		param = Conversions.bool_to_str(fixed)
		self._core.io.write(f'SOURce<HwInstance>:BB:DAB:TRIGger:OUTPut:DELay:FIXed {param}')

	def clone(self) -> 'Delay':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Delay(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
