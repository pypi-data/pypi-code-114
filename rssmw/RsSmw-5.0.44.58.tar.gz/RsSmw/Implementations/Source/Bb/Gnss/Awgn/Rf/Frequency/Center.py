from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Center:
	"""Center commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("center", core, parent)

	def set(self, center_frequency: int, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:AWGN:[RF<CH>]:FREQuency:CENTer \n
		Snippet: driver.source.bb.gnss.awgn.rf.frequency.center.set(center_frequency = 1, path = repcap.Path.Default) \n
		Sets center frequency of the noise signal. \n
			:param center_frequency: integer Range: 1E9 to 2E9
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
		"""
		param = Conversions.decimal_value_to_str(center_frequency)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:AWGN:RF{path_cmd_val}:FREQuency:CENTer {param}')

	def get(self, path=repcap.Path.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:AWGN:[RF<CH>]:FREQuency:CENTer \n
		Snippet: value: int = driver.source.bb.gnss.awgn.rf.frequency.center.get(path = repcap.Path.Default) \n
		Sets center frequency of the noise signal. \n
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
			:return: center_frequency: integer Range: 1E9 to 2E9"""
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:AWGN:RF{path_cmd_val}:FREQuency:CENTer?')
		return Conversions.str_to_int(response)
