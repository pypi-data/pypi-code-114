from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tsn:
	"""Tsn commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsn", core, parent)

	def set(self, tsn: float, timeSlice=repcap.TimeSlice.Default, inputStream=repcap.InputStream.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:TSL<ST>:IS<CH>:TSN \n
		Snippet: driver.source.bb.dvbs2.tsl.isPy.tsn.set(tsn = 1.0, timeSlice = repcap.TimeSlice.Default, inputStream = repcap.InputStream.Default) \n
		Sets the time slice number (TSN) or the input stream identifier (ISI) in hexadecimal representation. This number is used
		for identification. Each time slice uses a unique TSN. \n
			:param tsn: float
			:param timeSlice: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tsl')
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
		"""
		param = Conversions.decimal_value_to_str(tsn)
		timeSlice_cmd_val = self._cmd_group.get_repcap_cmd_value(timeSlice, repcap.TimeSlice)
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:TSL{timeSlice_cmd_val}:IS{inputStream_cmd_val}:TSN {param}')

	def get(self, timeSlice=repcap.TimeSlice.Default, inputStream=repcap.InputStream.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:TSL<ST>:IS<CH>:TSN \n
		Snippet: value: float = driver.source.bb.dvbs2.tsl.isPy.tsn.get(timeSlice = repcap.TimeSlice.Default, inputStream = repcap.InputStream.Default) \n
		Sets the time slice number (TSN) or the input stream identifier (ISI) in hexadecimal representation. This number is used
		for identification. Each time slice uses a unique TSN. \n
			:param timeSlice: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tsl')
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
			:return: tsn: float"""
		timeSlice_cmd_val = self._cmd_group.get_repcap_cmd_value(timeSlice, repcap.TimeSlice)
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVBS2:TSL{timeSlice_cmd_val}:IS{inputStream_cmd_val}:TSN?')
		return Conversions.str_to_float(response)
