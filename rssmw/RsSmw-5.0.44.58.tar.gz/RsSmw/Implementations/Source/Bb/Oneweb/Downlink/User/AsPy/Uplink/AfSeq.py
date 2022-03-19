from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AfSeq:
	"""AfSeq commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("afSeq", core, parent)

	def set(self, autofill_seq: bool, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:USER<CH>:AS:UL:AFSeq \n
		Snippet: driver.source.bb.oneweb.downlink.user.asPy.uplink.afSeq.set(autofill_seq = False, userIx = repcap.UserIx.Default) \n
		No command help available \n
			:param autofill_seq: No help available
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.bool_to_str(autofill_seq)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:USER{userIx_cmd_val}:AS:UL:AFSeq {param}')

	def get(self, userIx=repcap.UserIx.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:USER<CH>:AS:UL:AFSeq \n
		Snippet: value: bool = driver.source.bb.oneweb.downlink.user.asPy.uplink.afSeq.get(userIx = repcap.UserIx.Default) \n
		No command help available \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: autofill_seq: No help available"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:DL:USER{userIx_cmd_val}:AS:UL:AFSeq?')
		return Conversions.str_to_bool(response)
