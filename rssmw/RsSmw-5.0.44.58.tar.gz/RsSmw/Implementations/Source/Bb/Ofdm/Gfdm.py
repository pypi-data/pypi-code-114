from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gfdm:
	"""Gfdm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gfdm", core, parent)

	def get_db_symbols(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:OFDM:GFDM:DBSYmbols \n
		Snippet: value: int = driver.source.bb.ofdm.gfdm.get_db_symbols() \n
		Sets data block size in terms of symbols per data block. \n
			:return: gfdm_db_symbols: integer Range: 1 to 50
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:GFDM:DBSYmbols?')
		return Conversions.str_to_int(response)

	def set_db_symbols(self, gfdm_db_symbols: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:GFDM:DBSYmbols \n
		Snippet: driver.source.bb.ofdm.gfdm.set_db_symbols(gfdm_db_symbols = 1) \n
		Sets data block size in terms of symbols per data block. \n
			:param gfdm_db_symbols: integer Range: 1 to 50
		"""
		param = Conversions.decimal_value_to_str(gfdm_db_symbols)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:GFDM:DBSYmbols {param}')
