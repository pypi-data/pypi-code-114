from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModCod:
	"""ModCod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modCod", core, parent)

	def set(self, mod_cod: enums.Dvbs2CodingModCod, timeSlice=repcap.TimeSlice.Default, inputStream=repcap.InputStream.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:TSL<ST>:IS<CH>:MODCod \n
		Snippet: driver.source.bb.dvbs2.tsl.isPy.modCod.set(mod_cod = enums.Dvbs2CodingModCod._0, timeSlice = repcap.TimeSlice.Default, inputStream = repcap.InputStream.Default) \n
		Defines the modulation coding, a combined setting of constellation and code rate. \n
			:param mod_cod: 0| 1| 10| 100| 101| 102| 103| 104| 105| 106| 11| 12| 13| 14| 15| 16| 17| 18| 19| 2| 20| 21| 22| 23| 24| 25| 26| 27| 28| 29| 3| 30| 31| 32| 33| 34| 35| 36| 37| 38| 39| 4| 40| 41| 42| 43| 44| 45| 46| 47| 48| 49| 5| 50| 51| 52| 53| 54| 55| 56| 57| 58| 59| 6| 60| 61| 62| 63| 64| 65| 66| 67| 68| 69| 7| 70| 71| 72| 73| 74| 75| 76| 77| 78| 79| 8| 80| 81| 82| 83| 84| 85| 86| 87| 88| 89| 9| 90| 91| 92| 93| 94| 95| 96| 97| 98| 99
			:param timeSlice: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tsl')
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
		"""
		param = Conversions.enum_scalar_to_str(mod_cod, enums.Dvbs2CodingModCod)
		timeSlice_cmd_val = self._cmd_group.get_repcap_cmd_value(timeSlice, repcap.TimeSlice)
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBS2:TSL{timeSlice_cmd_val}:IS{inputStream_cmd_val}:MODCod {param}')

	# noinspection PyTypeChecker
	def get(self, timeSlice=repcap.TimeSlice.Default, inputStream=repcap.InputStream.Default) -> enums.Dvbs2CodingModCod:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:TSL<ST>:IS<CH>:MODCod \n
		Snippet: value: enums.Dvbs2CodingModCod = driver.source.bb.dvbs2.tsl.isPy.modCod.get(timeSlice = repcap.TimeSlice.Default, inputStream = repcap.InputStream.Default) \n
		Defines the modulation coding, a combined setting of constellation and code rate. \n
			:param timeSlice: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tsl')
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
			:return: mod_cod: 0| 1| 10| 100| 101| 102| 103| 104| 105| 106| 11| 12| 13| 14| 15| 16| 17| 18| 19| 2| 20| 21| 22| 23| 24| 25| 26| 27| 28| 29| 3| 30| 31| 32| 33| 34| 35| 36| 37| 38| 39| 4| 40| 41| 42| 43| 44| 45| 46| 47| 48| 49| 5| 50| 51| 52| 53| 54| 55| 56| 57| 58| 59| 6| 60| 61| 62| 63| 64| 65| 66| 67| 68| 69| 7| 70| 71| 72| 73| 74| 75| 76| 77| 78| 79| 8| 80| 81| 82| 83| 84| 85| 86| 87| 88| 89| 9| 90| 91| 92| 93| 94| 95| 96| 97| 98| 99"""
		timeSlice_cmd_val = self._cmd_group.get_repcap_cmd_value(timeSlice, repcap.TimeSlice)
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVBS2:TSL{timeSlice_cmd_val}:IS{inputStream_cmd_val}:MODCod?')
		return Conversions.str_to_scalar_enum(response, enums.Dvbs2CodingModCod)
