from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, tbs_alt_index_old: bool, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:TALTindex:STATe \n
		Snippet: driver.source.bb.eutra.downlink.user.taltIndex.state.set(tbs_alt_index_old = False, userIx = repcap.UserIx.Default) \n
		This command is supported for backwards compatibility. Use [:SOURce<hw>]:BB:EUTRa:DL:USER<ch>:CELL<st0>:TBAL instead. \n
			:param tbs_alt_index_old: 1| ON| 0| OFF
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.bool_to_str(tbs_alt_index_old)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:TALTindex:STATe {param}')

	def get(self, userIx=repcap.UserIx.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:TALTindex:STATe \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.user.taltIndex.state.get(userIx = repcap.UserIx.Default) \n
		This command is supported for backwards compatibility. Use [:SOURce<hw>]:BB:EUTRa:DL:USER<ch>:CELL<st0>:TBAL instead. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: tbs_alt_index_old: 1| ON| 0| OFF"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:TALTindex:STATe?')
		return Conversions.str_to_bool(response)
