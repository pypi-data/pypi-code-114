from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LogPoint:
	"""LogPoint commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: IndexNull, default value after init: IndexNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("logPoint", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_indexNull_get', 'repcap_indexNull_set', repcap.IndexNull.Nr0)

	def repcap_indexNull_set(self, indexNull: repcap.IndexNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to IndexNull.Default
		Default value after init: IndexNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(indexNull)

	def repcap_indexNull_get(self) -> repcap.IndexNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, log_point_state: bool, indexNull=repcap.IndexNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:DL:LOGPoint<CH0> \n
		Snippet: driver.source.bb.v5G.logGen.downlink.logPoint.set(log_point_state = False, indexNull = repcap.IndexNull.Default) \n
		No command help available \n
			:param log_point_state: No help available
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'LogPoint')
		"""
		param = Conversions.bool_to_str(log_point_state)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:LOGGen:DL:LOGPoint{indexNull_cmd_val} {param}')

	def get(self, indexNull=repcap.IndexNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:V5G:LOGGen:DL:LOGPoint<CH0> \n
		Snippet: value: bool = driver.source.bb.v5G.logGen.downlink.logPoint.get(indexNull = repcap.IndexNull.Default) \n
		No command help available \n
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'LogPoint')
			:return: log_point_state: No help available"""
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:LOGGen:DL:LOGPoint{indexNull_cmd_val}?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'LogPoint':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LogPoint(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
