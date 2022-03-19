from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Allowed:
	"""Allowed commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("allowed", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:FREQuency:CONVerter:EXTernal:OVERrange:ALLowed:[STATe] \n
		Snippet: value: bool = driver.source.frequency.converter.external.overrange.allowed.get_state() \n
		Queries if the connected R&S SZU provides the extended frequency range. If confirmed, the R&S SMW indicates the
		correpsonding parameters in the 'RF Frequency' dialog, see 'Frequency Overrange'. \n
			:return: overrang_allowed: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:CONVerter:EXTernal:OVERrange:ALLowed:STATe?')
		return Conversions.str_to_bool(response)
