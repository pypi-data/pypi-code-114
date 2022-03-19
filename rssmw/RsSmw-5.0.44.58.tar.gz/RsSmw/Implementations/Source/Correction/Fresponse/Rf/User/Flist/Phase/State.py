from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, freq_corr_rf_ph_sta: bool, index=repcap.Index.Default) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:FLISt<CH>:PHASe:[STATe] \n
		Snippet: driver.source.correction.fresponse.rf.user.flist.phase.state.set(freq_corr_rf_ph_sta = False, index = repcap.Index.Default) \n
		Enables that the magnitude and/or phase values from the selected file are used for frequency response compensation.
		To trigger calculation of the correction values, send the command [:SOURce<hw>]:CORRection:FRESponse:RF:USER:APPLy.
		Otherwise changes are not considered. \n
			:param freq_corr_rf_ph_sta: 1| ON| 0| OFF
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Flist')
		"""
		param = Conversions.bool_to_str(freq_corr_rf_ph_sta)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:RF:USER:FLISt{index_cmd_val}:PHASe:STATe {param}')

	def get(self, index=repcap.Index.Default) -> bool:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:FLISt<CH>:PHASe:[STATe] \n
		Snippet: value: bool = driver.source.correction.fresponse.rf.user.flist.phase.state.get(index = repcap.Index.Default) \n
		Enables that the magnitude and/or phase values from the selected file are used for frequency response compensation.
		To trigger calculation of the correction values, send the command [:SOURce<hw>]:CORRection:FRESponse:RF:USER:APPLy.
		Otherwise changes are not considered. \n
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Flist')
			:return: freq_corr_rf_ph_sta: No help available"""
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce<HwInstance>:CORRection:FRESponse:RF:USER:FLISt{index_cmd_val}:PHASe:STATe?')
		return Conversions.str_to_bool(response)
