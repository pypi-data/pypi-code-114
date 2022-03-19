from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DataRate:
	"""DataRate commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dataRate", core, parent)

	def get_low(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DVBT:[INPut]:DATarate:LOW \n
		Snippet: value: float = driver.source.bb.dvbt.inputPy.dataRate.get_low() \n
			INTRO_CMD_HELP: Queries the measured value of the data rate of one of the following: \n
			- External transport stream including null packets input at 'User 1' connector
			- External transport stream including null packets input at 'IP Data/LAN' connector (TSoverIP)
		The value equals the sum of useful data rate rmeas and the rate of null packets r0: rmeas = rmeas + r0 \n
			:return: meas_drlp: float Range: 0 to 9999999999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:INPut:DATarate:LOW?')
		return Conversions.str_to_float(response)

	def get_high(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DVBT:[INPut]:DATarate:[HIGH] \n
		Snippet: value: float = driver.source.bb.dvbt.inputPy.dataRate.get_high() \n
			INTRO_CMD_HELP: Queries the measured value of the data rate of one of the following: \n
			- External transport stream including null packets input at 'User 1' connector
			- External transport stream including null packets input at 'IP Data/LAN' connector (TSoverIP)
		The value equals the sum of useful data rate rmeas and the rate of null packets r0: rmeas = rmeas + r0 \n
			:return: meas_drhp: float Range: 0 to 9999999999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:INPut:DATarate:HIGH?')
		return Conversions.str_to_float(response)
