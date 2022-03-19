from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pll:
	"""Pll commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pll", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.FreqPllModeA:
		"""SCPI: [SOURce<HW>]:FREQuency:PLL:MODE \n
		Snippet: value: enums.FreqPllModeA = driver.source.frequency.pll.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:PLL:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FreqPllModeA)

	def set_mode(self, mode: enums.FreqPllModeA) -> None:
		"""SCPI: [SOURce<HW>]:FREQuency:PLL:MODE \n
		Snippet: driver.source.frequency.pll.set_mode(mode = enums.FreqPllModeA.NARRow) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FreqPllModeA)
		self._core.io.write(f'SOURce<HwInstance>:FREQuency:PLL:MODE {param}')
