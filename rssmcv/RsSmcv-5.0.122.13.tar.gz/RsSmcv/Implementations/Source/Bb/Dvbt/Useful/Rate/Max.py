from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Max:
	"""Max commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("max", core, parent)

	def get_low(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVBT:USEFul:[RATE]:MAX:LOW \n
		Snippet: value: int = driver.source.bb.dvbt.useful.rate.max.get_low() \n
		Queries the maximum data rate, that is derived from the current modulation parameter settings. The value is the optimal
		value at the TS input interface, that is necessary for the modulator. \n
			:return: max_use_drlp: integer Range: 0 to 9999999999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:USEFul:RATE:MAX:LOW?')
		return Conversions.str_to_int(response)

	def get_high(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVBT:USEFul:[RATE]:MAX:[HIGH] \n
		Snippet: value: int = driver.source.bb.dvbt.useful.rate.max.get_high() \n
		Queries the maximum data rate, that is derived from the current modulation parameter settings. The value is the optimal
		value at the TS input interface, that is necessary for the modulator. \n
			:return: max_use_drhp: integer Range: 0 to 9999999999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:USEFul:RATE:MAX:HIGH?')
		return Conversions.str_to_int(response)
