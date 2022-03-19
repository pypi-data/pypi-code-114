from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pramp:
	"""Pramp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pramp", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:PRAMp:[STATe] \n
		Snippet: value: bool = driver.source.bb.arbitrary.pramp.get_state() \n
		If activated, the burst gate marker signal included in the ARB waveform file is used as marker signal for the pulse
		modulator. \n
			:return: arb_pram_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:PRAMp:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, arb_pram_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:PRAMp:[STATe] \n
		Snippet: driver.source.bb.arbitrary.pramp.set_state(arb_pram_state = False) \n
		If activated, the burst gate marker signal included in the ARB waveform file is used as marker signal for the pulse
		modulator. \n
			:param arb_pram_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(arb_pram_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:PRAMp:STATe {param}')
