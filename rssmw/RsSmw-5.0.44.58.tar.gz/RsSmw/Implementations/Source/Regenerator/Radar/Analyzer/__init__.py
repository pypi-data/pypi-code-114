from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Analyzer:
	"""Analyzer commands group definition. 4 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("analyzer", core, parent)

	@property
	def power(self):
		"""power commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	# noinspection PyTypeChecker
	def get_status(self) -> enums.RegRadarPowRefFswStatus:
		"""SCPI: [SOURce<HW>]:REGenerator:RADar:ANALyzer:STATus \n
		Snippet: value: enums.RegRadarPowRefFswStatus = driver.source.regenerator.radar.analyzer.get_status() \n
		Queries the reference level status. The command can be used only if a R&S FSW is connected to the R&S SMW. \n
			:return: analyzer_status: NCONected| INValid| VALid| UPDated NCONected Analyzer is not connected INValid Reference level outside the permissible level range of the analyzer VALid Reference level within the permissible level range of the analyzer; value not set UPDated Refence level is updated
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:RADar:ANALyzer:STATus?')
		return Conversions.str_to_scalar_enum(response, enums.RegRadarPowRefFswStatus)

	def clone(self) -> 'Analyzer':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Analyzer(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
