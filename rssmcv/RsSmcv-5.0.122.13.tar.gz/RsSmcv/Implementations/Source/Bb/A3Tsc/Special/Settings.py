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
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SPECial:SETTings:[STATe] \n
		Snippet: value: bool = driver.source.bb.a3Tsc.special.settings.get_state() \n
		Enables/disables special settings. The setting allows you to switch between standard-compliant and user-defined channel
		coding. \n
			:return: special_settings: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:SPECial:SETTings:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, special_settings: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SPECial:SETTings:[STATe] \n
		Snippet: driver.source.bb.a3Tsc.special.settings.set_state(special_settings = False) \n
		Enables/disables special settings. The setting allows you to switch between standard-compliant and user-defined channel
		coding. \n
			:param special_settings: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(special_settings)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:SPECial:SETTings:STATe {param}')
