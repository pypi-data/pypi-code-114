from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spacing:
	"""Spacing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spacing", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.Spacing:
		"""SCPI: [SOURce<HW>]:SWEep:POWer:SPACing:MODE \n
		Snippet: value: enums.Spacing = driver.source.sweep.power.spacing.get_mode() \n
		Queries the level sweep spacing. The sweep spacing for level sweeps is always linear. \n
			:return: mode: LINear
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:SWEep:POWer:SPACing:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.Spacing)
