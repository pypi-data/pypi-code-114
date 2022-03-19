from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CndRatio:
	"""CndRatio commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cndRatio", core, parent)

	def set(self, cn_density_ratio: float, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:AWGN:[RF<CH>]:CNDRatio \n
		Snippet: driver.source.bb.gnss.awgn.rf.cndRatio.set(cn_density_ratio = 1.0, path = repcap.Path.Default) \n
		Sets the carrier power to noise power ratio C/N ratio, that is the difference of carrier power and noise power: C/N ratio
		= Carrier power - Noise power Noise power = Refrence power + 10 * log10(System Bandwidth) - C/ N0 \n
			:param cn_density_ratio: float Range: 0 to 55
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
		"""
		param = Conversions.decimal_value_to_str(cn_density_ratio)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:AWGN:RF{path_cmd_val}:CNDRatio {param}')

	def get(self, path=repcap.Path.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:AWGN:[RF<CH>]:CNDRatio \n
		Snippet: value: float = driver.source.bb.gnss.awgn.rf.cndRatio.get(path = repcap.Path.Default) \n
		Sets the carrier power to noise power ratio C/N ratio, that is the difference of carrier power and noise power: C/N ratio
		= Carrier power - Noise power Noise power = Refrence power + 10 * log10(System Bandwidth) - C/ N0 \n
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
			:return: cn_density_ratio: float Range: 0 to 55"""
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:AWGN:RF{path_cmd_val}:CNDRatio?')
		return Conversions.str_to_float(response)
