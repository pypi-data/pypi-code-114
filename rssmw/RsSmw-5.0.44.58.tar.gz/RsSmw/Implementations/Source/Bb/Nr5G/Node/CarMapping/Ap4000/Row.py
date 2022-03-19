from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Row:
	"""Row commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: RowNull, default value after init: RowNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("row", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_rowNull_get', 'repcap_rowNull_set', repcap.RowNull.Nr0)

	def repcap_rowNull_set(self, rowNull: repcap.RowNull) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to RowNull.Default
		Default value after init: RowNull.Nr0"""
		self._cmd_group.set_repcap_enum_value(rowNull)

	def repcap_rowNull_get(self) -> repcap.RowNull:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, ap_4000: bool, rowNull=repcap.RowNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CARMapping:AP4000:[ROW<CH0>] \n
		Snippet: driver.source.bb.nr5G.node.carMapping.ap4000.row.set(ap_4000 = False, rowNull = repcap.RowNull.Default) \n
		Sets if the SS/PBCHs are output at the selected output. \n
			:param ap_4000: 0| 1| OFF| ON
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
		"""
		param = Conversions.bool_to_str(ap_4000)
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CARMapping:AP4000:ROW{rowNull_cmd_val} {param}')

	def get(self, rowNull=repcap.RowNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CARMapping:AP4000:[ROW<CH0>] \n
		Snippet: value: bool = driver.source.bb.nr5G.node.carMapping.ap4000.row.get(rowNull = repcap.RowNull.Default) \n
		Sets if the SS/PBCHs are output at the selected output. \n
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
			:return: ap_4000: 0| 1| OFF| ON"""
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CARMapping:AP4000:ROW{rowNull_cmd_val}?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Row':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Row(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
