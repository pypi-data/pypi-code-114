from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dfts:
	"""Dfts commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dfts", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:OFDM:DFTS:STATe \n
		Snippet: value: bool = driver.source.bb.ofdm.dfts.get_state() \n
		No command help available \n
			:return: dfts_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:DFTS:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, dfts_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:DFTS:STATe \n
		Snippet: driver.source.bb.ofdm.dfts.set_state(dfts_state = False) \n
		No command help available \n
			:param dfts_state: No help available
		"""
		param = Conversions.bool_to_str(dfts_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:DFTS:STATe {param}')
