from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fofdm:
	"""Fofdm commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fofdm", core, parent)

	def get_nsuband(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:OFDM:FOFDm:NSUBand \n
		Snippet: value: int = driver.source.bb.ofdm.fofdm.get_nsuband() \n
		Sets the number of f-OFDM sub-bands. \n
			:return: fofdm_nsubands: integer Range: 1 to 1500
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:FOFDm:NSUBand?')
		return Conversions.str_to_int(response)

	def set_nsuband(self, fofdm_nsubands: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:FOFDm:NSUBand \n
		Snippet: driver.source.bb.ofdm.fofdm.set_nsuband(fofdm_nsubands = 1) \n
		Sets the number of f-OFDM sub-bands. \n
			:param fofdm_nsubands: integer Range: 1 to 1500
		"""
		param = Conversions.decimal_value_to_str(fofdm_nsubands)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:FOFDm:NSUBand {param}')

	def get_ntx_blocks(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:OFDM:FOFDm:NTXBlocks \n
		Snippet: value: int = driver.source.bb.ofdm.fofdm.get_ntx_blocks() \n
		No command help available \n
			:return: fofdm_ntx_blocks: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:FOFDm:NTXBlocks?')
		return Conversions.str_to_int(response)

	def set_ntx_blocks(self, fofdm_ntx_blocks: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:FOFDm:NTXBlocks \n
		Snippet: driver.source.bb.ofdm.fofdm.set_ntx_blocks(fofdm_ntx_blocks = 1) \n
		No command help available \n
			:param fofdm_ntx_blocks: No help available
		"""
		param = Conversions.decimal_value_to_str(fofdm_ntx_blocks)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:FOFDm:NTXBlocks {param}')
