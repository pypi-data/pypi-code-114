from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, numb_of_basebands: enums.NumbOfBasebands, stream=repcap.Stream.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:STReam<ST>:BB:COUNt \n
		Snippet: driver.source.bb.gnss.stream.bb.count.set(numb_of_basebands = enums.NumbOfBasebands._0, stream = repcap.Stream.Default) \n
		Sets the number of basebands used for the GNSS stream. \n
			:param numb_of_basebands: 0| 1| 2| 3| 4
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
		"""
		param = Conversions.enum_scalar_to_str(numb_of_basebands, enums.NumbOfBasebands)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:STReam{stream_cmd_val}:BB:COUNt {param}')

	# noinspection PyTypeChecker
	def get(self, stream=repcap.Stream.Default) -> enums.NumbOfBasebands:
		"""SCPI: [SOURce<HW>]:BB:GNSS:STReam<ST>:BB:COUNt \n
		Snippet: value: enums.NumbOfBasebands = driver.source.bb.gnss.stream.bb.count.get(stream = repcap.Stream.Default) \n
		Sets the number of basebands used for the GNSS stream. \n
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:return: numb_of_basebands: 0| 1| 2| 3| 4"""
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:STReam{stream_cmd_val}:BB:COUNt?')
		return Conversions.str_to_scalar_enum(response, enums.NumbOfBasebands)
