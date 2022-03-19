from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TpConfiguration:
	"""TpConfiguration commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tpConfiguration", core, parent)

	def get_tp_interval(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:DTTest:TPConfiguration:TPINterval \n
		Snippet: value: float = driver.source.bb.btooth.dtTest.tpConfiguration.get_tp_interval() \n
		Sets the time interval between two consecutive test packets, regarding the starting points. Command sets the values in ms.
		Query returns values in s. \n
			:return: tp_interval: float Range: 0.625E-3 s to 27.5E-3 s - depends on packet characteristics , Unit: ms
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:DTTest:TPConfiguration:TPINterval?')
		return Conversions.str_to_float(response)

	def set_tp_interval(self, tp_interval: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:DTTest:TPConfiguration:TPINterval \n
		Snippet: driver.source.bb.btooth.dtTest.tpConfiguration.set_tp_interval(tp_interval = 1.0) \n
		Sets the time interval between two consecutive test packets, regarding the starting points. Command sets the values in ms.
		Query returns values in s. \n
			:param tp_interval: float Range: 0.625E-3 s to 27.5E-3 s - depends on packet characteristics , Unit: ms
		"""
		param = Conversions.decimal_value_to_str(tp_interval)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:DTTest:TPConfiguration:TPINterval {param}')

	def get_up_length(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:DTTest:TPConfiguration:UPLength \n
		Snippet: value: int = driver.source.bb.btooth.dtTest.tpConfiguration.get_up_length() \n
		Sets the payload length. \n
			:return: up_length: integer Range: 0 to 255
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:DTTest:TPConfiguration:UPLength?')
		return Conversions.str_to_int(response)

	def set_up_length(self, up_length: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:DTTest:TPConfiguration:UPLength \n
		Snippet: driver.source.bb.btooth.dtTest.tpConfiguration.set_up_length(up_length = 1) \n
		Sets the payload length. \n
			:param up_length: integer Range: 0 to 255
		"""
		param = Conversions.decimal_value_to_str(up_length)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:DTTest:TPConfiguration:UPLength {param}')

	# noinspection PyTypeChecker
	def get_up_source(self) -> enums.BtoPyLdSour:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:DTTest:TPConfiguration:UPSource \n
		Snippet: value: enums.BtoPyLdSour = driver.source.bb.btooth.dtTest.tpConfiguration.get_up_source() \n
		Selects the data source used for the payload test packets. \n
			:return: up_source: PN09| PAT1| PAT2| PN15| PAT3| PAT4| PAT5| PAT6 PN9 / PN15 Pseudo-random bit sequences (PRBS) of a length of xx bits. The length in bit can be 9 or 15. PAT1 Predefined pattern: 11110000 PAT2 Predefined pattern: 10101010 PAT3 Predefined pattern: 11111111 PAT4 Predefined pattern: 00000000 PAT5 Predefined pattern: 00001111 PAT6 Predefined pattern: 01010101
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:DTTest:TPConfiguration:UPSource?')
		return Conversions.str_to_scalar_enum(response, enums.BtoPyLdSour)

	def set_up_source(self, up_source: enums.BtoPyLdSour) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:DTTest:TPConfiguration:UPSource \n
		Snippet: driver.source.bb.btooth.dtTest.tpConfiguration.set_up_source(up_source = enums.BtoPyLdSour.PAT1) \n
		Selects the data source used for the payload test packets. \n
			:param up_source: PN09| PAT1| PAT2| PN15| PAT3| PAT4| PAT5| PAT6 PN9 / PN15 Pseudo-random bit sequences (PRBS) of a length of xx bits. The length in bit can be 9 or 15. PAT1 Predefined pattern: 11110000 PAT2 Predefined pattern: 10101010 PAT3 Predefined pattern: 11111111 PAT4 Predefined pattern: 00000000 PAT5 Predefined pattern: 00001111 PAT6 Predefined pattern: 01010101
		"""
		param = Conversions.enum_scalar_to_str(up_source, enums.BtoPyLdSour)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:DTTest:TPConfiguration:UPSource {param}')
