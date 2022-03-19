from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PiChannel:
	"""PiChannel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("piChannel", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:C2K:PPARameter:PICHannel:[STATe] \n
		Snippet: value: bool = driver.source.bb.c2K.pparameter.piChannel.get_state() \n
		The command activates/deactivates the pilot channel. The setting takes effect only after execution of command
		[:SOURce<hw>]:BB:C2K:PPARameter:EXECute. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:PPARameter:PICHannel:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:PPARameter:PICHannel:[STATe] \n
		Snippet: driver.source.bb.c2K.pparameter.piChannel.set_state(state = False) \n
		The command activates/deactivates the pilot channel. The setting takes effect only after execution of command
		[:SOURce<hw>]:BB:C2K:PPARameter:EXECute. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:PPARameter:PICHannel:STATe {param}')
