from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Crate:
	"""Crate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("crate", core, parent)

	def get_variation(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EVDO:CRATe:VARiation \n
		Snippet: value: float = driver.source.bb.evdo.crate.get_variation() \n
		Enters the output chip rate. The output chip rate changes the output clock and the modulation bandwidth, as well as the
		synchronization signals that are output. It does not affect the calculated chip sequence. \n
			:return: variation: float Range: 1 Mcps to 5 Mcps
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EVDO:CRATe:VARiation?')
		return Conversions.str_to_float(response)

	def set_variation(self, variation: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:CRATe:VARiation \n
		Snippet: driver.source.bb.evdo.crate.set_variation(variation = 1.0) \n
		Enters the output chip rate. The output chip rate changes the output clock and the modulation bandwidth, as well as the
		synchronization signals that are output. It does not affect the calculated chip sequence. \n
			:param variation: float Range: 1 Mcps to 5 Mcps
		"""
		param = Conversions.decimal_value_to_str(variation)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:CRATe:VARiation {param}')
