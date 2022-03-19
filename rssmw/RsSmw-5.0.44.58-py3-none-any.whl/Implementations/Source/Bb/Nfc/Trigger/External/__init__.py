from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class External:
	"""External commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("external", core, parent)

	@property
	def synchronize(self):
		"""synchronize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_synchronize'):
			from .Synchronize import Synchronize
			self._synchronize = Synchronize(self._core, self._cmd_group)
		return self._synchronize

	def get_delay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NFC:TRIGger:[EXTernal]:DELay \n
		Snippet: value: float = driver.source.bb.nfc.trigger.external.get_delay() \n
		Sets the trigger signal delay in samples on external triggering or on internal triggering via the second path (if
		applicable) . The numeric suffix to EXTernal distinguishes between the external trigger via the multipurpose connectors. \n
			:return: delay: float Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:TRIGger:EXTernal:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:TRIGger:[EXTernal]:DELay \n
		Snippet: driver.source.bb.nfc.trigger.external.set_delay(delay = 1.0) \n
		Sets the trigger signal delay in samples on external triggering or on internal triggering via the second path (if
		applicable) . The numeric suffix to EXTernal distinguishes between the external trigger via the multipurpose connectors. \n
			:param delay: float Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:TRIGger:EXTernal:DELay {param}')

	def get_inhibit(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NFC:TRIGger:[EXTernal]:INHibit \n
		Snippet: value: int = driver.source.bb.nfc.trigger.external.get_inhibit() \n
		Sets the duration for inhibiting a new trigger event subsequent to triggering. The input is to be expressed in samples. \n
			:return: inhibit: integer Range: 0 to 67108863
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NFC:TRIGger:EXTernal:INHibit?')
		return Conversions.str_to_int(response)

	def set_inhibit(self, inhibit: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:TRIGger:[EXTernal]:INHibit \n
		Snippet: driver.source.bb.nfc.trigger.external.set_inhibit(inhibit = 1) \n
		Sets the duration for inhibiting a new trigger event subsequent to triggering. The input is to be expressed in samples. \n
			:param inhibit: integer Range: 0 to 67108863
		"""
		param = Conversions.decimal_value_to_str(inhibit)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:TRIGger:EXTernal:INHibit {param}')

	def clone(self) -> 'External':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = External(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
