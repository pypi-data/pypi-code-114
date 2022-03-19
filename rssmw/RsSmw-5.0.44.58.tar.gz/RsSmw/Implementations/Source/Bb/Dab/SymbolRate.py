from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def get_variation(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DAB:SRATe:VARiation \n
		Snippet: value: float = driver.source.bb.dab.symbolRate.get_variation() \n
		No command help available \n
			:return: variation: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DAB:SRATe:VARiation?')
		return Conversions.str_to_float(response)

	def set_variation(self, variation: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:DAB:SRATe:VARiation \n
		Snippet: driver.source.bb.dab.symbolRate.set_variation(variation = 1.0) \n
		No command help available \n
			:param variation: No help available
		"""
		param = Conversions.decimal_value_to_str(variation)
		self._core.io.write(f'SOURce<HwInstance>:BB:DAB:SRATe:VARiation {param}')
