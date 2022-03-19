from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stream:
	"""Stream commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stream", core, parent)

	def set(self, stream: enums.RefStream, monitorPane=repcap.MonitorPane.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay:STReam \n
		Snippet: driver.source.bb.gnss.monitor.display.stream.set(stream = enums.RefStream.S1, monitorPane = repcap.MonitorPane.Default) \n
		In GNSS advanced mode, switches between available streams in 'Display Type > HW Channels'. For the display type, see
		[:SOURce<hw>]:BB:GNSS:MONitor<ch>:DISPlay. \n
			:param stream: S1| S2| S3| S4
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
		"""
		param = Conversions.enum_scalar_to_str(stream, enums.RefStream)
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay:STReam {param}')

	# noinspection PyTypeChecker
	def get(self, monitorPane=repcap.MonitorPane.Default) -> enums.RefStream:
		"""SCPI: [SOURce<HW>]:BB:GNSS:MONitor<CH>:DISPlay:STReam \n
		Snippet: value: enums.RefStream = driver.source.bb.gnss.monitor.display.stream.get(monitorPane = repcap.MonitorPane.Default) \n
		In GNSS advanced mode, switches between available streams in 'Display Type > HW Channels'. For the display type, see
		[:SOURce<hw>]:BB:GNSS:MONitor<ch>:DISPlay. \n
			:param monitorPane: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Monitor')
			:return: stream: S1| S2| S3| S4"""
		monitorPane_cmd_val = self._cmd_group.get_repcap_cmd_value(monitorPane, repcap.MonitorPane)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:MONitor{monitorPane_cmd_val}:DISPlay:STReam?')
		return Conversions.str_to_scalar_enum(response, enums.RefStream)
