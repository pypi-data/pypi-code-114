from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class L1C:
	"""L1C commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("l1C", core, parent)

	def set(self, signal_state: bool, monitorPane=repcap.MonitorPane.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay:POWer:SYSTem:QZSS:SIGNal:L1Band:L1C \n
		Snippet: driver.source.bb.gnss.monitor.display.power.system.qzss.signal.l1Band.l1C.set(signal_state = False, monitorPane = repcap.MonitorPane.Default) \n
		No command help available \n
			:param signal_state: No help available
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
		"""
		param = Conversions.bool_to_str(signal_state)
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay:POWer:SYSTem:QZSS:SIGNal:L1Band:L1C {param}')

	def get(self, monitorPane=repcap.MonitorPane.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay:POWer:SYSTem:QZSS:SIGNal:L1Band:L1C \n
		Snippet: value: bool = driver.source.bb.gnss.monitor.display.power.system.qzss.signal.l1Band.l1C.get(monitorPane = repcap.MonitorPane.Default) \n
		No command help available \n
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
			:return: signal_state: No help available"""
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay:POWer:SYSTem:QZSS:SIGNal:L1Band:L1C?')
		return Conversions.str_to_bool(response)
