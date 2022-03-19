from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FecFrame:
	"""FecFrame commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fecFrame", core, parent)

	def set(self, fec_frame: enums.Dvbs2CodingFecFrame, timeSlice=repcap.TimeSlice.Default, inputStream=repcap.InputStream.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:TSL<ST>:IS<CH>:FECFrame \n
		Snippet: driver.source.bb.dvbs2.tsl.isPy.fecFrame.set(fec_frame = enums.Dvbs2CodingFecFrame.MEDium, timeSlice = repcap.TimeSlice.Default, inputStream = repcap.InputStream.Default) \n
		Sets the length of the FEC frames. \n
			:param fec_frame: SHORt| NORMal| MEDium
			:param timeSlice: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tsl')
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
		"""
		param = Conversions.enum_scalar_to_str(fec_frame, enums.Dvbs2CodingFecFrame)
		timeSlice_cmd_val = self._cmd_group.get_repcap_cmd_value(timeSlice, repcap.TimeSlice)
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:TSL{timeSlice_cmd_val}:IS{inputStream_cmd_val}:FECFrame {param}')

	# noinspection PyTypeChecker
	def get(self, timeSlice=repcap.TimeSlice.Default, inputStream=repcap.InputStream.Default) -> enums.Dvbs2CodingFecFrame:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:TSL<ST>:IS<CH>:FECFrame \n
		Snippet: value: enums.Dvbs2CodingFecFrame = driver.source.bb.dvbs2.tsl.isPy.fecFrame.get(timeSlice = repcap.TimeSlice.Default, inputStream = repcap.InputStream.Default) \n
		Sets the length of the FEC frames. \n
			:param timeSlice: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tsl')
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
			:return: fec_frame: SHORt| NORMal| MEDium"""
		timeSlice_cmd_val = self._cmd_group.get_repcap_cmd_value(timeSlice, repcap.TimeSlice)
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVBS2:TSL{timeSlice_cmd_val}:IS{inputStream_cmd_val}:FECFrame?')
		return Conversions.str_to_scalar_enum(response, enums.Dvbs2CodingFecFrame)
