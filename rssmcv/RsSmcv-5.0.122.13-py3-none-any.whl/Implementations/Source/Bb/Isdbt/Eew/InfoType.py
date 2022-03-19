from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InfoType:
	"""InfoType commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Index, default value after init: Index.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("infoType", core, parent)
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

	def set(self, info_type: enums.IsdbtEewInfoType, index=repcap.Index.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:EEW:INFotype<CH> \n
		Snippet: driver.source.bb.isdbt.eew.infoType.set(info_type = enums.IsdbtEewInfoType.CANCeled, index = repcap.Index.Default) \n
		Provides information about the validity of the seismic motion warning. \n
			:param info_type: CANCeled| ISSued
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InfoType')
		"""
		param = Conversions.enum_scalar_to_str(info_type, enums.IsdbtEewInfoType)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:EEW:INFotype{index_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, index=repcap.Index.Default) -> enums.IsdbtEewInfoType:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:EEW:INFotype<CH> \n
		Snippet: value: enums.IsdbtEewInfoType = driver.source.bb.isdbt.eew.infoType.get(index = repcap.Index.Default) \n
		Provides information about the validity of the seismic motion warning. \n
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InfoType')
			:return: info_type: CANCeled| ISSued"""
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ISDBt:EEW:INFotype{index_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.IsdbtEewInfoType)

	def clone(self) -> 'InfoType':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = InfoType(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
