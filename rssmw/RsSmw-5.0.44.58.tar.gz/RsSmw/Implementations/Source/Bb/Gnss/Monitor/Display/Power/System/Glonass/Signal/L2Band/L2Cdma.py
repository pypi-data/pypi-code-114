from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............Internal.RepeatedCapability import RepeatedCapability
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class L2Cdma:
	"""L2Cdma commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: IndexNull, default value after init: IndexNull.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("l2Cdma", core, parent)
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

	def set(self, signal_state: bool, monitorPane=repcap.MonitorPane.Default, indexNull=repcap.IndexNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay:POWer:SYSTem:GLONass:SIGNal:L2Band:L2CDma<US0> \n
		Snippet: driver.source.bb.gnss.monitor.display.power.system.glonass.signal.l2Band.l2Cdma.set(signal_state = False, monitorPane = repcap.MonitorPane.Default, indexNull = repcap.IndexNull.Default) \n
		No command help available \n
			:param signal_state: No help available
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'L2Cdma')
		"""
		param = Conversions.bool_to_str(signal_state)
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay:POWer:SYSTem:GLONass:SIGNal:L2Band:L2CDma{indexNull_cmd_val} {param}')

	def get(self, monitorPane=repcap.MonitorPane.Default, indexNull=repcap.IndexNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay:POWer:SYSTem:GLONass:SIGNal:L2Band:L2CDma<US0> \n
		Snippet: value: bool = driver.source.bb.gnss.monitor.display.power.system.glonass.signal.l2Band.l2Cdma.get(monitorPane = repcap.MonitorPane.Default, indexNull = repcap.IndexNull.Default) \n
		No command help available \n
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'L2Cdma')
			:return: signal_state: No help available"""
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay:POWer:SYSTem:GLONass:SIGNal:L2Band:L2CDma{indexNull_cmd_val}?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'L2Cdma':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = L2Cdma(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
