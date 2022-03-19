from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Allocated:
	"""Allocated commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("allocated", core, parent)

	def get(self, monitorPane=repcap.MonitorPane.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay:CHANnels:ALLocated \n
		Snippet: value: int = driver.source.bb.gnss.monitor.display.channels.allocated.get(monitorPane = repcap.MonitorPane.Default) \n
		Queries the maximum number of allocated channels. The maximum number of allocated channels depends on the installed
		options, see 'Channel budget'. \n
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
			:return: allocated_chans: integer Range: 0 to depends on installed options"""
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay:CHANnels:ALLocated?')
		return Conversions.str_to_int(response)
