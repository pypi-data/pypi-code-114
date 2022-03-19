from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class JsRatio:
	"""JsRatio commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("jsRatio", core, parent)

	def set(self, js_ratio: float, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:AWGN:[RF<CH>]:JSRatio \n
		Snippet: driver.source.bb.gnss.awgn.rf.jsRatio.set(js_ratio = 1.0, path = repcap.Path.Default) \n
		Sets the jammer (interferer) power to signal power ratio C/I ratio, that is the difference of carrier power and noise
		power: C/I ratio = Carrier power - Interferer power Interferer power = Refrence power + J/S \n
			:param js_ratio: float Range: -50 to 50
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
		"""
		param = Conversions.decimal_value_to_str(js_ratio)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:AWGN:RF{path_cmd_val}:JSRatio {param}')

	def get(self, path=repcap.Path.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:AWGN:[RF<CH>]:JSRatio \n
		Snippet: value: float = driver.source.bb.gnss.awgn.rf.jsRatio.get(path = repcap.Path.Default) \n
		Sets the jammer (interferer) power to signal power ratio C/I ratio, that is the difference of carrier power and noise
		power: C/I ratio = Carrier power - Interferer power Interferer power = Refrence power + J/S \n
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
			:return: js_ratio: float Range: -50 to 50"""
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:AWGN:RF{path_cmd_val}:JSRatio?')
		return Conversions.str_to_float(response)
