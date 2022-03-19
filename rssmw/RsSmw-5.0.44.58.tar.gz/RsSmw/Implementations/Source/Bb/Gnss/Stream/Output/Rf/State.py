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

	def set(self, state: bool, stream=repcap.Stream.Default, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:STReam<ST>:OUTPut:RF<CH>:STATe \n
		Snippet: driver.source.bb.gnss.stream.output.rf.state.set(state = False, stream = repcap.Stream.Default, path = repcap.Path.Default) \n
		Sets the output state of the GNSS stream at the RF A/B output. \n
			:param state: 1| ON| 0| OFF
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
		"""
		param = Conversions.bool_to_str(state)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:STReam{stream_cmd_val}:OUTPut:RF{path_cmd_val}:STATe {param}')

	def get(self, stream=repcap.Stream.Default, path=repcap.Path.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:STReam<ST>:OUTPut:RF<CH>:STATe \n
		Snippet: value: bool = driver.source.bb.gnss.stream.output.rf.state.get(stream = repcap.Stream.Default, path = repcap.Path.Default) \n
		Sets the output state of the GNSS stream at the RF A/B output. \n
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
			:return: state: 1| ON| 0| OFF"""
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:STReam{stream_cmd_val}:OUTPut:RF{path_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
