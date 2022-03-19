from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FromPy:
	"""FromPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fromPy", core, parent)

	def set(self, freq_corr_iq_po_fro: int, index=repcap.Index.Default) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:SLISt<CH>:PORTs:FROM \n
		Snippet: driver.source.correction.fresponse.iq.user.slist.ports.fromPy.set(freq_corr_iq_po_fro = 1, index = repcap.Index.Default) \n
		No command help available \n
			:param freq_corr_iq_po_fro: No help available
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slist')
		"""
		param = Conversions.decimal_value_to_str(freq_corr_iq_po_fro)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:SLISt{index_cmd_val}:PORTs:FROM {param}')

	def get(self, index=repcap.Index.Default) -> int:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:SLISt<CH>:PORTs:FROM \n
		Snippet: value: int = driver.source.correction.fresponse.iq.user.slist.ports.fromPy.get(index = repcap.Index.Default) \n
		No command help available \n
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Slist')
			:return: freq_corr_iq_po_fro: No help available"""
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:SLISt{index_cmd_val}:PORTs:FROM?')
		return Conversions.str_to_int(response)
