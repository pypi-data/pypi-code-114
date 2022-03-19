from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Antenna:
	"""Antenna commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("antenna", core, parent)

	def set(self, antenna: enums.AntennaNr, stream=repcap.Stream.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:STReam<ST>:ANTenna \n
		Snippet: driver.source.bb.gnss.stream.antenna.set(antenna = enums.AntennaNr.A1, stream = repcap.Stream.Default) \n
		Selects the signal of which antenna is carried by which stream. \n
			:param antenna: A1| A2| A3| A4
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
		"""
		param = Conversions.enum_scalar_to_str(antenna, enums.AntennaNr)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:STReam{stream_cmd_val}:ANTenna {param}')

	# noinspection PyTypeChecker
	def get(self, stream=repcap.Stream.Default) -> enums.AntennaNr:
		"""SCPI: [SOURce<HW>]:BB:GNSS:STReam<ST>:ANTenna \n
		Snippet: value: enums.AntennaNr = driver.source.bb.gnss.stream.antenna.get(stream = repcap.Stream.Default) \n
		Selects the signal of which antenna is carried by which stream. \n
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:return: antenna: A1| A2| A3| A4"""
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:STReam{stream_cmd_val}:ANTenna?')
		return Conversions.str_to_scalar_enum(response, enums.AntennaNr)
