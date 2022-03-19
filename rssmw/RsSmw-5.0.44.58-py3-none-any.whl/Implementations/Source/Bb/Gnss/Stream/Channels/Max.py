from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Max:
	"""Max commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("max", core, parent)

	def set(self, max_channels: int, stream=repcap.Stream.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:STReam<ST>:CHANnels:MAX \n
		Snippet: driver.source.bb.gnss.stream.channels.max.set(max_channels = 1, stream = repcap.Stream.Default) \n
		Sets the maximum number of channels per stream. See also 'Channel budget'. \n
			:param max_channels: integer Range: 0 to depends on options
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
		"""
		param = Conversions.decimal_value_to_str(max_channels)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:STReam{stream_cmd_val}:CHANnels:MAX {param}')

	def get(self, stream=repcap.Stream.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:STReam<ST>:CHANnels:MAX \n
		Snippet: value: int = driver.source.bb.gnss.stream.channels.max.get(stream = repcap.Stream.Default) \n
		Sets the maximum number of channels per stream. See also 'Channel budget'. \n
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:return: max_channels: integer Range: 0 to depends on options"""
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:STReam{stream_cmd_val}:CHANnels:MAX?')
		return Conversions.str_to_int(response)
