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

	def set(self, source: enums.FmSour, generatorIx=repcap.GeneratorIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:FM<CH>:SOURce \n
		Snippet: driver.source.fm.source.set(source = enums.FmSour.EXT1, generatorIx = repcap.GeneratorIx.Default) \n
		Selects the modulation source for frequency modulation. \n
			:param source: INTernal| EXTernal| LF1| LF2| NOISe| EXT1| EXT2 | INTB LF1|LF2 Uses an internally generated LF signal. INTernal = LF2 Works like LF1 EXTernal Works like EXT1 EXT1|EXT2 Uses an externally supplied LF signal. NOISe Uses the internally generated noise signal. INTB Uses the internal baseband signal.
			:param generatorIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fm')
		"""
		param = Conversions.enum_scalar_to_str(source, enums.FmSour)
		generatorIx_cmd_val = self._cmd_group.get_repcap_cmd_value(generatorIx, repcap.GeneratorIx)
		self._core.io.write(f'SOURce<HwInstance>:FM{generatorIx_cmd_val}:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self, generatorIx=repcap.GeneratorIx.Default) -> enums.FmSour:
		"""SCPI: [SOURce<HW>]:FM<CH>:SOURce \n
		Snippet: value: enums.FmSour = driver.source.fm.source.get(generatorIx = repcap.GeneratorIx.Default) \n
		Selects the modulation source for frequency modulation. \n
			:param generatorIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fm')
			:return: source: INTernal| EXTernal| LF1| LF2| NOISe| EXT1| EXT2 | INTB LF1|LF2 Uses an internally generated LF signal. INTernal = LF2 Works like LF1 EXTernal Works like EXT1 EXT1|EXT2 Uses an externally supplied LF signal. NOISe Uses the internally generated noise signal. INTB Uses the internal baseband signal."""
		generatorIx_cmd_val = self._cmd_group.get_repcap_cmd_value(generatorIx, repcap.GeneratorIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FM{generatorIx_cmd_val}:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.FmSour)
