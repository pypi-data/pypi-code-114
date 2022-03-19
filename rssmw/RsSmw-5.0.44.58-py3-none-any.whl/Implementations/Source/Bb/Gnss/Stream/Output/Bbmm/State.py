from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, stream=repcap.Stream.Default, iqConnector=repcap.IqConnector.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:STReam<ST>:OUTPut:BBMM<CH>:STATe \n
		Snippet: driver.source.bb.gnss.stream.output.bbmm.state.set(state = False, stream = repcap.Stream.Default, iqConnector = repcap.IqConnector.Default) \n
		Sets the output state of the GNSS stream at the BBMM 1/2 output. \n
			:param state: 1| ON| 0| OFF
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
		"""
		param = Conversions.bool_to_str(state)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:STReam{stream_cmd_val}:OUTPut:BBMM{iqConnector_cmd_val}:STATe {param}')

	def get(self, stream=repcap.Stream.Default, iqConnector=repcap.IqConnector.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:STReam<ST>:OUTPut:BBMM<CH>:STATe \n
		Snippet: value: bool = driver.source.bb.gnss.stream.output.bbmm.state.get(stream = repcap.Stream.Default, iqConnector = repcap.IqConnector.Default) \n
		Sets the output state of the GNSS stream at the BBMM 1/2 output. \n
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:param iqConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bbmm')
			:return: state: 1| ON| 0| OFF"""
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		iqConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(iqConnector, repcap.IqConnector)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:STReam{stream_cmd_val}:OUTPut:BBMM{iqConnector_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
