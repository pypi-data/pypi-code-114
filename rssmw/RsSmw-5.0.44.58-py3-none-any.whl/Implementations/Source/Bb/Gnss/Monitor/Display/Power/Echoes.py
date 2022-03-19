from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Echoes:
	"""Echoes commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("echoes", core, parent)

	def set(self, show_echoes: bool, monitorPane=repcap.MonitorPane.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay:POWer:ECHoes \n
		Snippet: driver.source.bb.gnss.monitor.display.power.echoes.set(show_echoes = False, monitorPane = repcap.MonitorPane.Default) \n
		If enabled, the 'Power View' indicates also the echoes per SV. \n
			:param show_echoes: 1| ON| 0| OFF
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
		"""
		param = Conversions.bool_to_str(show_echoes)
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay:POWer:ECHoes {param}')

	def get(self, monitorPane=repcap.MonitorPane.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay:POWer:ECHoes \n
		Snippet: value: bool = driver.source.bb.gnss.monitor.display.power.echoes.get(monitorPane = repcap.MonitorPane.Default) \n
		If enabled, the 'Power View' indicates also the echoes per SV. \n
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
			:return: show_echoes: 1| ON| 0| OFF"""
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay:POWer:ECHoes?')
		return Conversions.str_to_bool(response)
