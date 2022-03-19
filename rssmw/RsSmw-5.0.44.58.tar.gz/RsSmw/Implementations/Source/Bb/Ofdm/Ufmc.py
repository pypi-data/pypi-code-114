from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ufmc:
	"""Ufmc commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ufmc", core, parent)

	def get_nsuband(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:OFDM:UFMC:NSUBand \n
		Snippet: value: int = driver.source.bb.ofdm.ufmc.get_nsuband() \n
		Sets the number of UFMC sub-bands. \n
			:return: nsubbands: integer Range: 1 to 1500
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:UFMC:NSUBand?')
		return Conversions.str_to_int(response)

	def set_nsuband(self, nsubbands: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:UFMC:NSUBand \n
		Snippet: driver.source.bb.ofdm.ufmc.set_nsuband(nsubbands = 1) \n
		Sets the number of UFMC sub-bands. \n
			:param nsubbands: integer Range: 1 to 1500
		"""
		param = Conversions.decimal_value_to_str(nsubbands)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:UFMC:NSUBand {param}')

	def get_pre_equal(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:OFDM:UFMC:PREequal \n
		Snippet: value: bool = driver.source.bb.ofdm.ufmc.get_pre_equal() \n
		Applies a filter pre-equalization. \n
			:return: ufmc_pre_equal: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:UFMC:PREequal?')
		return Conversions.str_to_bool(response)

	def set_pre_equal(self, ufmc_pre_equal: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:UFMC:PREequal \n
		Snippet: driver.source.bb.ofdm.ufmc.set_pre_equal(ufmc_pre_equal = False) \n
		Applies a filter pre-equalization. \n
			:param ufmc_pre_equal: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(ufmc_pre_equal)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:UFMC:PREequal {param}')
