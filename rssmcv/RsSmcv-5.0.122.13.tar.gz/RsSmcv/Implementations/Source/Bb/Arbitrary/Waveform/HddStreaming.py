from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HddStreaming:
	"""HddStreaming commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hddStreaming", core, parent)

	def get_blevel(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WAVeform:HDDStreaming:BLEVel \n
		Snippet: value: int = driver.source.bb.arbitrary.waveform.hddStreaming.get_blevel() \n
		No command help available \n
			:return: blevel: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:WAVeform:HDDStreaming:BLEVel?')
		return Conversions.str_to_int(response)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WAVeform:HDDStreaming:STATe \n
		Snippet: value: bool = driver.source.bb.arbitrary.waveform.hddStreaming.get_state() \n
		By processing large files, enables the streaming of modulation data directly from the hard drive (HDD) . \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:WAVeform:HDDStreaming:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WAVeform:HDDStreaming:STATe \n
		Snippet: driver.source.bb.arbitrary.waveform.hddStreaming.set_state(state = False) \n
		By processing large files, enables the streaming of modulation data directly from the hard drive (HDD) . \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:WAVeform:HDDStreaming:STATe {param}')
