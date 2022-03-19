from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Index, default value after init: Index.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_index_get', 'repcap_index_set', repcap.Index.Nr1)

	def repcap_index_set(self, index: repcap.Index) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Index.Default
		Default value after init: Index.Nr1"""
		self._cmd_group.set_repcap_enum_value(index)

	def repcap_index_get(self) -> repcap.Index:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	# noinspection PyTypeChecker
	def get(self, index=repcap.Index.Default) -> enums.TdmbInputSignalProtectionLevel:
		"""SCPI: [SOURce<HW>]:BB:TDMB:PROTection:LEVel<CH> \n
		Snippet: value: enums.TdmbInputSignalProtectionLevel = driver.source.bb.tdmb.protection.level.get(index = repcap.Index.Default) \n
		Queries the protection level. The level depends on the protection profile. \n
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Level')
			:return: prot_level: UNDefined| EP1A| EP2A| EP3A| EP4A| EP1B| EP2B| EP3B| EP4B| UP1| UP2| UP3| UP4| UP5 UP1|UP2|UP3|UP4|UP5 Protection level 1 to 5 with protection profile EP1A|EP2A|EP3A|EP4A Protection level 1A to 4A with protection profile EP1B|EP2B|EP3B|EP4B Protection level 1B to 4B with protection profile UNDefined No protection profile detected"""
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDMB:PROTection:LEVel{index_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.TdmbInputSignalProtectionLevel)

	def clone(self) -> 'Level':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Level(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
