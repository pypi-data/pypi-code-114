from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Settings:
	"""Settings commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("settings", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DTMB:[SPECial]:SETTings:[STATe] \n
		Snippet: value: bool = driver.source.bb.dtmb.special.settings.get_state() \n
		Enables/disables special settings. The setting allows you to switch between standard-compliant and user-defined channel
		coding. \n
			:return: dtmb_special: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DTMB:SPECial:SETTings:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, dtmb_special: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DTMB:[SPECial]:SETTings:[STATe] \n
		Snippet: driver.source.bb.dtmb.special.settings.set_state(dtmb_special = False) \n
		Enables/disables special settings. The setting allows you to switch between standard-compliant and user-defined channel
		coding. \n
			:param dtmb_special: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(dtmb_special)
		self._core.io.write(f'SOURce<HwInstance>:BB:DTMB:SPECial:SETTings:STATe {param}')
