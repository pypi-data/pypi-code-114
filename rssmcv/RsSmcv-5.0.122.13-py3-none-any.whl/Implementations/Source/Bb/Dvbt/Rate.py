from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rate:
	"""Rate commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rate", core, parent)

	# noinspection PyTypeChecker
	def get_low(self) -> enums.CodingCoderate:
		"""SCPI: [SOURce<HW>]:BB:DVBT:RATE:LOW \n
		Snippet: value: enums.CodingCoderate = driver.source.bb.dvbt.rate.get_low() \n
		Sets the code rate. \n
			:return: coderate_lp: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:RATE:LOW?')
		return Conversions.str_to_scalar_enum(response, enums.CodingCoderate)

	def set_low(self, coderate_lp: enums.CodingCoderate) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:RATE:LOW \n
		Snippet: driver.source.bb.dvbt.rate.set_low(coderate_lp = enums.CodingCoderate.R1_2) \n
		Sets the code rate. \n
			:param coderate_lp: R1_2| R2_3| R3_4| R5_6| R7_8
		"""
		param = Conversions.enum_scalar_to_str(coderate_lp, enums.CodingCoderate)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:RATE:LOW {param}')

	# noinspection PyTypeChecker
	def get_high(self) -> enums.CodingCoderate:
		"""SCPI: [SOURce<HW>]:BB:DVBT:RATE:[HIGH] \n
		Snippet: value: enums.CodingCoderate = driver.source.bb.dvbt.rate.get_high() \n
		Sets the code rate. \n
			:return: coderate_hp: R1_2| R2_3| R3_4| R5_6| R7_8
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:RATE:HIGH?')
		return Conversions.str_to_scalar_enum(response, enums.CodingCoderate)

	def set_high(self, coderate_hp: enums.CodingCoderate) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:RATE:[HIGH] \n
		Snippet: driver.source.bb.dvbt.rate.set_high(coderate_hp = enums.CodingCoderate.R1_2) \n
		Sets the code rate. \n
			:param coderate_hp: R1_2| R2_3| R3_4| R5_6| R7_8
		"""
		param = Conversions.enum_scalar_to_str(coderate_hp, enums.CodingCoderate)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:RATE:HIGH {param}')
