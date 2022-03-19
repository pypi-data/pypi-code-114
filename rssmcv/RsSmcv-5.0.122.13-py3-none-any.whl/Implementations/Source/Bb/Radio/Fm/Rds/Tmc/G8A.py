from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class G8A:
	"""G8A commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("g8A", core, parent)

	def get_block_2(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:TMC:G8A:BLOCk2 \n
		Snippet: value: int = driver.source.bb.radio.fm.rds.tmc.g8A.get_block_2() \n
		No command help available \n
			:return: g_8_ab_lk_2: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:TMC:G8A:BLOCk2?')
		return Conversions.str_to_int(response)

	def set_block_2(self, g_8_ab_lk_2: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:TMC:G8A:BLOCk2 \n
		Snippet: driver.source.bb.radio.fm.rds.tmc.g8A.set_block_2(g_8_ab_lk_2 = 1) \n
		No command help available \n
			:param g_8_ab_lk_2: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(g_8_ab_lk_2)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:TMC:G8A:BLOCk2 {param}')

	def get_block_3_a(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:TMC:G8A:BLOCk3a \n
		Snippet: value: int = driver.source.bb.radio.fm.rds.tmc.g8A.get_block_3_a() \n
		No command help available \n
			:return: ga_8_blk_3: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:TMC:G8A:BLOCk3a?')
		return Conversions.str_to_int(response)

	def set_block_3_a(self, ga_8_blk_3: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:TMC:G8A:BLOCk3a \n
		Snippet: driver.source.bb.radio.fm.rds.tmc.g8A.set_block_3_a(ga_8_blk_3 = 1) \n
		No command help available \n
			:param ga_8_blk_3: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(ga_8_blk_3)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:TMC:G8A:BLOCk3a {param}')

	def get_block_4(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:TMC:G8A:BLOCk4 \n
		Snippet: value: int = driver.source.bb.radio.fm.rds.tmc.g8A.get_block_4() \n
		No command help available \n
			:return: g_8_ab_lk_4: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:TMC:G8A:BLOCk4?')
		return Conversions.str_to_int(response)

	def set_block_4(self, g_8_ab_lk_4: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:TMC:G8A:BLOCk4 \n
		Snippet: driver.source.bb.radio.fm.rds.tmc.g8A.set_block_4(g_8_ab_lk_4 = 1) \n
		No command help available \n
			:param g_8_ab_lk_4: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(g_8_ab_lk_4)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:TMC:G8A:BLOCk4 {param}')

	def get_number(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:TMC:G8A:NUMBer \n
		Snippet: value: int = driver.source.bb.radio.fm.rds.tmc.g8A.get_number() \n
		Defines the number of A8 groups. \n
			:return: g_8_ano: integer Range: 1 to 6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:TMC:G8A:NUMBer?')
		return Conversions.str_to_int(response)

	def set_number(self, g_8_ano: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:TMC:G8A:NUMBer \n
		Snippet: driver.source.bb.radio.fm.rds.tmc.g8A.set_number(g_8_ano = 1) \n
		Defines the number of A8 groups. \n
			:param g_8_ano: integer Range: 1 to 6
		"""
		param = Conversions.decimal_value_to_str(g_8_ano)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:TMC:G8A:NUMBer {param}')
