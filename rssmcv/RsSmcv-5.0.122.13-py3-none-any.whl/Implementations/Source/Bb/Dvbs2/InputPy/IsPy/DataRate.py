from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DataRate:
	"""DataRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dataRate", core, parent)

	def get(self, inputStream=repcap.InputStream.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:DVBS2:[INPut]:[IS<CH>]:DATarate \n
		Snippet: value: float = driver.source.bb.dvbs2.inputPy.isPy.dataRate.get(inputStream = repcap.InputStream.Default) \n
			INTRO_CMD_HELP: Queries the measured value of the data rate of one of the following: \n
			- External transport stream including null packets input at 'User 1' connector
			- External transport stream including null packets input at 'IP Data/LAN' connector (TSoverIP)
		The value equals the sum of useful data rate rmeas and the rate of null packets r0: rmeas = rmeas + r0 \n
			:param inputStream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'IsPy')
			:return: meas_data_rate: float Range: 0 to 999999999"""
		inputStream_cmd_val = self._cmd_group.get_repcap_cmd_value(inputStream, repcap.InputStream)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVBS2:INPut:IS{inputStream_cmd_val}:DATarate?')
		return Conversions.str_to_float(response)
