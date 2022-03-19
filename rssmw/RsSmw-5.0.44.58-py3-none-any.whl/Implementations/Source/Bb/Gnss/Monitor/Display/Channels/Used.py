from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Used:
	"""Used commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("used", core, parent)

	def get(self, monitorPane=repcap.MonitorPane.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay:CHANnels:USED \n
		Snippet: value: int = driver.source.bb.gnss.monitor.display.channels.used.get(monitorPane = repcap.MonitorPane.Default) \n
		Queries the number of active channels. The maximum number of active channels depends on the installed options, see
		'Channel budget'. \n
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
			:return: used_channels: integer Range: 0 to depends on installed options The *RST value depends on the installed GNSS system option, e.g. for GPS : *RST: 11"""
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay:CHANnels:USED?')
		return Conversions.str_to_int(response)
