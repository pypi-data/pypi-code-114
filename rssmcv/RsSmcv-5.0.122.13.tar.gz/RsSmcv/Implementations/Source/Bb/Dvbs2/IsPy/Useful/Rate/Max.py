from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Max:
	"""Max commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("max", core, parent)

	def get(self, inputStream=repcap.InputStream.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:[IS<CH>]:USEFul:[RATE]:MAX \n
		Snippet: value: float = driver.source.bb.dvbs2.isPy.useful.rate.max.get(inputStream = repcap.InputStream.Default) \n
		Queries the maximum data rate, that is derived from the current modulation parameter settings. The value is the optimal
		value at the TS input interface, that is necessary for the modulator. \n
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
			:return: max_use_data_rate: float Range: 0 to 999999999"""
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVBS2:IS{inputStream_cmd_val}:USEFul:RATE:MAX?')
		return Conversions.str_to_float(response)
