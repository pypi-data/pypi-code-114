from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PtUse:
	"""PtUse commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ptUse", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:GHConfig:PTUSe:[STATe] \n
		Snippet: value: bool = driver.source.bb.dvb.dvbx.ghConfig.ptUse.get_state() \n
		Includes the payload type indication in the GSE header. \n
			:return: pt_use: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:GHConfig:PTUSe:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, pt_use: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:GHConfig:PTUSe:[STATe] \n
		Snippet: driver.source.bb.dvb.dvbx.ghConfig.ptUse.set_state(pt_use = False) \n
		Includes the payload type indication in the GSE header. \n
			:param pt_use: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(pt_use)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:GHConfig:PTUSe:STATe {param}')
