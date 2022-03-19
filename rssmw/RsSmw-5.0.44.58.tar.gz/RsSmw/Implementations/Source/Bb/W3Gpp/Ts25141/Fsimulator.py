from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fsimulator:
	"""Fsimulator commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fsimulator", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:FSIMulator:STATe \n
		Snippet: value: bool = driver.source.bb.w3Gpp.ts25141.fsimulator.get_state() \n
		Queries the state of the fading simulator. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce:BB:W3GPp:TS25141:FSIMulator:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce]:BB:W3GPp:TS25141:FSIMulator:STATe \n
		Snippet: driver.source.bb.w3Gpp.ts25141.fsimulator.set_state(state = False) \n
		Queries the state of the fading simulator. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce:BB:W3GPp:TS25141:FSIMulator:STATe {param}')
