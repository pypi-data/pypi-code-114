from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Delay:
	"""Delay commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("delay", core, parent)

	def get_offset(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:COUPled:TRIGger:DELay:OFFSet \n
		Snippet: value: float = driver.source.bb.arbitrary.coupled.trigger.delay.get_offset() \n
		Sets a time delay to delay the waveform processing of a particular baseband. \n
			:return: offset: float Range: 0 to 2147483647/clockrate
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:COUPled:TRIGger:DELay:OFFSet?')
		return Conversions.str_to_float(response)

	def set_offset(self, offset: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:COUPled:TRIGger:DELay:OFFSet \n
		Snippet: driver.source.bb.arbitrary.coupled.trigger.delay.set_offset(offset = 1.0) \n
		Sets a time delay to delay the waveform processing of a particular baseband. \n
			:param offset: float Range: 0 to 2147483647/clockrate
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:COUPled:TRIGger:DELay:OFFSet {param}')
