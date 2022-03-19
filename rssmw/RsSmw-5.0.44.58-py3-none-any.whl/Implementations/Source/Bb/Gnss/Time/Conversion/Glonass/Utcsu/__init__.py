from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Utcsu:
	"""Utcsu commands group definition. 8 total commands, 3 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("utcsu", core, parent)

	@property
	def aone(self):
		"""aone commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_aone'):
			from .Aone import Aone
			self._aone = Aone(self._core, self._cmd_group)
		return self._aone

	@property
	def azero(self):
		"""azero commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_azero'):
			from .Azero import Azero
			self._azero = Azero(self._core, self._cmd_group)
		return self._azero

	@property
	def tot(self):
		"""tot commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_tot'):
			from .Tot import Tot
			self._tot = Tot(self._core, self._cmd_group)
		return self._tot

	def get_ioffset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:CONVersion:GLONass:UTCSu:IOFFset \n
		Snippet: value: int = driver.source.bb.gnss.time.conversion.glonass.utcsu.get_ioffset() \n
		Queries the integer offset. \n
			:return: integer_offset: integer Range: 0 to 604800
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:TIME:CONVersion:GLONass:UTCSu:IOFFset?')
		return Conversions.str_to_int(response)

	def get_wnot(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:CONVersion:GLONass:UTCSu:WNOT \n
		Snippet: value: int = driver.source.bb.gnss.time.conversion.glonass.utcsu.get_wnot() \n
		Sets the UTC data reference week number, WNt. \n
			:return: wnot: integer Range: 0 to 255
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:TIME:CONVersion:GLONass:UTCSu:WNOT?')
		return Conversions.str_to_int(response)

	def set_wnot(self, wnot: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:TIME:CONVersion:GLONass:UTCSu:WNOT \n
		Snippet: driver.source.bb.gnss.time.conversion.glonass.utcsu.set_wnot(wnot = 1) \n
		Sets the UTC data reference week number, WNt. \n
			:param wnot: integer Range: 0 to 255
		"""
		param = Conversions.decimal_value_to_str(wnot)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:TIME:CONVersion:GLONass:UTCSu:WNOT {param}')

	def clone(self) -> 'Utcsu':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Utcsu(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
