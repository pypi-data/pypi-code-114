from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Antenna:
	"""Antenna commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("antenna", core, parent)

	def set(self, antenna: enums.AntennaNr, monitorPane=repcap.MonitorPane.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay:ANTenna \n
		Snippet: driver.source.bb.gnss.monitor.display.antenna.set(antenna = enums.AntennaNr.A1, monitorPane = repcap.MonitorPane.Default) \n
		Sets the antenna for that the information displayed in the 'Simulation Monitor' applies. \n
			:param antenna: A1| A2| A3| A4
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
		"""
		param = Conversions.enum_scalar_to_str(antenna, enums.AntennaNr)
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay:ANTenna {param}')

	# noinspection PyTypeChecker
	def get(self, monitorPane=repcap.MonitorPane.Default) -> enums.AntennaNr:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay:ANTenna \n
		Snippet: value: enums.AntennaNr = driver.source.bb.gnss.monitor.display.antenna.get(monitorPane = repcap.MonitorPane.Default) \n
		Sets the antenna for that the information displayed in the 'Simulation Monitor' applies. \n
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
			:return: antenna: A1| A2| A3| A4"""
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay:ANTenna?')
		return Conversions.str_to_scalar_enum(response, enums.AntennaNr)
