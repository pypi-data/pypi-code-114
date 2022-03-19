from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AudGen:
	"""AudGen commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("audGen", core, parent)

	def get_frq(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:RADio:AM:AUDGen:FRQ \n
		Snippet: value: float = driver.source.bb.radio.am.audGen.get_frq() \n
		Sets the frequency. \n
			:return: freq: float Range: 0.03 to 15, Unit: kHz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:AM:AUDGen:FRQ?')
		return Conversions.str_to_float(response)

	def set_frq(self, freq: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:AM:AUDGen:FRQ \n
		Snippet: driver.source.bb.radio.am.audGen.set_frq(freq = 1.0) \n
		Sets the frequency. \n
			:param freq: float Range: 0.03 to 15, Unit: kHz
		"""
		param = Conversions.decimal_value_to_str(freq)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:AM:AUDGen:FRQ {param}')

	def get_lev(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:RADio:AM:AUDGen:LEV \n
		Snippet: value: float = driver.source.bb.radio.am.audGen.get_lev() \n
		Sets the level. \n
			:return: level: float Range: -60 to 12, Unit: dBu
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:RADio:AM:AUDGen:LEV?')
		return Conversions.str_to_float(response)

	def set_lev(self, level: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:AM:AUDGen:LEV \n
		Snippet: driver.source.bb.radio.am.audGen.set_lev(level = 1.0) \n
		Sets the level. \n
			:param level: float Range: -60 to 12, Unit: dBu
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:AM:AUDGen:LEV {param}')
