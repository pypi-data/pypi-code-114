from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CbIndex:
	"""CbIndex commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: IndexNull, default value after init: IndexNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cbIndex", core, parent)
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

	def set(self, code_book_index: int, userIx=repcap.UserIx.Default, indexNull=repcap.IndexNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:USER<CH>:APM:CBINdex<DIR_OPTIONAL> \n
		Snippet: driver.source.bb.v5G.downlink.user.apm.cbIndex.set(code_book_index = 1, userIx = repcap.UserIx.Default, indexNull = repcap.IndexNull.Default) \n
		No command help available \n
			:param code_book_index: No help available
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'CbIndex')
		"""
		param = Conversions.decimal_value_to_str(code_book_index)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:USER{userIx_cmd_val}:APM:CBINdex{indexNull_cmd_val} {param}')

	def get(self, userIx=repcap.UserIx.Default, indexNull=repcap.IndexNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:USER<CH>:APM:CBINdex<DIR_OPTIONAL> \n
		Snippet: value: int = driver.source.bb.v5G.downlink.user.apm.cbIndex.get(userIx = repcap.UserIx.Default, indexNull = repcap.IndexNull.Default) \n
		No command help available \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'CbIndex')
			:return: code_book_index: No help available"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:USER{userIx_cmd_val}:APM:CBINdex{indexNull_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'CbIndex':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CbIndex(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
