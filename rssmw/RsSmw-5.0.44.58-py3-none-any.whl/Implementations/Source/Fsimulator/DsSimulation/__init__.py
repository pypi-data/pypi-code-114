from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DsSimulation:
	"""DsSimulation commands group definition. 84 total commands, 4 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dsSimulation", core, parent)

	@property
	def create(self):
		"""create commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_create'):
			from .Create import Create
			self._create = Create(self._core, self._cmd_group)
		return self._create

	@property
	def shiptoship(self):
		"""shiptoship commands group. 3 Sub-classes, 4 commands."""
		if not hasattr(self, '_shiptoship'):
			from .Shiptoship import Shiptoship
			self._shiptoship = Shiptoship(self._core, self._cmd_group)
		return self._shiptoship

	@property
	def towerToAir(self):
		"""towerToAir commands group. 7 Sub-classes, 4 commands."""
		if not hasattr(self, '_towerToAir'):
			from .TowerToAir import TowerToAir
			self._towerToAir = TowerToAir(self._core, self._cmd_group)
		return self._towerToAir

	@property
	def user(self):
		"""user commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_user'):
			from .User import User
			self._user = User(self._core, self._cmd_group)
		return self._user

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:CATalog \n
		Snippet: value: List[str] = driver.source.fsimulator.dsSimulation.get_catalog() \n
		No command help available \n
			:return: scenario_files: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:CATalog?')
		return Conversions.str_to_str_list(response)

	# noinspection PyTypeChecker
	def get_cformat(self) -> enums.FadDssRealAppr:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:CFORmat \n
		Snippet: value: enums.FadDssRealAppr = driver.source.fsimulator.dsSimulation.get_cformat() \n
		No command help available \n
			:return: coor_format: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:CFORmat?')
		return Conversions.str_to_scalar_enum(response, enums.FadDssRealAppr)

	def set_cformat(self, coor_format: enums.FadDssRealAppr) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:CFORmat \n
		Snippet: driver.source.fsimulator.dsSimulation.set_cformat(coor_format = enums.FadDssRealAppr.DECimal) \n
		No command help available \n
			:param coor_format: No help available
		"""
		param = Conversions.enum_scalar_to_str(coor_format, enums.FadDssRealAppr)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:CFORmat {param}')

	def get_load(self) -> str:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:LOAD \n
		Snippet: value: str = driver.source.fsimulator.dsSimulation.get_load() \n
		No command help available \n
			:return: scenario_file: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:LOAD?')
		return trim_str_response(response)

	def set_load(self, scenario_file: str) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:LOAD \n
		Snippet: driver.source.fsimulator.dsSimulation.set_load(scenario_file = '1') \n
		No command help available \n
			:param scenario_file: No help available
		"""
		param = Conversions.value_to_quoted_str(scenario_file)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:LOAD {param}')

	def get_save(self) -> str:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SAVE \n
		Snippet: value: str = driver.source.fsimulator.dsSimulation.get_save() \n
		No command help available \n
			:return: scenario_file: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:SAVE?')
		return trim_str_response(response)

	def set_save(self, scenario_file: str) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SAVE \n
		Snippet: driver.source.fsimulator.dsSimulation.set_save(scenario_file = '1') \n
		No command help available \n
			:param scenario_file: No help available
		"""
		param = Conversions.value_to_quoted_str(scenario_file)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:SAVE {param}')

	# noinspection PyTypeChecker
	def get_scenario(self) -> enums.FadDssScen:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SCENario \n
		Snippet: value: enums.FadDssScen = driver.source.fsimulator.dsSimulation.get_scenario() \n
		No command help available \n
			:return: scenario: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:SCENario?')
		return Conversions.str_to_scalar_enum(response, enums.FadDssScen)

	def set_scenario(self, scenario: enums.FadDssScen) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SCENario \n
		Snippet: driver.source.fsimulator.dsSimulation.set_scenario(scenario = enums.FadDssScen.SHIPtoship) \n
		No command help available \n
			:param scenario: No help available
		"""
		param = Conversions.enum_scalar_to_str(scenario, enums.FadDssScen)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:SCENario {param}')

	def clone(self) -> 'DsSimulation':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DsSimulation(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
