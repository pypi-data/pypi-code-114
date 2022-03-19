from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSignalling:
	"""RfSignalling commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfSignalling", core, parent)

	def get_frequency(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:L:RFSignalling:FREQuency \n
		Snippet: value: int = driver.source.bb.t2Dvb.lpy.rfSignalling.get_frequency() \n
		Queries the signaled frequency in the L1 signaling. \n
			:return: l_1_freq: integer Range: 0 to 4294967295, Unit: Hz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:L:RFSignalling:FREQuency?')
		return Conversions.str_to_int(response)

	def get_value(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:L:RFSignalling \n
		Snippet: value: bool = driver.source.bb.t2Dvb.lpy.rfSignalling.get_value() \n
		Queries the RF signaling state in L1.
			INTRO_CMD_HELP: The setting depends on the setting of the 'T2-MI Interface': \n
			- 'T2-MI Interface > Off': 0x0000 0000 is sent.
			- 'T2-MI Interface > On': The value from the T2-MI stream is sent. \n
			:return: rf_signalling: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:L:RFSignalling?')
		return Conversions.str_to_bool(response)

	def set_value(self, rf_signalling: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:L:RFSignalling \n
		Snippet: driver.source.bb.t2Dvb.lpy.rfSignalling.set_value(rf_signalling = False) \n
		Queries the RF signaling state in L1.
			INTRO_CMD_HELP: The setting depends on the setting of the 'T2-MI Interface': \n
			- 'T2-MI Interface > Off': 0x0000 0000 is sent.
			- 'T2-MI Interface > On': The value from the T2-MI stream is sent. \n
			:param rf_signalling: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(rf_signalling)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:L:RFSignalling {param}')
