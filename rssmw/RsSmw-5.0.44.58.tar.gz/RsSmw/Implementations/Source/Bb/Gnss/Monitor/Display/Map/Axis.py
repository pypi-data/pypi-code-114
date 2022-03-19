from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Axis:
	"""Axis commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("axis", core, parent)

	def set(self, axis_type: enums.AxisType, monitorPane=repcap.MonitorPane.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay:MAP:AXIS \n
		Snippet: driver.source.bb.gnss.monitor.display.map.axis.set(axis_type = enums.AxisType.CIRCles, monitorPane = repcap.MonitorPane.Default) \n
		Changes the axis type in the 'Map View' display. \n
			:param axis_type: GRID| CIRCles
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
		"""
		param = Conversions.enum_scalar_to_str(axis_type, enums.AxisType)
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay:MAP:AXIS {param}')

	# noinspection PyTypeChecker
	def get(self, monitorPane=repcap.MonitorPane.Default) -> enums.AxisType:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay:MAP:AXIS \n
		Snippet: value: enums.AxisType = driver.source.bb.gnss.monitor.display.map.axis.get(monitorPane = repcap.MonitorPane.Default) \n
		Changes the axis type in the 'Map View' display. \n
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
			:return: axis_type: GRID| CIRCles"""
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay:MAP:AXIS?')
		return Conversions.str_to_scalar_enum(response, enums.AxisType)
