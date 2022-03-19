from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Vehicle:
	"""Vehicle commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vehicle", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import Catalog
			self._catalog = Catalog(self._core, self._cmd_group)
		return self._catalog

	# noinspection PyTypeChecker
	def get_count(self) -> enums.Count:
		"""SCPI: [SOURce<HW>]:BB:GNSS:VEHicle:COUNt \n
		Snippet: value: enums.Count = driver.source.bb.gnss.vehicle.get_count() \n
		Sets the number of simulated vehicles. \n
			:return: number_of_vehicle: integer Range: 1 to 2
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:VEHicle:COUNt?')
		return Conversions.str_to_scalar_enum(response, enums.Count)

	def set_count(self, number_of_vehicle: enums.Count) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:VEHicle:COUNt \n
		Snippet: driver.source.bb.gnss.vehicle.set_count(number_of_vehicle = enums.Count._1) \n
		Sets the number of simulated vehicles. \n
			:param number_of_vehicle: integer Range: 1 to 2
		"""
		param = Conversions.enum_scalar_to_str(number_of_vehicle, enums.Count)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:VEHicle:COUNt {param}')

	def clone(self) -> 'Vehicle':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Vehicle(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
