from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class H32Qam:
	"""H32Qam commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("h32Qam", core, parent)

	# noinspection PyTypeChecker
	def get_format_py(self) -> enums.GsmModType32Qam:
		"""SCPI: [SOURce<HW>]:BB:GSM:H32Qam:FORMat \n
		Snippet: value: enums.GsmModType32Qam = driver.source.bb.gsm.h32Qam.get_format_py() \n
		The command queries the modulation type. \n
			:return: format_py: QAM32EDge
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:H32Qam:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.GsmModType32Qam)
