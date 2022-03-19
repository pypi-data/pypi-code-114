from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Display:
	"""Display commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("display", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.FadMimoPowDispMode:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:POWer:DISPlay:MODE \n
		Snippet: value: enums.FadMimoPowDispMode = driver.source.fsimulator.mimo.power.display.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MIMO:POWer:DISPlay:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FadMimoPowDispMode)

	def set_mode(self, mode: enums.FadMimoPowDispMode) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:POWer:DISPlay:MODE \n
		Snippet: driver.source.fsimulator.mimo.power.display.set_mode(mode = enums.FadMimoPowDispMode.ABSolute) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FadMimoPowDispMode)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:POWer:DISPlay:MODE {param}')
