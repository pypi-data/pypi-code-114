from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Isi:
	"""Isi commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("isi", core, parent)

	def set(self, isi: int, timeSlice=repcap.TimeSlice.Default, inputStream=repcap.InputStream.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:TSL<ST>:IS<CH>:ISI \n
		Snippet: driver.source.bb.dvbs2.tsl.isPy.isi.set(isi = 1, timeSlice = repcap.TimeSlice.Default, inputStream = repcap.InputStream.Default) \n
		Sets the input stream identifier (ISI) . \n
			:param isi: integer Range: 1 to 8
			:param timeSlice: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tsl')
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
		"""
		param = Conversions.decimal_value_to_str(isi)
		timeSlice_cmd_val = self._cmd_group.get_repcap_cmd_value(timeSlice, repcap.TimeSlice)
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:TSL{timeSlice_cmd_val}:IS{inputStream_cmd_val}:ISI {param}')

	def get(self, timeSlice=repcap.TimeSlice.Default, inputStream=repcap.InputStream.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:TSL<ST>:IS<CH>:ISI \n
		Snippet: value: int = driver.source.bb.dvbs2.tsl.isPy.isi.get(timeSlice = repcap.TimeSlice.Default, inputStream = repcap.InputStream.Default) \n
		Sets the input stream identifier (ISI) . \n
			:param timeSlice: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tsl')
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
			:return: isi: integer Range: 1 to 8"""
		timeSlice_cmd_val = self._cmd_group.get_repcap_cmd_value(timeSlice, repcap.TimeSlice)
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVBS2:TSL{timeSlice_cmd_val}:IS{inputStream_cmd_val}:ISI?')
		return Conversions.str_to_int(response)
