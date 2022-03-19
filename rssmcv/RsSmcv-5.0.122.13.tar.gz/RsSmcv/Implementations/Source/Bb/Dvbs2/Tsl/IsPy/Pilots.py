from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pilots:
	"""Pilots commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pilots", core, parent)

	def set(self, pilots: bool, timeSlice=repcap.TimeSlice.Default, inputStream=repcap.InputStream.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:TSL<ST>:IS<CH>:PILots \n
		Snippet: driver.source.bb.dvbs2.tsl.isPy.pilots.set(pilots = False, timeSlice = repcap.TimeSlice.Default, inputStream = repcap.InputStream.Default) \n
		Controls the insertion of pilot symbols during the formation of the physical layer frame. Pilot symbols generate an
		unmodulated carrier and are helpful for synchronizing receivers under difficult transmission conditions. \n
			:param pilots: 1| ON| 0| OFF
			:param timeSlice: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tsl')
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
		"""
		param = Conversions.bool_to_str(pilots)
		timeSlice_cmd_val = self._cmd_group.get_repcap_cmd_value(timeSlice, repcap.TimeSlice)
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:TSL{timeSlice_cmd_val}:IS{inputStream_cmd_val}:PILots {param}')

	def get(self, timeSlice=repcap.TimeSlice.Default, inputStream=repcap.InputStream.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:TSL<ST>:IS<CH>:PILots \n
		Snippet: value: bool = driver.source.bb.dvbs2.tsl.isPy.pilots.get(timeSlice = repcap.TimeSlice.Default, inputStream = repcap.InputStream.Default) \n
		Controls the insertion of pilot symbols during the formation of the physical layer frame. Pilot symbols generate an
		unmodulated carrier and are helpful for synchronizing receivers under difficult transmission conditions. \n
			:param timeSlice: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tsl')
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
			:return: pilots: 1| ON| 0| OFF"""
		timeSlice_cmd_val = self._cmd_group.get_repcap_cmd_value(timeSlice, repcap.TimeSlice)
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVBS2:TSL{timeSlice_cmd_val}:IS{inputStream_cmd_val}:PILots?')
		return Conversions.str_to_bool(response)
