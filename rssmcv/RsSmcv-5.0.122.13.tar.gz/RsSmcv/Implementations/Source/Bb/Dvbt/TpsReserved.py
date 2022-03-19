from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TpsReserved:
	"""TpsReserved commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tpsReserved", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBT:TPSReserved:STATE \n
		Snippet: value: bool = driver.source.bb.dvbt.tpsReserved.get_state() \n
		Enables or disables the reserved TPS bits. \n
			:return: tps_reserved: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:TPSReserved:STATE?')
		return Conversions.str_to_bool(response)

	def set_state(self, tps_reserved: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:TPSReserved:STATE \n
		Snippet: driver.source.bb.dvbt.tpsReserved.set_state(tps_reserved = False) \n
		Enables or disables the reserved TPS bits. \n
			:param tps_reserved: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(tps_reserved)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:TPSReserved:STATE {param}')

	def get_value(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVBT:TPSReserved:VALue \n
		Snippet: value: int = driver.source.bb.dvbt.tpsReserved.get_value() \n
		Sets the reserved bits in one-digit hexadecimal format. \n
			:return: reserved_bits: integer Range: #H0 to #HF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:TPSReserved:VALue?')
		return Conversions.str_to_int(response)

	def set_value(self, reserved_bits: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:TPSReserved:VALue \n
		Snippet: driver.source.bb.dvbt.tpsReserved.set_value(reserved_bits = 1) \n
		Sets the reserved bits in one-digit hexadecimal format. \n
			:param reserved_bits: integer Range: #H0 to #HF
		"""
		param = Conversions.decimal_value_to_str(reserved_bits)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:TPSReserved:VALue {param}')
