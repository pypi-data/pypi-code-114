from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, source: enums.LfSource, lfOutput=repcap.LfOutput.Default) -> None:
		"""SCPI: [SOURce]:LFOutput<CH>:SOURce \n
		Snippet: driver.source.lfOutput.source.set(source = enums.LfSource.AM, lfOutput = repcap.LfOutput.Default) \n
		Determines the LF signal to be synchronized, when monitoring is enabled. \n
			:param source: LF1| LF2| NOISe| AM| FMPM| EXT1 | | EXT2| LF1B| LF2B| AMB| NOISB| FMPMB| LF1A| LF2A| NOISA| FMPMA| AMA LF1|LF2|LF1A|LF2A|LF1B|LF2B Selects an internally generated LF signal. NOISe|NOISA|NOISB Selects an internally generated noise signal. EXT1|EXT2 Selects an externally supplied LF signal AM|AMA|AMB Selects the AM signal. FMPM|FMPMA|FMPMB Selects the signal also used by the frequency or phase modulations.
			:param lfOutput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'LfOutput')
		"""
		param = Conversions.enum_scalar_to_str(source, enums.LfSource)
		lfOutput_cmd_val = self._cmd_group.get_repcap_cmd_value(lfOutput, repcap.LfOutput)
		self._core.io.write(f'SOURce:LFOutput{lfOutput_cmd_val}:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self, lfOutput=repcap.LfOutput.Default) -> enums.LfSource:
		"""SCPI: [SOURce]:LFOutput<CH>:SOURce \n
		Snippet: value: enums.LfSource = driver.source.lfOutput.source.get(lfOutput = repcap.LfOutput.Default) \n
		Determines the LF signal to be synchronized, when monitoring is enabled. \n
			:param lfOutput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'LfOutput')
			:return: source: LF1| LF2| NOISe| AM| FMPM| EXT1 | | EXT2| LF1B| LF2B| AMB| NOISB| FMPMB| LF1A| LF2A| NOISA| FMPMA| AMA LF1|LF2|LF1A|LF2A|LF1B|LF2B Selects an internally generated LF signal. NOISe|NOISA|NOISB Selects an internally generated noise signal. EXT1|EXT2 Selects an externally supplied LF signal AM|AMA|AMB Selects the AM signal. FMPM|FMPMA|FMPMB Selects the signal also used by the frequency or phase modulations."""
		lfOutput_cmd_val = self._cmd_group.get_repcap_cmd_value(lfOutput, repcap.LfOutput)
		response = self._core.io.query_str(f'SOURce:LFOutput{lfOutput_cmd_val}:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.LfSource)
