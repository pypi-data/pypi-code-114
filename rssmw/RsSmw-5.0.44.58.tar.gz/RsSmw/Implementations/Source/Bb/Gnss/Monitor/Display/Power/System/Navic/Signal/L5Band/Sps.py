from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sps:
	"""Sps commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sps", core, parent)

	def set(self, signal_state: bool, monitorPane=repcap.MonitorPane.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay:POWer:SYSTem:NAVic:SIGNal:L5Band:SPS \n
		Snippet: driver.source.bb.gnss.monitor.display.power.system.navic.signal.l5Band.sps.set(signal_state = False, monitorPane = repcap.MonitorPane.Default) \n
		Defines the signals to be visualized on the 'Power View' graph. \n
			:param signal_state: 1| ON| 0| OFF
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
		"""
		param = Conversions.bool_to_str(signal_state)
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay:POWer:SYSTem:NAVic:SIGNal:L5Band:SPS {param}')

	def get(self, monitorPane=repcap.MonitorPane.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay:POWer:SYSTem:NAVic:SIGNal:L5Band:SPS \n
		Snippet: value: bool = driver.source.bb.gnss.monitor.display.power.system.navic.signal.l5Band.sps.get(monitorPane = repcap.MonitorPane.Default) \n
		Defines the signals to be visualized on the 'Power View' graph. \n
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
			:return: signal_state: 1| ON| 0| OFF"""
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay:POWer:SYSTem:NAVic:SIGNal:L5Band:SPS?')
		return Conversions.str_to_bool(response)
