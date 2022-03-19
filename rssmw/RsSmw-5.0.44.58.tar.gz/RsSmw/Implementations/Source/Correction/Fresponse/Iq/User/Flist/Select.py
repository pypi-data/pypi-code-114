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

	def set(self, freq_corr_iq_flsel: str, index=repcap.Index.Default) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:FLISt<CH>:SELect \n
		Snippet: driver.source.correction.fresponse.iq.user.flist.select.set(freq_corr_iq_flsel = '1', index = repcap.Index.Default) \n
		No command help available \n
			:param freq_corr_iq_flsel: No help available
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Flist')
		"""
		param = Conversions.value_to_quoted_str(freq_corr_iq_flsel)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:FLISt{index_cmd_val}:SELect {param}')

	def get(self, index=repcap.Index.Default) -> str:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:FLISt<CH>:SELect \n
		Snippet: value: str = driver.source.correction.fresponse.iq.user.flist.select.get(index = repcap.Index.Default) \n
		No command help available \n
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Flist')
			:return: freq_corr_iq_flsel: No help available"""
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:FLISt{index_cmd_val}:SELect?')
		return trim_str_response(response)
