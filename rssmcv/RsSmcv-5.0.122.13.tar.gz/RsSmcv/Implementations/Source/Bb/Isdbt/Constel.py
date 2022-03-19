from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Constel:
	"""Constel commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("constel", core, parent)

	# noinspection PyTypeChecker
	def get_a(self) -> enums.CodingIsdbtCodingConstel:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:CONStel:A \n
		Snippet: value: enums.CodingIsdbtCodingConstel = driver.source.bb.isdbt.constel.get_a() \n
		Defines the constellation. \n
			:return: constel_a: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:CONStel:A?')
		return Conversions.str_to_scalar_enum(response, enums.CodingIsdbtCodingConstel)

	def set_a(self, constel_a: enums.CodingIsdbtCodingConstel) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:CONStel:A \n
		Snippet: driver.source.bb.isdbt.constel.set_a(constel_a = enums.CodingIsdbtCodingConstel.C_16QAM) \n
		Defines the constellation. \n
			:param constel_a: C_DQPSK| C_QPSK| C_16QAM| C_64QAM
		"""
		param = Conversions.enum_scalar_to_str(constel_a, enums.CodingIsdbtCodingConstel)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:CONStel:A {param}')

	# noinspection PyTypeChecker
	def get_b(self) -> enums.CodingIsdbtCodingConstel:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:CONStel:B \n
		Snippet: value: enums.CodingIsdbtCodingConstel = driver.source.bb.isdbt.constel.get_b() \n
		Defines the constellation. \n
			:return: constel_b: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:CONStel:B?')
		return Conversions.str_to_scalar_enum(response, enums.CodingIsdbtCodingConstel)

	def set_b(self, constel_b: enums.CodingIsdbtCodingConstel) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:CONStel:B \n
		Snippet: driver.source.bb.isdbt.constel.set_b(constel_b = enums.CodingIsdbtCodingConstel.C_16QAM) \n
		Defines the constellation. \n
			:param constel_b: C_DQPSK| C_QPSK| C_16QAM| C_64QAM
		"""
		param = Conversions.enum_scalar_to_str(constel_b, enums.CodingIsdbtCodingConstel)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:CONStel:B {param}')

	# noinspection PyTypeChecker
	def get_c(self) -> enums.CodingIsdbtCodingConstel:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:CONStel:C \n
		Snippet: value: enums.CodingIsdbtCodingConstel = driver.source.bb.isdbt.constel.get_c() \n
		Defines the constellation. \n
			:return: constel_c: C_DQPSK| C_QPSK| C_16QAM| C_64QAM
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:CONStel:C?')
		return Conversions.str_to_scalar_enum(response, enums.CodingIsdbtCodingConstel)

	def set_c(self, constel_c: enums.CodingIsdbtCodingConstel) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:CONStel:C \n
		Snippet: driver.source.bb.isdbt.constel.set_c(constel_c = enums.CodingIsdbtCodingConstel.C_16QAM) \n
		Defines the constellation. \n
			:param constel_c: C_DQPSK| C_QPSK| C_16QAM| C_64QAM
		"""
		param = Conversions.enum_scalar_to_str(constel_c, enums.CodingIsdbtCodingConstel)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:CONStel:C {param}')
