from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Row:
	"""Row commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Row, default value after init: Row.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("row", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_row_get', 'repcap_row_set', repcap.Row.Nr1)

	def repcap_row_set(self, row: repcap.Row) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Row.Default
		Default value after init: Row.Nr1"""
		self._cmd_group.set_repcap_enum_value(row)

	def repcap_row_get(self) -> repcap.Row:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, xss_ant_ports: bool, row=repcap.Row.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:APM:CS:XSSap:ROW<ST0> \n
		Snippet: driver.source.bb.v5G.downlink.apm.cs.xssap.row.set(xss_ant_ports = False, row = repcap.Row.Default) \n
		Defines the mapping of the logical antenna ports for synchronization signal (AP 300 to 313) to the available physical TX
		antennas (basebands) . Row (ROW0 to ROW7) defines the baseband and at the same time also the cell. \n
			:param xss_ant_ports: 1| ON| 0| OFF
			:param row: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Row')
		"""
		param = Conversions.bool_to_str(xss_ant_ports)
		row_cmd_val = self._cmd_group.get_repcap_cmd_value(row, repcap.Row)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:APM:CS:XSSap:ROW{row_cmd_val} {param}')

	def get(self, row=repcap.Row.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:APM:CS:XSSap:ROW<ST0> \n
		Snippet: value: bool = driver.source.bb.v5G.downlink.apm.cs.xssap.row.get(row = repcap.Row.Default) \n
		Defines the mapping of the logical antenna ports for synchronization signal (AP 300 to 313) to the available physical TX
		antennas (basebands) . Row (ROW0 to ROW7) defines the baseband and at the same time also the cell. \n
			:param row: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Row')
			:return: xss_ant_ports: 1| ON| 0| OFF"""
		row_cmd_val = self._cmd_group.get_repcap_cmd_value(row, repcap.Row)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:APM:CS:XSSap:ROW{row_cmd_val}?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Row':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Row(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
