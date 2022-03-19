from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.Rosc1GoUtpFreqMode:
		"""SCPI: [SOURce]:ROSCillator:OUTPut:ALTernate:FREQuency:MODE \n
		Snippet: value: enums.Rosc1GoUtpFreqMode = driver.source.roscillator.output.alternate.frequency.get_mode() \n
		No command help available \n
			:return: outp_freq_mode: No help available
		"""
		response = self._core.io.query_str('SOURce:ROSCillator:OUTPut:ALTernate:FREQuency:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.Rosc1GoUtpFreqMode)

	def set_mode(self, outp_freq_mode: enums.Rosc1GoUtpFreqMode) -> None:
		"""SCPI: [SOURce]:ROSCillator:OUTPut:ALTernate:FREQuency:MODE \n
		Snippet: driver.source.roscillator.output.alternate.frequency.set_mode(outp_freq_mode = enums.Rosc1GoUtpFreqMode.DER1G) \n
		No command help available \n
			:param outp_freq_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(outp_freq_mode, enums.Rosc1GoUtpFreqMode)
		self._core.io.write(f'SOURce:ROSCillator:OUTPut:ALTernate:FREQuency:MODE {param}')
