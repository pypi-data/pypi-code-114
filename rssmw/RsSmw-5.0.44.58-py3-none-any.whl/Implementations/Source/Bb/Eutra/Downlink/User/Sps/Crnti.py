from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Crnti:
	"""Crnti commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("crnti", core, parent)

	def set(self, user_sps_crnti: int, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:SPS:CRNTi \n
		Snippet: driver.source.bb.eutra.downlink.user.sps.crnti.set(user_sps_crnti = 1, userIx = repcap.UserIx.Default) \n
		Sets the SPS C-RNTI parameter. \n
			:param user_sps_crnti: integer Range: 1 to 65523
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.decimal_value_to_str(user_sps_crnti)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:SPS:CRNTi {param}')

	def get(self, userIx=repcap.UserIx.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:SPS:CRNTi \n
		Snippet: value: int = driver.source.bb.eutra.downlink.user.sps.crnti.get(userIx = repcap.UserIx.Default) \n
		Sets the SPS C-RNTI parameter. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: user_sps_crnti: integer Range: 1 to 65523"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:SPS:CRNTi?')
		return Conversions.str_to_int(response)
