from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	# noinspection PyTypeChecker
	def get_amode(self) -> enums.PowerAttMode:
		"""SCPI: [SOURce<HW>]:LIST:POWer:AMODe \n
		Snippet: value: enums.PowerAttMode = driver.source.listPy.power.get_amode() \n
		No command help available \n
			:return: amode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LIST:POWer:AMODe?')
		return Conversions.str_to_scalar_enum(response, enums.PowerAttMode)

	def set_amode(self, amode: enums.PowerAttMode) -> None:
		"""SCPI: [SOURce<HW>]:LIST:POWer:AMODe \n
		Snippet: driver.source.listPy.power.set_amode(amode = enums.PowerAttMode.AUTO) \n
		No command help available \n
			:param amode: No help available
		"""
		param = Conversions.enum_scalar_to_str(amode, enums.PowerAttMode)
		self._core.io.write(f'SOURce<HwInstance>:LIST:POWer:AMODe {param}')

	def get_points(self) -> int:
		"""SCPI: [SOURce<HW>]:LIST:POWer:POINts \n
		Snippet: value: int = driver.source.listPy.power.get_points() \n
		Queries the number (points) of level entries in the selected list. \n
			:return: points: integer Range: 0 to INT_MAX
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:LIST:POWer:POINts?')
		return Conversions.str_to_int(response)

	def get_value(self) -> List[float]:
		"""SCPI: [SOURce<HW>]:LIST:POWer \n
		Snippet: value: List[float] = driver.source.listPy.power.get_value() \n
		Enters the level values in the selected list. The number of level values must correspond to the number of frequency
		values. Existing data is overwritten. \n
			:return: power: Power#1{, Power#2, ...} | block data You can either enter the data as a list of numbers, or as binary block data. The list of numbers can be of any length, with the list entries separated by commas. In binary block format, 8 (4) bytes are always interpreted as a floating-point number with double accuracy. See also method RsSmcv.FormatPy.data. Range: depends on the installed options , Unit: dBm
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce<HwInstance>:LIST:POWer?')
		return response

	def set_value(self, power: List[float]) -> None:
		"""SCPI: [SOURce<HW>]:LIST:POWer \n
		Snippet: driver.source.listPy.power.set_value(power = [1.1, 2.2, 3.3]) \n
		Enters the level values in the selected list. The number of level values must correspond to the number of frequency
		values. Existing data is overwritten. \n
			:param power: Power#1{, Power#2, ...} | block data You can either enter the data as a list of numbers, or as binary block data. The list of numbers can be of any length, with the list entries separated by commas. In binary block format, 8 (4) bytes are always interpreted as a floating-point number with double accuracy. See also method RsSmcv.FormatPy.data. Range: depends on the installed options , Unit: dBm
		"""
		param = Conversions.list_to_csv_str(power)
		self._core.io.write(f'SOURce<HwInstance>:LIST:POWer {param}')
