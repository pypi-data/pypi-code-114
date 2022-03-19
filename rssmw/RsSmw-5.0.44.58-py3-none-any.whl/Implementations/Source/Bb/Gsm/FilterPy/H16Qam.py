from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class H16Qam:
	"""H16Qam commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("h16Qam", core, parent)

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.GilterHigh:
		"""SCPI: [SOURce<HW>]:BB:GSM:FILTer:H16Qam:TYPE \n
		Snippet: value: enums.GilterHigh = driver.source.bb.gsm.filterPy.h16Qam.get_type_py() \n
		Sets the filter for HSR 16QAM signal. \n
			:return: type_py: ENPShape| EWPShape
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:FILTer:H16Qam:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.GilterHigh)

	def set_type_py(self, type_py: enums.GilterHigh) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:FILTer:H16Qam:TYPE \n
		Snippet: driver.source.bb.gsm.filterPy.h16Qam.set_type_py(type_py = enums.GilterHigh.ENPShape) \n
		Sets the filter for HSR 16QAM signal. \n
			:param type_py: ENPShape| EWPShape
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.GilterHigh)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:FILTer:H16Qam:TYPE {param}')
