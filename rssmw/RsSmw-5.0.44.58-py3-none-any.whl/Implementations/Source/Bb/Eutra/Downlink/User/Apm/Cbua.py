from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cbua:
	"""Cbua commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cbua", core, parent)

	def set(self, cb_use_alt: bool, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:APM:CBUA \n
		Snippet: driver.source.bb.eutra.downlink.user.apm.cbua.set(cb_use_alt = False, userIx = repcap.UserIx.Default) \n
		Applies the enhanced 4 Tx codebook. \n
			:param cb_use_alt: 1| ON| 0| OFF OFF Tthe normal codebook is used. ON Applied is the enhanced 4Tx codebook.
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.bool_to_str(cb_use_alt)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:APM:CBUA {param}')

	def get(self, userIx=repcap.UserIx.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:APM:CBUA \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.user.apm.cbua.get(userIx = repcap.UserIx.Default) \n
		Applies the enhanced 4 Tx codebook. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: cb_use_alt: 1| ON| 0| OFF OFF Tthe normal codebook is used. ON Applied is the enhanced 4Tx codebook."""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:APM:CBUA?')
		return Conversions.str_to_bool(response)
