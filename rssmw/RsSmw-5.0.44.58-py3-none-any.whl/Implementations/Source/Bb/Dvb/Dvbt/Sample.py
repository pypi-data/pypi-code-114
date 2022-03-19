from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sample:
	"""Sample commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sample", core, parent)

	def get_length(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBT:SAMPle:LENGth \n
		Snippet: value: int = driver.source.bb.dvb.dvbt.sample.get_length() \n
		Queries the number of the transmitted samples. \n
			:return: length: integer
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBT:SAMPle:LENGth?')
		return Conversions.str_to_int(response)

	def get_rate(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBT:SAMPle:RATE \n
		Snippet: value: float = driver.source.bb.dvb.dvbt.sample.get_rate() \n
		Queries the sample rate. \n
			:return: rate: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVB:DVBT:SAMPle:RATE?')
		return Conversions.str_to_float(response)
