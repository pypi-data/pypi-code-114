from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ethernet:
	"""Ethernet commands group definition. 12 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ethernet", core, parent)

	@property
	def statistics(self):
		"""statistics commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_statistics'):
			from .Statistics import Statistics
			self._statistics = Statistics(self._core, self._cmd_group)
		return self._statistics

	@property
	def waveform(self):
		"""waveform commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_waveform'):
			from .Waveform import Waveform
			self._waveform = Waveform(self._core, self._cmd_group)
		return self._waveform

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ArbEthMode:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:ETHernet:MODE \n
		Snippet: value: enums.ArbEthMode = driver.source.bb.arbitrary.ethernet.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:ETHernet:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ArbEthMode)

	def set_mode(self, mode: enums.ArbEthMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:ETHernet:MODE \n
		Snippet: driver.source.bb.arbitrary.ethernet.set_mode(mode = enums.ArbEthMode.M10G) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ArbEthMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:ETHernet:MODE {param}')

	def get_status(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:ETHernet:STATus \n
		Snippet: value: str = driver.source.bb.arbitrary.ethernet.get_status() \n
		No command help available \n
			:return: status: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:ETHernet:STATus?')
		return trim_str_response(response)

	def clone(self) -> 'Ethernet':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ethernet(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
