from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Msc:
	"""Msc commands group definition. 4 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("msc", core, parent)

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
	def get_constel(self) -> enums.DrmCodingConstelMsc:
		"""SCPI: [SOURce<HW>]:BB:DRM:MSC:CONStel \n
		Snippet: value: enums.DrmCodingConstelMsc = driver.source.bb.drm.msc.get_constel() \n
		Queries the constellation of the . \n
			:return: drm_const_msc: Q64N| Q64I| Q64Q| Q16| Q4| INV Q64N 64 non-hierarchical Q64I 64QAM hierarchical on I Q64Q 64QAM hierarchical on I and Q Q16 16QAM non-hierarchical Q4 4QAM non-hierarchical INV Invalid constellation
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DRM:MSC:CONStel?')
		return Conversions.str_to_scalar_enum(response, enums.DrmCodingConstelMsc)

	def clone(self) -> 'Msc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Msc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
