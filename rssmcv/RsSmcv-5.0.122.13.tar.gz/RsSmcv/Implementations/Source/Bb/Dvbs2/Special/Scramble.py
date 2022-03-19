from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scramble:
	"""Scramble commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scramble", core, parent)

	def get_sequence(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:[SPECial]:SCRamble:SEQuence \n
		Snippet: value: float = driver.source.bb.dvbs2.special.scramble.get_sequence() \n
		For normal applications, set this parameter to 0. If ≠ 0 is set, the corresponding line of a hidden file is evaluated. PL
		header scrambling is performed, and the 'PL Gold Code Index (n) ' is set using the dedicated values of this line.
		The results are not displayed and are not readable. Also set the PL scrambling sequence ID in the DVB-S2 receiver. \n
			:return: scr_sequ: float Range: 0 to 9999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS2:SPECial:SCRamble:SEQuence?')
		return Conversions.str_to_float(response)

	def set_sequence(self, scr_sequ: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:[SPECial]:SCRamble:SEQuence \n
		Snippet: driver.source.bb.dvbs2.special.scramble.set_sequence(scr_sequ = 1.0) \n
		For normal applications, set this parameter to 0. If ≠ 0 is set, the corresponding line of a hidden file is evaluated. PL
		header scrambling is performed, and the 'PL Gold Code Index (n) ' is set using the dedicated values of this line.
		The results are not displayed and are not readable. Also set the PL scrambling sequence ID in the DVB-S2 receiver. \n
			:param scr_sequ: float Range: 0 to 9999
		"""
		param = Conversions.decimal_value_to_str(scr_sequ)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:SPECial:SCRamble:SEQuence {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:[SPECial]:SCRamble:STATe \n
		Snippet: value: bool = driver.source.bb.dvbs2.special.scramble.get_state() \n
		For test purposes, you can disable the PL scrambler. In normal operation it is enabled. \n
			:return: scrambler: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS2:SPECial:SCRamble:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, scrambler: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:[SPECial]:SCRamble:STATe \n
		Snippet: driver.source.bb.dvbs2.special.scramble.set_state(scrambler = False) \n
		For test purposes, you can disable the PL scrambler. In normal operation it is enabled. \n
			:param scrambler: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(scrambler)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:SPECial:SCRamble:STATe {param}')
