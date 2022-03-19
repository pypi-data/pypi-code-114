from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, freq_corr_iq_sl_sel: str, index=repcap.Index.Default) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:SLISt<CH>:SELect \n
		Snippet: driver.source.correction.fresponse.iq.user.slist.select.set(freq_corr_iq_sl_sel = '1', index = repcap.Index.Default) \n
		No command help available \n
			:param freq_corr_iq_sl_sel: No help available
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slist')
		"""
		param = Conversions.value_to_quoted_str(freq_corr_iq_sl_sel)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:SLISt{index_cmd_val}:SELect {param}')

	def get(self, index=repcap.Index.Default) -> str:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:SLISt<CH>:SELect \n
		Snippet: value: str = driver.source.correction.fresponse.iq.user.slist.select.get(index = repcap.Index.Default) \n
		No command help available \n
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slist')
			:return: freq_corr_iq_sl_sel: No help available"""
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:SLISt{index_cmd_val}:SELect?')
		return trim_str_response(response)
