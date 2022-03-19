from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Allocated:
	"""Allocated commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("allocated", core, parent)

	def get(self, stream=repcap.Stream.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:STReam<ST>:BB:CHANnels:ALLocated \n
		Snippet: value: int = driver.source.bb.gnss.stream.bb.channels.allocated.get(stream = repcap.Stream.Default) \n
		Queries the maximum number of channels of the selected GNSS stream. For details, see 'Channel budget'. \n
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:return: allocated_chans: integer Range: 0 to 144"""
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:STReam{stream_cmd_val}:BB:CHANnels:ALLocated?')
		return Conversions.str_to_int(response)
