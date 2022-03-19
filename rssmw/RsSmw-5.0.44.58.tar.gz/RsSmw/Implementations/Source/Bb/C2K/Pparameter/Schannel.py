from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Schannel:
	"""Schannel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("schannel", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:C2K:PPARameter:SCHannel:[STATe] \n
		Snippet: value: bool = driver.source.bb.c2K.pparameter.schannel.get_state() \n
		Activates/deactivates the F-SYNC.
		The setting takes effect only after execution of command [:SOURce<hw>]:BB:C2K:PPARameter:EXECute. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:C2K:PPARameter:SCHannel:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:PPARameter:SCHannel:[STATe] \n
		Snippet: driver.source.bb.c2K.pparameter.schannel.set_state(state = False) \n
		Activates/deactivates the F-SYNC.
		The setting takes effect only after execution of command [:SOURce<hw>]:BB:C2K:PPARameter:EXECute. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:PPARameter:SCHannel:STATe {param}')
