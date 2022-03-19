from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Location:
	"""Location commands group definition. 6 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("location", core, parent)

	@property
	def coordinates(self):
		"""coordinates commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_coordinates'):
			from .Coordinates import Coordinates
			self._coordinates = Coordinates(self._core, self._cmd_group)
		return self._coordinates

	def get_uradius(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:QZSS:LOCation:URADius \n
		Snippet: value: int = driver.source.bb.gnss.adGeneration.qzss.location.get_uradius() \n
		Sets the Uncertainty Radius, i.e. sets the maximum radius of the area within which the two-dimensional location of the UE
		is bounded. \n
			:return: radius: integer Range: 0 to 1.E6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:ADGeneration:QZSS:LOCation:URADius?')
		return Conversions.str_to_int(response)

	def set_uradius(self, radius: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:ADGeneration:QZSS:LOCation:URADius \n
		Snippet: driver.source.bb.gnss.adGeneration.qzss.location.set_uradius(radius = 1) \n
		Sets the Uncertainty Radius, i.e. sets the maximum radius of the area within which the two-dimensional location of the UE
		is bounded. \n
			:param radius: integer Range: 0 to 1.E6
		"""
		param = Conversions.decimal_value_to_str(radius)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:ADGeneration:QZSS:LOCation:URADius {param}')

	def clone(self) -> 'Location':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Location(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
