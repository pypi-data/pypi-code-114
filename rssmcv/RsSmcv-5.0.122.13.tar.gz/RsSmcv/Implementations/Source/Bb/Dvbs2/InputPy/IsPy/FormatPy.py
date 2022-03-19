from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPy:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, input_format: enums.CodingInputFormat, inputStream=repcap.InputStream.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:INPut:[IS<CH>]:FORMat \n
		Snippet: driver.source.bb.dvbs2.inputPy.isPy.formatPy.set(input_format = enums.CodingInputFormat.ASI, inputStream = repcap.InputStream.Default) \n
		Sets the format of the input signal. \n
			:param input_format: SMPTE| ASI
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
		"""
		param = Conversions.enum_scalar_to_str(input_format, enums.CodingInputFormat)
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:INPut:IS{inputStream_cmd_val}:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self, inputStream=repcap.InputStream.Default) -> enums.CodingInputFormat:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:INPut:[IS<CH>]:FORMat \n
		Snippet: value: enums.CodingInputFormat = driver.source.bb.dvbs2.inputPy.isPy.formatPy.get(inputStream = repcap.InputStream.Default) \n
		Sets the format of the input signal. \n
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
			:return: input_format: SMPTE| ASI"""
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVBS2:INPut:IS{inputStream_cmd_val}:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.CodingInputFormat)
