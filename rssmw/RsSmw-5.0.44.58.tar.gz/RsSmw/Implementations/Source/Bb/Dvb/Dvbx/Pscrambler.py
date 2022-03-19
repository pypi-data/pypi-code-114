from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pscrambler:
	"""Pscrambler commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pscrambler", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:PSCRambler:[STATe] \n
		Snippet: value: bool = driver.source.bb.dvb.dvbx.pscrambler.get_state() \n
		Activates pilot scrambling. \n
			:return: pscrambler: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:PSCRambler:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, pscrambler: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:PSCRambler:[STATe] \n
		Snippet: driver.source.bb.dvb.dvbx.pscrambler.set_state(pscrambler = False) \n
		Activates pilot scrambling. \n
			:param pscrambler: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(pscrambler)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:PSCRambler:STATe {param}')
