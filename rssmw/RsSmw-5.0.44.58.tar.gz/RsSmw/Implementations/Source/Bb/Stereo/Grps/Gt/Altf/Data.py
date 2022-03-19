from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: DataNull, default value after init: DataNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_dataNull_get', 'repcap_dataNull_set', repcap.DataNull.Nr0)

	def repcap_dataNull_set(self, dataNull: repcap.DataNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to DataNull.Default
		Default value after init: DataNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(dataNull)

	def repcap_dataNull_get(self) -> repcap.DataNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, data: float, groupNull=repcap.GroupNull.Default, dataNull=repcap.DataNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GRPS:GT<ST0>:ALTF:DATA<CH0> \n
		Snippet: driver.source.bb.stereo.grps.gt.altf.data.set(data = 1.0, groupNull = repcap.GroupNull.Default, dataNull = repcap.DataNull.Default) \n
		No command help available \n
			:param data: No help available
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Gt')
			:param dataNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Data')
		"""
		param = Conversions.decimal_value_to_str(data)
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		dataNull_cmd_val = self._cmd_group.get_repcap_cmd_value(dataNull, repcap.DataNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:STEReo:GRPS:GT{groupNull_cmd_val}:ALTF:DATA{dataNull_cmd_val} {param}')

	def get(self, groupNull=repcap.GroupNull.Default, dataNull=repcap.DataNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:STEReo:GRPS:GT<ST0>:ALTF:DATA<CH0> \n
		Snippet: value: float = driver.source.bb.stereo.grps.gt.altf.data.get(groupNull = repcap.GroupNull.Default, dataNull = repcap.DataNull.Default) \n
		No command help available \n
			:param groupNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Gt')
			:param dataNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Data')
			:return: data: No help available"""
		groupNull_cmd_val = self._cmd_group.get_repcap_cmd_value(groupNull, repcap.GroupNull)
		dataNull_cmd_val = self._cmd_group.get_repcap_cmd_value(dataNull, repcap.DataNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:STEReo:GRPS:GT{groupNull_cmd_val}:ALTF:DATA{dataNull_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Data':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Data(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
