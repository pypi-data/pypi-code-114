from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Measure:
	"""Measure commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measure", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CFR:MEASure:[STATe] \n
		Snippet: value: bool = driver.source.bb.arbitrary.cfr.measure.get_state() \n
		Queries the state of the crest factor reduction calculation. \n
			:return: measure_state: 1| ON| 0| OFF ON: the original and resulting crest factors are already calculated.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:CFR:MEASure:STATe?')
		return Conversions.str_to_bool(response)
