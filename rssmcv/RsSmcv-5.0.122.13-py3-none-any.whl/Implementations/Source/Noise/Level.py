from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def get_relative(self) -> float:
		"""SCPI: [SOURce<HW>]:NOISe:LEVel:RELative \n
		Snippet: value: float = driver.source.noise.level.get_relative() \n
		No command help available \n
			:return: relative: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:NOISe:LEVel:RELative?')
		return Conversions.str_to_float(response)
