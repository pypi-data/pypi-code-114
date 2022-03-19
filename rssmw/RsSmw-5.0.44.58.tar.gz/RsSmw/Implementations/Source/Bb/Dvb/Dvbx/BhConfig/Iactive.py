from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iactive:
	"""Iactive commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iactive", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:BHConfig:IACTive:[STATe] \n
		Snippet: value: bool = driver.source.bb.dvb.dvbx.bhConfig.iactive.get_state() \n
		Sets the ISSYI (input stream synchronization indicator) bit to 1. \n
			:return: iactive: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:BHConfig:IACTive:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, iactive: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:BHConfig:IACTive:[STATe] \n
		Snippet: driver.source.bb.dvb.dvbx.bhConfig.iactive.set_state(iactive = False) \n
		Sets the ISSYI (input stream synchronization indicator) bit to 1. \n
			:param iactive: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(iactive)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:BHConfig:IACTive:STATe {param}')
