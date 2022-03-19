from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ReedSolomon:
	"""ReedSolomon commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reedSolomon", core, parent)

	def get_low(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBT:[SPECial]:REEDsolomon:LOW \n
		Snippet: value: bool = driver.source.bb.dvbt.special.reedSolomon.get_low() \n
		Enables/disables the Reed-Solomon encoder. \n
			:return: reed_solomon_low: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:SPECial:REEDsolomon:LOW?')
		return Conversions.str_to_bool(response)

	def set_low(self, reed_solomon_low: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:[SPECial]:REEDsolomon:LOW \n
		Snippet: driver.source.bb.dvbt.special.reedSolomon.set_low(reed_solomon_low = False) \n
		Enables/disables the Reed-Solomon encoder. \n
			:param reed_solomon_low: OFF| ON| 1| 0
		"""
		param = Conversions.bool_to_str(reed_solomon_low)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:SPECial:REEDsolomon:LOW {param}')

	def get_high(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DVBT:[SPECial]:REEDsolomon:[HIGH] \n
		Snippet: value: bool = driver.source.bb.dvbt.special.reedSolomon.get_high() \n
		Enables/disables the Reed-Solomon encoder. \n
			:return: reed_solomon_high: OFF| ON| 1| 0
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:SPECial:REEDsolomon:HIGH?')
		return Conversions.str_to_bool(response)

	def set_high(self, reed_solomon_high: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:[SPECial]:REEDsolomon:[HIGH] \n
		Snippet: driver.source.bb.dvbt.special.reedSolomon.set_high(reed_solomon_high = False) \n
		Enables/disables the Reed-Solomon encoder. \n
			:param reed_solomon_high: OFF| ON| 1| 0
		"""
		param = Conversions.bool_to_str(reed_solomon_high)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:SPECial:REEDsolomon:HIGH {param}')
