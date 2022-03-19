from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sdc:
	"""Sdc commands group definition. 4 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sdc", core, parent)

	@property
	def level(self):
		"""level commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_level'):
			from .Level import Level
			self._level = Level(self._core, self._cmd_group)
		return self._level

	@property
	def profile(self):
		"""profile commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_profile'):
			from .Profile import Profile
			self._profile = Profile(self._core, self._cmd_group)
		return self._profile

	@property
	def rate(self):
		"""rate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rate'):
			from .Rate import Rate
			self._rate = Rate(self._core, self._cmd_group)
		return self._rate

	# noinspection PyTypeChecker
	def get_constel(self) -> enums.DrmCodingConstelSdc:
		"""SCPI: [SOURce<HW>]:BB:DRM:SDC:CONStel \n
		Snippet: value: enums.DrmCodingConstelSdc = driver.source.bb.drm.sdc.get_constel() \n
		Queries the constellation of the . \n
			:return: drm_const_sdc: Q16| Q4| INV Q16 16 Q4 4 INV Invalid constellation
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DRM:SDC:CONStel?')
		return Conversions.str_to_scalar_enum(response, enums.DrmCodingConstelSdc)

	def clone(self) -> 'Sdc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sdc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
