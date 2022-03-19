from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Utilities import trim_str_response
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Signals:
	"""Signals commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("signals", core, parent)

	def get(self, stream=repcap.Stream.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:GNSS:RT:[STReam<CH>]:GLONass:ACTive:SIGNals \n
		Snippet: value: str = driver.source.bb.gnss.rt.stream.glonass.active.signals.get(stream = repcap.Stream.Default) \n
		Queries active signals of a GNSS in a comma-separated list. \n
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:return: active_signals: string"""
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:RT:STReam{stream_cmd_val}:GLONass:ACTive:SIGNals?')
		return trim_str_response(response)
