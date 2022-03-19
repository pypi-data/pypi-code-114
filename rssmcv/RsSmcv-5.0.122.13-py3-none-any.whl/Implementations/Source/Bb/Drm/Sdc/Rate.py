from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rate:
	"""Rate commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Profile, default value after init: Profile.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rate", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_profile_get', 'repcap_profile_set', repcap.Profile.Nr1)

	def repcap_profile_set(self, profile: repcap.Profile) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Profile.Default
		Default value after init: Profile.Nr1"""
		self._cmd_group.set_repcap_enum_value(profile)

	def repcap_profile_get(self) -> repcap.Profile:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	# noinspection PyTypeChecker
	def get(self, profile=repcap.Profile.Default) -> enums.DrmCodingCoderate:
		"""SCPI: [SOURce<HW>]:BB:DRM:SDC:RATE<CH> \n
		Snippet: value: enums.DrmCodingCoderate = driver.source.bb.drm.sdc.rate.get(profile = repcap.Profile.Default) \n
		Queries the overall code rate of the . \n
			:param profile: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rate')
			:return: drm_sdc_rate: R025| R033| R040| R041| R045| R048| R050| R055| R057| R058| R060| R062| R066| R071| R072| R078| INV R0xy 0xy constitutes a code rate of 0.xy INV Invalid code rate"""
		profile_cmd_val = self._cmd_group.get_repcap_cmd_value(profile, repcap.Profile)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DRM:SDC:RATE{profile_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.DrmCodingCoderate)

	def clone(self) -> 'Rate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
