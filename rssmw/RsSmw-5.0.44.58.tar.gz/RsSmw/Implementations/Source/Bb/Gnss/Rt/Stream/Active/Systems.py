from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Systems:
	"""Systems commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("systems", core, parent)

	def get(self, stream=repcap.Stream.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RT:[STReam<CH>]:ACTive:SYSTems \n
		Snippet: value: str = driver.source.bb.gnss.rt.stream.active.systems.get(stream = repcap.Stream.Default) \n
		Queries active GNSS in a comma-separated string. \n
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:return: active_systems: string"""
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RT:STReam{stream_cmd_val}:ACTive:SYSTems?')
		return trim_str_response(response)
