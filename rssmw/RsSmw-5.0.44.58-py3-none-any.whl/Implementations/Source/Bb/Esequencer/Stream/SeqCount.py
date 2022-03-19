from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SeqCount:
	"""SeqCount commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("seqCount", core, parent)

	def set(self, max_num_of_sequences: int, twoStreams=repcap.TwoStreams.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:STReam<DI>:SEQCount \n
		Snippet: driver.source.bb.esequencer.stream.seqCount.set(max_num_of_sequences = 1, twoStreams = repcap.TwoStreams.Default) \n
		Sets how many sequencers can be mapped to the stream at most. \n
			:param max_num_of_sequences: integer Range: 1 to 3
			:param twoStreams: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
		"""
		param = Conversions.decimal_value_to_str(max_num_of_sequences)
		twoStreams_cmd_val = self._cmd_group.get_repcap_cmd_value(twoStreams, repcap.TwoStreams)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:STReam{twoStreams_cmd_val}:SEQCount {param}')

	def get(self, twoStreams=repcap.TwoStreams.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:STReam<DI>:SEQCount \n
		Snippet: value: int = driver.source.bb.esequencer.stream.seqCount.get(twoStreams = repcap.TwoStreams.Default) \n
		Sets how many sequencers can be mapped to the stream at most. \n
			:param twoStreams: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:return: max_num_of_sequences: integer Range: 1 to 3"""
		twoStreams_cmd_val = self._cmd_group.get_repcap_cmd_value(twoStreams, repcap.TwoStreams)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:STReam{twoStreams_cmd_val}:SEQCount?')
		return Conversions.str_to_int(response)
