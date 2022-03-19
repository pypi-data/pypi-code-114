from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GlActive:
	"""GlActive commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("glActive", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:BHConfig:GLACtive:[STATe] \n
		Snippet: value: bool = driver.source.bb.dvb.dvbx.bhConfig.glActive.get_state() \n
		Sets that the GSE stream is GSE-Lite compliant. \n
			:return: gl_active: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBX:BHConfig:GLACtive:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, gl_active: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBX:BHConfig:GLACtive:[STATe] \n
		Snippet: driver.source.bb.dvb.dvbx.bhConfig.glActive.set_state(gl_active = False) \n
		Sets that the GSE stream is GSE-Lite compliant. \n
			:param gl_active: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(gl_active)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBX:BHConfig:GLACtive:STATe {param}')
