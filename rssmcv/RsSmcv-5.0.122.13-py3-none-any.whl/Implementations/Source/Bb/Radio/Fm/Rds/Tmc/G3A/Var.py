from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Var:
	"""Var commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: GroupTypeVariant, default value after init: GroupTypeVariant.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("var", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_groupTypeVariant_get', 'repcap_groupTypeVariant_set', repcap.GroupTypeVariant.Nr1)

	def repcap_groupTypeVariant_set(self, groupTypeVariant: repcap.GroupTypeVariant) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to GroupTypeVariant.Default
		Default value after init: GroupTypeVariant.Nr1"""
		self._cmd_group.set_repcap_enum_value(groupTypeVariant)

	def repcap_groupTypeVariant_get(self) -> repcap.GroupTypeVariant:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, g_3_avar: int, groupTypeVariant=repcap.GroupTypeVariant.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:TMC:G3A:VAR<CH> \n
		Snippet: driver.source.bb.radio.fm.rds.tmc.g3A.var.set(g_3_avar = 1, groupTypeVariant = repcap.GroupTypeVariant.Default) \n
		Sets the traffic message channel 3A group variants. \n
			:param g_3_avar: integer Range: 0 to 65535
			:param groupTypeVariant: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Var')
		"""
		param = Conversions.decimal_value_to_str(g_3_avar)
		groupTypeVariant_cmd_val = self._cmd_group.get_repcap_cmd_value(groupTypeVariant, repcap.GroupTypeVariant)
		self._core.io.write(f'SOURce<HwInstance>:BB:RADio:FM:RDS:TMC:G3A:VAR{groupTypeVariant_cmd_val} {param}')

	def get(self, groupTypeVariant=repcap.GroupTypeVariant.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:RADio:FM:RDS:TMC:G3A:VAR<CH> \n
		Snippet: value: int = driver.source.bb.radio.fm.rds.tmc.g3A.var.get(groupTypeVariant = repcap.GroupTypeVariant.Default) \n
		Sets the traffic message channel 3A group variants. \n
			:param groupTypeVariant: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Var')
			:return: g_3_avar: integer Range: 0 to 65535"""
		groupTypeVariant_cmd_val = self._cmd_group.get_repcap_cmd_value(groupTypeVariant, repcap.GroupTypeVariant)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:RADio:FM:RDS:TMC:G3A:VAR{groupTypeVariant_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Var':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Var(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
