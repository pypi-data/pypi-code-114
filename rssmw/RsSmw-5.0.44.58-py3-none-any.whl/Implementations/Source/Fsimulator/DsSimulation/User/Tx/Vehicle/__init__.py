from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Vehicle:
	"""Vehicle commands group definition. 5 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vehicle", core, parent)

	@property
	def predefined(self):
		"""predefined commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_predefined'):
			from .Predefined import Predefined
			self._predefined = Predefined(self._core, self._cmd_group)
		return self._predefined

	@property
	def user(self):
		"""user commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_user'):
			from .User import User
			self._user = User(self._core, self._cmd_group)
		return self._user

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.FadDssUsrVehMode:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:TX:VEHicle:MODE \n
		Snippet: value: enums.FadDssUsrVehMode = driver.source.fsimulator.dsSimulation.user.tx.vehicle.get_mode() \n
		No command help available \n
			:return: veh_mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:USER:TX:VEHicle:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FadDssUsrVehMode)

	def set_mode(self, veh_mode: enums.FadDssUsrVehMode) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:USER:TX:VEHicle:MODE \n
		Snippet: driver.source.fsimulator.dsSimulation.user.tx.vehicle.set_mode(veh_mode = enums.FadDssUsrVehMode.NONE) \n
		No command help available \n
			:param veh_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(veh_mode, enums.FadDssUsrVehMode)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:USER:TX:VEHicle:MODE {param}')

	def clone(self) -> 'Vehicle':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Vehicle(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
