from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offline:
	"""Offline commands group definition. 5 total commands, 1 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offline", core, parent)

	@property
	def generate(self):
		"""generate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_generate'):
			from .Generate import Generate
			self._generate = Generate(self._core, self._cmd_group)
		return self._generate

	def abort(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:OFFLine:ABORt \n
		Snippet: driver.source.bb.gnss.logging.offline.abort() \n
		Logging files are created and saved. Files with the same name are overwritten. To stop the generation,
		send [:SOURce<hw>]:BB:GNSS:LOGGing:OFFLine:ABORt. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:OFFLine:ABORt')

	def abort_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:OFFLine:ABORt \n
		Snippet: driver.source.bb.gnss.logging.offline.abort_with_opc() \n
		Logging files are created and saved. Files with the same name are overwritten. To stop the generation,
		send [:SOURce<hw>]:BB:GNSS:LOGGing:OFFLine:ABORt. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:GNSS:LOGGing:OFFLine:ABORt', opc_timeout_ms)

	def get_duration(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:OFFLine:DURation \n
		Snippet: value: float = driver.source.bb.gnss.logging.offline.get_duration() \n
		Sets the logging duration. \n
			:return: duration: float Range: 0 to 864000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:OFFLine:DURation?')
		return Conversions.str_to_float(response)

	def set_duration(self, duration: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:OFFLine:DURation \n
		Snippet: driver.source.bb.gnss.logging.offline.set_duration(duration = 1.0) \n
		Sets the logging duration. \n
			:param duration: float Range: 0 to 864000
		"""
		param = Conversions.decimal_value_to_str(duration)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:OFFLine:DURation {param}')

	def get_progress(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:OFFLine:PROGress \n
		Snippet: value: int = driver.source.bb.gnss.logging.offline.get_progress() \n
		Querries the progress of the offline data logging generation. \n
			:return: progress: integer Range: 0 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:OFFLine:PROGress?')
		return Conversions.str_to_int(response)

	def get_toffset(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:OFFLine:TOFFset \n
		Snippet: value: float = driver.source.bb.gnss.logging.offline.get_toffset() \n
		Delays the logging start. \n
			:return: time_offset: float Range: 0 to 864000, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:LOGGing:OFFLine:TOFFset?')
		return Conversions.str_to_float(response)

	def set_toffset(self, time_offset: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:LOGGing:OFFLine:TOFFset \n
		Snippet: driver.source.bb.gnss.logging.offline.set_toffset(time_offset = 1.0) \n
		Delays the logging start. \n
			:param time_offset: float Range: 0 to 864000, Unit: s
		"""
		param = Conversions.decimal_value_to_str(time_offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:LOGGing:OFFLine:TOFFset {param}')

	def clone(self) -> 'Offline':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Offline(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
