from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............Internal.RepeatedCapability import RepeatedCapability
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class El5S:
	"""El5S commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Index, default value after init: Index.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("el5S", core, parent)
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

	def set(self, signal_state: bool, monitorPane=repcap.MonitorPane.Default, index=repcap.Index.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay:POWer:SYSTem:SBAS:SIGNal:L5Band:EL5S<US> \n
		Snippet: driver.source.bb.gnss.monitor.display.power.system.sbas.signal.l5Band.el5S.set(signal_state = False, monitorPane = repcap.MonitorPane.Default, index = repcap.Index.Default) \n
		Defines the signals to be visualized on the 'Power View' graph. \n
			:param signal_state: 1| ON| 0| OFF
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'El5S')
		"""
		param = Conversions.bool_to_str(signal_state)
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay:POWer:SYSTem:SBAS:SIGNal:L5Band:EL5S{index_cmd_val} {param}')

	def get(self, monitorPane=repcap.MonitorPane.Default, index=repcap.Index.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay:POWer:SYSTem:SBAS:SIGNal:L5Band:EL5S<US> \n
		Snippet: value: bool = driver.source.bb.gnss.monitor.display.power.system.sbas.signal.l5Band.el5S.get(monitorPane = repcap.MonitorPane.Default, index = repcap.Index.Default) \n
		Defines the signals to be visualized on the 'Power View' graph. \n
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'El5S')
			:return: signal_state: 1| ON| 0| OFF"""
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay:POWer:SYSTem:SBAS:SIGNal:L5Band:EL5S{index_cmd_val}?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'El5S':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = El5S(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
