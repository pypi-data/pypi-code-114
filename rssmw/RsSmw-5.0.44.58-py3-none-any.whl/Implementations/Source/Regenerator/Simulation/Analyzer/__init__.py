from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Analyzer:
	"""Analyzer commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("analyzer", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	# noinspection PyTypeChecker
	def get_status(self) -> enums.RegSimFreqRefFswState:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:ANALyzer:STATus \n
		Snippet: value: enums.RegSimFreqRefFswState = driver.source.regenerator.simulation.analyzer.get_status() \n
		Queries the frequency status. The command can be used only if a R&S FSW is connected to the R&S SMW. \n
			:return: status: VALid| UPDated
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:SIMulation:ANALyzer:STATus?')
		return Conversions.str_to_scalar_enum(response, enums.RegSimFreqRefFswState)

	def set_status(self, status: enums.RegSimFreqRefFswState) -> None:
		"""SCPI: [SOURce<HW>]:REGenerator:SIMulation:ANALyzer:STATus \n
		Snippet: driver.source.regenerator.simulation.analyzer.set_status(status = enums.RegSimFreqRefFswState.UPDated) \n
		Queries the frequency status. The command can be used only if a R&S FSW is connected to the R&S SMW. \n
			:param status: VALid| UPDated
		"""
		param = Conversions.enum_scalar_to_str(status, enums.RegSimFreqRefFswState)
		self._core.io.write(f'SOURce<HwInstance>:REGenerator:SIMulation:ANALyzer:STATus {param}')

	def clone(self) -> 'Analyzer':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Analyzer(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
