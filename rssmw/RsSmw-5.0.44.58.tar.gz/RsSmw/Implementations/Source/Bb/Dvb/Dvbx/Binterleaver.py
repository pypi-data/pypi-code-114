from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Binterleaver:
	"""Binterleaver commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("binterleaver", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:BINTerleaver:[STATe] \n
		Snippet: value: bool = driver.source.bb.dvb.dvbx.binterleaver.get_state() \n
		Enables the bit interleaver. \n
			:return: binterleaver: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:BINTerleaver:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, binterleaver: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:BINTerleaver:[STATe] \n
		Snippet: driver.source.bb.dvb.dvbx.binterleaver.set_state(binterleaver = False) \n
		Enables the bit interleaver. \n
			:param binterleaver: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(binterleaver)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:BINTerleaver:STATe {param}')
