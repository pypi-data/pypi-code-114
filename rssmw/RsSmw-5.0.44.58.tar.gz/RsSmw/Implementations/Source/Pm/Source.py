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
		"""SCPI: [SOURce<HW>]:PM<CH>:SOURce \n
		Snippet: driver.source.pm.source.set(source = enums.FmSour.EXT1, generatorIx = repcap.GeneratorIx.Default) \n
		Selects the modulation source for phase modulation signal. \n
			:param source: INTernal| EXTernal| LF1| LF2| NOISe| EXT1| EXT2 | INTB LF1|LF2 Uses an internally generated LF signal. EXT1|EXT2 Uses an externally supplied LF signal. NOISe Uses the internally generated noise signal. INTernal Uses the internally generated signal of LF1. EXTernal Uses an external LF signal (EXT1) . INTB Uses the internal baseband signal.
			:param generatorIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pm')
		"""
		param = Conversions.enum_scalar_to_str(source, enums.FmSour)
		generatorIx_cmd_val = self._cmd_group.get_repcap_cmd_value(generatorIx, repcap.GeneratorIx)
		self._core.io.write(f'SOURce<HwInstance>:PM{generatorIx_cmd_val}:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self, generatorIx=repcap.GeneratorIx.Default) -> enums.FmSour:
		"""SCPI: [SOURce<HW>]:PM<CH>:SOURce \n
		Snippet: value: enums.FmSour = driver.source.pm.source.get(generatorIx = repcap.GeneratorIx.Default) \n
		Selects the modulation source for phase modulation signal. \n
			:param generatorIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pm')
			:return: source: INTernal| EXTernal| LF1| LF2| NOISe| EXT1| EXT2 | INTB LF1|LF2 Uses an internally generated LF signal. EXT1|EXT2 Uses an externally supplied LF signal. NOISe Uses the internally generated noise signal. INTernal Uses the internally generated signal of LF1. EXTernal Uses an external LF signal (EXT1) . INTB Uses the internal baseband signal."""
		generatorIx_cmd_val = self._cmd_group.get_repcap_cmd_value(generatorIx, repcap.GeneratorIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:PM{generatorIx_cmd_val}:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.FmSour)
