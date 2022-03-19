from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfOff:
	"""RfOff commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfOff", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce]:ROSCillator:EXTernal:RFOFf:[STATe] \n
		Snippet: value: bool = driver.source.roscillator.external.rfOff.get_state() \n
		Determines that the RF output is turned off when the external reference signal is selected, but missing. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce:ROSCillator:EXTernal:RFOFf:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce]:ROSCillator:EXTernal:RFOFf:[STATe] \n
		Snippet: driver.source.roscillator.external.rfOff.set_state(state = False) \n
		Determines that the RF output is turned off when the external reference signal is selected, but missing. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce:ROSCillator:EXTernal:RFOFf:STATe {param}')
