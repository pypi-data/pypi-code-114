from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tx:
	"""Tx commands group definition. 6 total commands, 2 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tx", core, parent)

	@property
	def antenna(self):
		"""antenna commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_antenna'):
			from .Antenna import Antenna
			self._antenna = Antenna(self._core, self._cmd_group)
		return self._antenna

	@property
	def coordinates(self):
		"""coordinates commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_coordinates'):
			from .Coordinates import Coordinates
			self._coordinates = Coordinates(self._core, self._cmd_group)
		return self._coordinates

	def get_heading(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SHIPtoship:TX:HEADing \n
		Snippet: value: float = driver.source.fsimulator.dsSimulation.shiptoship.tx.get_heading() \n
		No command help available \n
			:return: heading: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:SHIPtoship:TX:HEADing?')
		return Conversions.str_to_float(response)

	def set_heading(self, heading: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SHIPtoship:TX:HEADing \n
		Snippet: driver.source.fsimulator.dsSimulation.shiptoship.tx.set_heading(heading = 1.0) \n
		No command help available \n
			:param heading: No help available
		"""
		param = Conversions.decimal_value_to_str(heading)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:SHIPtoship:TX:HEADing {param}')

	def get_speed(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SHIPtoship:TX:SPEed \n
		Snippet: value: float = driver.source.fsimulator.dsSimulation.shiptoship.tx.get_speed() \n
		No command help available \n
			:return: speed: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:SHIPtoship:TX:SPEed?')
		return Conversions.str_to_float(response)

	def set_speed(self, speed: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SHIPtoship:TX:SPEed \n
		Snippet: driver.source.fsimulator.dsSimulation.shiptoship.tx.set_speed(speed = 1.0) \n
		No command help available \n
			:param speed: No help available
		"""
		param = Conversions.decimal_value_to_str(speed)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:SHIPtoship:TX:SPEed {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.FadDssVehTypeShip:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SHIPtoship:TX:TYPE \n
		Snippet: value: enums.FadDssVehTypeShip = driver.source.fsimulator.dsSimulation.shiptoship.tx.get_type_py() \n
		No command help available \n
			:return: ship_type: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:DSSimulation:SHIPtoship:TX:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.FadDssVehTypeShip)

	def set_type_py(self, ship_type: enums.FadDssVehTypeShip) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:DSSimulation:SHIPtoship:TX:TYPE \n
		Snippet: driver.source.fsimulator.dsSimulation.shiptoship.tx.set_type_py(ship_type = enums.FadDssVehTypeShip.SCARrier) \n
		No command help available \n
			:param ship_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(ship_type, enums.FadDssVehTypeShip)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:DSSimulation:SHIPtoship:TX:TYPE {param}')

	def clone(self) -> 'Tx':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tx(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
