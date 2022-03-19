from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TsChannel:
	"""TsChannel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsChannel", core, parent)

	def set(self, ts_channel: enums.NumberA, inputStream=repcap.InputStream.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:INPut:[IS<CH>]:TSCHannel \n
		Snippet: driver.source.bb.dvbs2.inputPy.isPy.tsChannel.set(ts_channel = enums.NumberA._1, inputStream = repcap.InputStream.Default) \n
		Selects the IP-based transport stream (TS) channel. You can select 1 out of 4 IP TS channels as input at the 'IP Data'
		interface. To configure a particular channel, see 'IP channel x settings'. \n
			:param ts_channel: 1| 2| 3| 4
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
		"""
		param = Conversions.enum_scalar_to_str(ts_channel, enums.NumberA)
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:INPut:IS{inputStream_cmd_val}:TSCHannel {param}')

	# noinspection PyTypeChecker
	def get(self, inputStream=repcap.InputStream.Default) -> enums.NumberA:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:INPut:[IS<CH>]:TSCHannel \n
		Snippet: value: enums.NumberA = driver.source.bb.dvbs2.inputPy.isPy.tsChannel.get(inputStream = repcap.InputStream.Default) \n
		Selects the IP-based transport stream (TS) channel. You can select 1 out of 4 IP TS channels as input at the 'IP Data'
		interface. To configure a particular channel, see 'IP channel x settings'. \n
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
			:return: ts_channel: 1| 2| 3| 4"""
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVBS2:INPut:IS{inputStream_cmd_val}:TSCHannel?')
		return Conversions.str_to_scalar_enum(response, enums.NumberA)
