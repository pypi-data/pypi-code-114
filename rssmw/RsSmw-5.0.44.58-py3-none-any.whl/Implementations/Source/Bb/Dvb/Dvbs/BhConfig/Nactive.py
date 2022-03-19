from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nactive:
	"""Nactive commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nactive", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:BHConfig:NACTive:[STATe] \n
		Snippet: value: bool = driver.source.bb.dvb.dvbs.bhConfig.nactive.get_state() \n
		Activates null-packet deletion (NPD) . \n
			:return: nactive: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBS:BHConfig:NACTive:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, nactive: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:BHConfig:NACTive:[STATe] \n
		Snippet: driver.source.bb.dvb.dvbs.bhConfig.nactive.set_state(nactive = False) \n
		Activates null-packet deletion (NPD) . \n
			:param nactive: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(nactive)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:BHConfig:NACTive:STATe {param}')
