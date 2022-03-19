from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Measurement:
	"""Measurement commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:IQ:DPD:MEASurement:STATe \n
		Snippet: value: bool = driver.source.iq.dpd.measurement.get_state() \n
		Queries whether the interactions are competed. \n
			:return: measure_validity: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DPD:MEASurement:STATe?')
		return Conversions.str_to_bool(response)
