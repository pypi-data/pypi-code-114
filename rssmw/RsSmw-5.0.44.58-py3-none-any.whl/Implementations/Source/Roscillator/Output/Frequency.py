from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.RoscOutpFreqMode:
		"""SCPI: [SOURce]:ROSCillator:OUTPut:FREQuency:MODE \n
		Snippet: value: enums.RoscOutpFreqMode = driver.source.roscillator.output.frequency.get_mode() \n
		Selects the mode for the determination and output of the reference frequency. \n
			:return: outp_freq_mode: DER10M| SAME
		"""
		response = self._core.io.query_str('SOURce:ROSCillator:OUTPut:FREQuency:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.RoscOutpFreqMode)

	def set_mode(self, outp_freq_mode: enums.RoscOutpFreqMode) -> None:
		"""SCPI: [SOURce]:ROSCillator:OUTPut:FREQuency:MODE \n
		Snippet: driver.source.roscillator.output.frequency.set_mode(outp_freq_mode = enums.RoscOutpFreqMode.DER100M) \n
		Selects the mode for the determination and output of the reference frequency. \n
			:param outp_freq_mode: DER10M| SAME
		"""
		param = Conversions.enum_scalar_to_str(outp_freq_mode, enums.RoscOutpFreqMode)
		self._core.io.write(f'SOURce:ROSCillator:OUTPut:FREQuency:MODE {param}')
