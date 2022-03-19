from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TowerToAir:
	"""TowerToAir commands group definition. 21 total commands, 7 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("towerToAir", core, parent)

	@property
	def altitude(self):
		"""altitude commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_altitude'):
			from .Altitude import Altitude
			self._altitude = Altitude(self._core, self._cmd_group)
		return self._altitude

	@property
	def angle(self):
		"""angle commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_angle'):
			from .Angle import Angle
			self._angle = Angle(self._core, self._cmd_group)
		return self._angle

	@property
	def flength(self):
		"""flength commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_flength'):
			from .Flength import Flength
			self._flength = Flength(self._core, self._cmd_group)
		return self._flength

	@property
	def radius(self):
		"""radius commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_radius'):
			from .Radius import Radius
			self._radius = Radius(self._core, self._cmd_group)
		return self._radius

	@property
	def rate(self):
		"""rate commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rate'):
			from .Rate import Rate
			self._rate = Rate(self._core, self._cmd_group)
		return self._rate

	@property
	def speed(self):
		"""speed commands group. 0 Sub-classes, 6 commands."""
		if not hasattr(self, '_speed'):
			from .Speed import Speed
			self._speed = Speed(self._core, self._cmd_group)
		return self._speed

	@property
	def trip(self):
		"""trip commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_trip'):
			from .Trip import Trip
			self._trip = Trip(self._core, self._cmd_group)
		return self._trip

	def get_cacceleration(self) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:CACCeleration \n
		Snippet: value: bool = driver.source.fsimulator.dsSimulation.towerToAir.get_cacceleration() \n
		No command help available \n
			:return: const_acceleration: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:CACCeleration?')
		return Conversions.str_to_bool(response)

	def set_cacceleration(self, const_acceleration: bool) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:CACCeleration \n
		Snippet: driver.source.fsimulator.dsSimulation.towerToAir.set_cacceleration(const_acceleration = False) \n
		No command help available \n
			:param const_acceleration: No help available
		"""
		param = Conversions.bool_to_str(const_acceleration)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:CACCeleration {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:PRESet \n
		Snippet: driver.source.fsimulator.dsSimulation.towerToAir.preset() \n
		No command help available \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:PRESet \n
		Snippet: driver.source.fsimulator.dsSimulation.towerToAir.preset_with_opc() \n
		No command help available \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:PRESet', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_terrain(self) -> enums.FadDssTerrType:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:TERRain \n
		Snippet: value: enums.FadDssTerrType = driver.source.fsimulator.dsSimulation.towerToAir.get_terrain() \n
		No command help available \n
			:return: terrain_type: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:TERRain?')
		return Conversions.str_to_scalar_enum(response, enums.FadDssTerrType)

	def set_terrain(self, terrain_type: enums.FadDssTerrType) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:TERRain \n
		Snippet: driver.source.fsimulator.dsSimulation.towerToAir.set_terrain(terrain_type = enums.FadDssTerrType.FORest) \n
		No command help available \n
			:param terrain_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(terrain_type, enums.FadDssTerrType)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:TERRain {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.FadDssVehTypeAir:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:TYPE \n
		Snippet: value: enums.FadDssVehTypeAir = driver.source.fsimulator.dsSimulation.towerToAir.get_type_py() \n
		No command help available \n
			:return: air_vehicle_type: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.FadDssVehTypeAir)

	def set_type_py(self, air_vehicle_type: enums.FadDssVehTypeAir) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:TOWertoair:TYPE \n
		Snippet: driver.source.fsimulator.dsSimulation.towerToAir.set_type_py(air_vehicle_type = enums.FadDssVehTypeAir.AHELicopter) \n
		No command help available \n
			:param air_vehicle_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(air_vehicle_type, enums.FadDssVehTypeAir)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:TOWertoair:TYPE {param}')

	def clone(self) -> 'TowerToAir':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TowerToAir(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
