from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Is2:
	"""Is2 commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("is2", core, parent)

	# noinspection PyTypeChecker
	def get_if_type(self) -> enums.InterfererTypeCw:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS2:IFTYpe \n
		Snippet: value: enums.InterfererTypeCw = driver.source.bb.nr5G.tcw.is2.get_if_type() \n
		Selects the type of the interfering signal. The second interfering signal is always a CW signal. \n
			:return: interferer_type_2: CW
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:IS2:IFTYpe?')
		return Conversions.str_to_scalar_enum(response, enums.InterfererTypeCw)

	def get_plevel(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS2:PLEVel \n
		Snippet: value: float = driver.source.bb.nr5G.tcw.is2.get_plevel() \n
		Queries the power level of the interfering signal. \n
			:return: is_2_powel_level: float Range: -145 to 20, Unit: dBm
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:IS2:PLEVel?')
		return Conversions.str_to_float(response)

	def get_rf_frequency(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:IS2:RFFRequency \n
		Snippet: value: int = driver.source.bb.nr5G.tcw.is2.get_rf_frequency() \n
		Queries the center frequency of the interfering signal 1 and 2. \n
			:return: is_2_rf_frequency: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:IS2:RFFRequency?')
		return Conversions.str_to_int(response)
