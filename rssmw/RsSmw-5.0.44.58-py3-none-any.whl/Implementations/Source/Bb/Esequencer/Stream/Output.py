from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Output:
	"""Output commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("output", core, parent)

	def set(self, output: enums.Output, twoStreams=repcap.TwoStreams.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:STReam<DI>:OUTPut \n
		Snippet: driver.source.bb.esequencer.stream.output.set(output = enums.Output.NONE, twoStreams = repcap.TwoStreams.Default) \n
		Selects the RF output the stream is routed to. \n
			:param output: NONE| RFA| RFB NONE Disable the stream output.
			:param twoStreams: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
		"""
		param = Conversions.enum_scalar_to_str(output, enums.Output)
		twoStreams_cmd_val = self._cmd_group.get_repcap_cmd_value(twoStreams, repcap.TwoStreams)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:STReam{twoStreams_cmd_val}:OUTPut {param}')

	# noinspection PyTypeChecker
	def get(self, twoStreams=repcap.TwoStreams.Default) -> enums.Output:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:STReam<DI>:OUTPut \n
		Snippet: value: enums.Output = driver.source.bb.esequencer.stream.output.get(twoStreams = repcap.TwoStreams.Default) \n
		Selects the RF output the stream is routed to. \n
			:param twoStreams: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:return: output: NONE| RFA| RFB NONE Disable the stream output."""
		twoStreams_cmd_val = self._cmd_group.get_repcap_cmd_value(twoStreams, repcap.TwoStreams)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:STReam{twoStreams_cmd_val}:OUTPut?')
		return Conversions.str_to_scalar_enum(response, enums.Output)
