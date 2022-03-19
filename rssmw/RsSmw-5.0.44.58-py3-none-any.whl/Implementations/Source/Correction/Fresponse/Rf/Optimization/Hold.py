from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hold:
	"""Hold commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hold", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:OPTimization:HOLD:[STATe] \n
		Snippet: value: bool = driver.source.correction.fresponse.rf.optimization.hold.get_state() \n
			INTRO_CMD_HELP: For [:SOURce<hw>]:CORRection:FRESponse:RF:OPTimization:MODEQHIG|QHT, retains the last calculated correction values as long as one of the following is performed: \n
			- SOURce1:CORRection:FRESponse:RF:OPTimization:HOLD:STATe 0
			- [:SOURce<hw>]:CORRection:FRESponse:RF:OPTimization:LOCal \n
			:return: freq_resp_hold_sta: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:RF:OPTimization:HOLD:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, freq_resp_hold_sta: bool) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:OPTimization:HOLD:[STATe] \n
		Snippet: driver.source.correction.fresponse.rf.optimization.hold.set_state(freq_resp_hold_sta = False) \n
			INTRO_CMD_HELP: For [:SOURce<hw>]:CORRection:FRESponse:RF:OPTimization:MODEQHIG|QHT, retains the last calculated correction values as long as one of the following is performed: \n
			- SOURce1:CORRection:FRESponse:RF:OPTimization:HOLD:STATe 0
			- [:SOURce<hw>]:CORRection:FRESponse:RF:OPTimization:LOCal \n
			:param freq_resp_hold_sta: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(freq_resp_hold_sta)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:RF:OPTimization:HOLD:STATe {param}')
