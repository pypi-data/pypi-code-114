from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Arrival:
	"""Arrival commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("arrival", core, parent)

	@property
	def zenith(self):
		"""zenith commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_zenith'):
			from .Zenith import Zenith
			self._zenith = Zenith(self._core, self._cmd_group)
		return self._zenith

	def get_angle(self) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:LOS:ARRival:[ANGLe] \n
		Snippet: value: float = driver.source.fsimulator.scm.los.arrival.get_angle() \n
		Sets the AoD and AoA of the LOS component. \n
			:return: angle: float Range: 0 to 359.999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:SCM:LOS:ARRival:ANGLe?')
		return Conversions.str_to_float(response)

	def set_angle(self, angle: float) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:SCM:LOS:ARRival:[ANGLe] \n
		Snippet: driver.source.fsimulator.scm.los.arrival.set_angle(angle = 1.0) \n
		Sets the AoD and AoA of the LOS component. \n
			:param angle: float Range: 0 to 359.999
		"""
		param = Conversions.decimal_value_to_str(angle)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:SCM:LOS:ARRival:ANGLe {param}')

	def clone(self) -> 'Arrival':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Arrival(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
