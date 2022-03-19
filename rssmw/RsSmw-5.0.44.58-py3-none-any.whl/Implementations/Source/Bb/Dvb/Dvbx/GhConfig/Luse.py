from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Luse:
	"""Luse commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("luse", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:GHConfig:LUSE:[STATe] \n
		Snippet: value: bool = driver.source.bb.dvb.dvbx.ghConfig.luse.get_state() \n
		Includes the label indication in the GSE header. \n
			:return: luse: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:GHConfig:LUSE:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, luse: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:GHConfig:LUSE:[STATe] \n
		Snippet: driver.source.bb.dvb.dvbx.ghConfig.luse.set_state(luse = False) \n
		Includes the label indication in the GSE header. \n
			:param luse: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(luse)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:GHConfig:LUSE:STATe {param}')
