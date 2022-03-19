from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Depth:
	"""Depth commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Index, default value after init: Index.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("depth", core, parent)
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

	def set(self, depth: float, index=repcap.Index.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:EEW:DEPTh<CH> \n
		Snippet: driver.source.bb.isdbt.eew.depth.set(depth = 1.0, index = repcap.Index.Default) \n
		Sets the depth of the epicenter of the seismic event. \n
			:param depth: float Range: 0 M to 1023 M
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Depth')
		"""
		param = Conversions.decimal_value_to_str(depth)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:EEW:DEPTh{index_cmd_val} {param}')

	def get(self, index=repcap.Index.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:EEW:DEPTh<CH> \n
		Snippet: value: float = driver.source.bb.isdbt.eew.depth.get(index = repcap.Index.Default) \n
		Sets the depth of the epicenter of the seismic event. \n
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Depth')
			:return: depth: float Range: 0 M to 1023 M"""
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ISDBt:EEW:DEPTh{index_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Depth':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Depth(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
