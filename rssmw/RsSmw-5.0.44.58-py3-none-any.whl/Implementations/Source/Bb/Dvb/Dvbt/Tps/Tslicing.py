from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tslicing:
	"""Tslicing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tslicing", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBT:TPS:TSLicing:[STATe] \n
		Snippet: value: bool = driver.source.bb.dvb.dvbt.tps.tslicing.get_state() \n
		Queries the time slicing state. \n
			:return: state: 0| 1| OFF| ON Always 1 for DVB-H Always 0 for DVB-T
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBT:TPS:TSLicing:STATe?')
		return Conversions.str_to_bool(response)
