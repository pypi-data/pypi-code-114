from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class System:
	"""System commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("system", core, parent)

	def set(self, system: enums.Hybrid, monitorPane=repcap.MonitorPane.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay:TRAJectory:SYSTem \n
		Snippet: driver.source.bb.gnss.monitor.display.trajectory.system.set(system = enums.Hybrid.BEIDou, monitorPane = repcap.MonitorPane.Default) \n
		Selects the GNSS system which elevation/azimuth variation over 24 hours is displayed. \n
			:param system: GPS| GALileo| GLONass| BEIDou| QZSS| SBAS
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
		"""
		param = Conversions.enum_scalar_to_str(system, enums.Hybrid)
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay:TRAJectory:SYSTem {param}')

	# noinspection PyTypeChecker
	def get(self, monitorPane=repcap.MonitorPane.Default) -> enums.Hybrid:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay:TRAJectory:SYSTem \n
		Snippet: value: enums.Hybrid = driver.source.bb.gnss.monitor.display.trajectory.system.get(monitorPane = repcap.MonitorPane.Default) \n
		Selects the GNSS system which elevation/azimuth variation over 24 hours is displayed. \n
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
			:return: system: GPS| GALileo| GLONass| BEIDou| QZSS| SBAS"""
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay:TRAJectory:SYSTem?')
		return Conversions.str_to_scalar_enum(response, enums.Hybrid)
