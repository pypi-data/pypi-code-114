from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Setting:
	"""Setting commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("setting", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:J83B:[SPECial]:SETTing:[STATe] \n
		Snippet: value: bool = driver.source.bb.j83B.special.setting.get_state() \n
		Enables/disables special settings. \n
			:return: special_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:J83B:SPECial:SETTing:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, special_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:J83B:[SPECial]:SETTing:[STATe] \n
		Snippet: driver.source.bb.j83B.special.setting.set_state(special_state = False) \n
		Enables/disables special settings. \n
			:param special_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(special_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:J83B:SPECial:SETTing:STATe {param}')
