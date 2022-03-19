from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bandwidth:
	"""Bandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	def get_variation(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:BANDwidth:VARiation \n
		Snippet: value: int = driver.source.bb.t2Dvb.bandwidth.get_variation() \n
		Changes the used bandwidth in the range of ±1000 ppm. \n
			:return: bandwidth_var: integer Range: -1000 to 1000, Unit: ppm
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:BANDwidth:VARiation?')
		return Conversions.str_to_int(response)

	def set_variation(self, bandwidth_var: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:BANDwidth:VARiation \n
		Snippet: driver.source.bb.t2Dvb.bandwidth.set_variation(bandwidth_var = 1) \n
		Changes the used bandwidth in the range of ±1000 ppm. \n
			:param bandwidth_var: integer Range: -1000 to 1000, Unit: ppm
		"""
		param = Conversions.decimal_value_to_str(bandwidth_var)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:BANDwidth:VARiation {param}')
