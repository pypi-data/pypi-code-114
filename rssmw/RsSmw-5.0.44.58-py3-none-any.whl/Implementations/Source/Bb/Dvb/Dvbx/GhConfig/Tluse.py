from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tluse:
	"""Tluse commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tluse", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:GHConfig:TLUSe:[STATe] \n
		Snippet: value: bool = driver.source.bb.dvb.dvbx.ghConfig.tluse.get_state() \n
		Includes the total length indication in the GSE header. \n
			:return: tluse: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:GHConfig:TLUSe:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, tluse: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:GHConfig:TLUSe:[STATe] \n
		Snippet: driver.source.bb.dvb.dvbx.ghConfig.tluse.set_state(tluse = False) \n
		Includes the total length indication in the GSE header. \n
			:param tluse: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(tluse)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:GHConfig:TLUSe:STATe {param}')
