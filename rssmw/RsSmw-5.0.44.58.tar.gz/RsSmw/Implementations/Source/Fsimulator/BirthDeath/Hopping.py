from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hopping:
	"""Hopping commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hopping", core, parent)

	def get_dwell(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:BIRThdeath:HOPPing:DWELl \n
		Snippet: value: float = driver.source.fsimulator.birthDeath.hopping.get_dwell() \n
		Sets the time until the next change in the delay of a path (birth death event) . \n
			:return: dwell: float Range: 1E-3 to 429.49672950
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:BIRThdeath:HOPPing:DWELl?')
		return Conversions.str_to_float(response)

	def set_dwell(self, dwell: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:BIRThdeath:HOPPing:DWELl \n
		Snippet: driver.source.fsimulator.birthDeath.hopping.set_dwell(dwell = 1.0) \n
		Sets the time until the next change in the delay of a path (birth death event) . \n
			:param dwell: float Range: 1E-3 to 429.49672950
		"""
		param = Conversions.decimal_value_to_str(dwell)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:BIRThdeath:HOPPing:DWELl {param}')
