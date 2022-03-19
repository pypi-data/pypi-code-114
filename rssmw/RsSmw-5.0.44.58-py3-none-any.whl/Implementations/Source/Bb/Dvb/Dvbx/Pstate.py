from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pstate:
	"""Pstate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pstate", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:PSTATe:[STATe] \n
		Snippet: value: bool = driver.source.bb.dvb.dvbx.pstate.get_state() \n
		Activates the pilot. \n
			:return: pstate: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:PSTATe:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, pstate: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:PSTATe:[STATe] \n
		Snippet: driver.source.bb.dvb.dvbx.pstate.set_state(pstate = False) \n
		Activates the pilot. \n
			:param pstate: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(pstate)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:PSTATe:STATe {param}')
