from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class G13A:
	"""G13A commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("g13A", core, parent)

	def get_block_2(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:OPF:G13A:BLOCk2 \n
		Snippet: value: int = driver.source.bb.radio.fm.rds.opf.g13A.get_block_2() \n
		Sets block 4 of the open format group types A. \n
			:return: ofg_1_ablk_2: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:OPF:G13A:BLOCk2?')
		return Conversions.str_to_int(response)

	def set_block_2(self, ofg_1_ablk_2: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:OPF:G13A:BLOCk2 \n
		Snippet: driver.source.bb.radio.fm.rds.opf.g13A.set_block_2(ofg_1_ablk_2 = 1) \n
		Sets block 4 of the open format group types A. \n
			:param ofg_1_ablk_2: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(ofg_1_ablk_2)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:OPF:G13A:BLOCk2 {param}')

	def get_block_3(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:OPF:G13A:BLOCk3 \n
		Snippet: value: int = driver.source.bb.radio.fm.rds.opf.g13A.get_block_3() \n
		Sets block 4 of the open format group types A. \n
			:return: open_format_blk_3: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:OPF:G13A:BLOCk3?')
		return Conversions.str_to_int(response)

	def set_block_3(self, open_format_blk_3: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:OPF:G13A:BLOCk3 \n
		Snippet: driver.source.bb.radio.fm.rds.opf.g13A.set_block_3(open_format_blk_3 = 1) \n
		Sets block 4 of the open format group types A. \n
			:param open_format_blk_3: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(open_format_blk_3)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:OPF:G13A:BLOCk3 {param}')

	def get_block_4(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:OPF:G13A:BLOCk4 \n
		Snippet: value: int = driver.source.bb.radio.fm.rds.opf.g13A.get_block_4() \n
		Sets block 4 of the open format group types A. \n
			:return: open_format_blk_4: integer Range: 0 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:FM:RDS:OPF:G13A:BLOCk4?')
		return Conversions.str_to_int(response)

	def set_block_4(self, open_format_blk_4: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:OPF:G13A:BLOCk4 \n
		Snippet: driver.source.bb.radio.fm.rds.opf.g13A.set_block_4(open_format_blk_4 = 1) \n
		Sets block 4 of the open format group types A. \n
			:param open_format_blk_4: integer Range: 0 to 65535
		"""
		param = Conversions.decimal_value_to_str(open_format_blk_4)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:OPF:G13A:BLOCk4 {param}')
