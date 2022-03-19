from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Los:
	"""Los commands group definition. 12 total commands, 3 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("los", core, parent)

	@property
	def arrival(self):
		"""arrival commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_arrival'):
			from .Arrival import Arrival
			self._arrival = Arrival(self._core, self._cmd_group)
		return self._arrival

	@property
	def departure(self):
		"""departure commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_departure'):
			from .Departure import Departure
			self._departure = Departure(self._core, self._cmd_group)
		return self._departure

	@property
	def random(self):
		"""random commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_random'):
			from .Random import Random
			self._random = Random(self._core, self._cmd_group)
		return self._random

	def get_distance(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:LOS:DISTance \n
		Snippet: value: float = driver.source.fsimulator.scm.los.get_distance() \n
		Sets the distance between the base station (BS) and the user terminal (UT) . \n
			:return: los_3_ddistance: float Range: 0 to 1000
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SCM:LOS:DISTance?')
		return Conversions.str_to_float(response)

	def set_distance(self, los_3_ddistance: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:LOS:DISTance \n
		Snippet: driver.source.fsimulator.scm.los.set_distance(los_3_ddistance = 1.0) \n
		Sets the distance between the base station (BS) and the user terminal (UT) . \n
			:param los_3_ddistance: float Range: 0 to 1000
		"""
		param = Conversions.decimal_value_to_str(los_3_ddistance)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:LOS:DISTance {param}')

	def get_kfactor(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:LOS:KFACtor \n
		Snippet: value: float = driver.source.fsimulator.scm.los.get_kfactor() \n
		Sets the ricean K factor. \n
			:return: factor: float Range: -50 to 0
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SCM:LOS:KFACtor?')
		return Conversions.str_to_float(response)

	def set_kfactor(self, factor: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:LOS:KFACtor \n
		Snippet: driver.source.fsimulator.scm.los.set_kfactor(factor = 1.0) \n
		Sets the ricean K factor. \n
			:param factor: float Range: -50 to 0
		"""
		param = Conversions.decimal_value_to_str(factor)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:LOS:KFACtor {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:LOS:STATe \n
		Snippet: value: bool = driver.source.fsimulator.scm.los.get_state() \n
		Adds a line-of-sight (LOS) component to the cluster. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SCM:LOS:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:LOS:STATe \n
		Snippet: driver.source.fsimulator.scm.los.set_state(state = False) \n
		Adds a line-of-sight (LOS) component to the cluster. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:LOS:STATe {param}')

	def clone(self) -> 'Los':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Los(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
