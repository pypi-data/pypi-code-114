from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tpa:
	"""Tpa commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tpa", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:TPA:CATalog \n
		Snippet: value: List[str] = driver.source.fsimulator.dsSimulation.user.tpa.get_catalog() \n
		No command help available \n
			:return: filenames: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:USER:TPA:CATalog?')
		return Conversions.str_to_str_list(response)

	def get_select(self) -> str:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:TPA:SELect \n
		Snippet: value: str = driver.source.fsimulator.dsSimulation.user.tpa.get_select() \n
		No command help available \n
			:return: traj_tpa_select: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:USER:TPA:SELect?')
		return trim_str_response(response)

	def set_select(self, traj_tpa_select: str) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:TPA:SELect \n
		Snippet: driver.source.fsimulator.dsSimulation.user.tpa.set_select(traj_tpa_select = '1') \n
		No command help available \n
			:param traj_tpa_select: No help available
		"""
		param = Conversions.value_to_quoted_str(traj_tpa_select)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:USER:TPA:SELect {param}')
