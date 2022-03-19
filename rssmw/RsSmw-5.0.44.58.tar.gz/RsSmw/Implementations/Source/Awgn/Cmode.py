from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cmode:
	"""Cmode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cmode", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:AWGN:CMODe:[STATe] \n
		Snippet: value: bool = driver.source.awgn.cmode.get_state() \n
		Couples the configuration of all streams. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AWGN:CMODe:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:AWGN:CMODe:[STATe] \n
		Snippet: driver.source.awgn.cmode.set_state(state = False) \n
		Couples the configuration of all streams. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:AWGN:CMODe:STATe {param}')
