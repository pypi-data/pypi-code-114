from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Profile:
	"""Profile commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("profile", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:PROFile:CATalog \n
		Snippet: value: List[str] = driver.source.fsimulator.dsSimulation.user.profile.get_catalog() \n
		No command help available \n
			:return: filenames: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:USER:PROFile:CATalog?')
		return Conversions.str_to_str_list(response)

	def get_select(self) -> str:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:PROFile:SELect \n
		Snippet: value: str = driver.source.fsimulator.dsSimulation.user.profile.get_select() \n
		No command help available \n
			:return: prof_select: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:USER:PROFile:SELect?')
		return trim_str_response(response)

	def set_select(self, prof_select: str) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:PROFile:SELect \n
		Snippet: driver.source.fsimulator.dsSimulation.user.profile.set_select(prof_select = '1') \n
		No command help available \n
			:param prof_select: No help available
		"""
		param = Conversions.value_to_quoted_str(prof_select)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:USER:PROFile:SELect {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.FadDssUsrProfSour:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:PROFile:SOURce \n
		Snippet: value: enums.FadDssUsrProfSour = driver.source.fsimulator.dsSimulation.user.profile.get_source() \n
		No command help available \n
			:return: prof_source: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:USER:PROFile:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.FadDssUsrProfSour)

	def set_source(self, prof_source: enums.FadDssUsrProfSour) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:PROFile:SOURce \n
		Snippet: driver.source.fsimulator.dsSimulation.user.profile.set_source(prof_source = enums.FadDssUsrProfSour.PROFile) \n
		No command help available \n
			:param prof_source: No help available
		"""
		param = Conversions.enum_scalar_to_str(prof_source, enums.FadDssUsrProfSour)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:USER:PROFile:SOURce {param}')
