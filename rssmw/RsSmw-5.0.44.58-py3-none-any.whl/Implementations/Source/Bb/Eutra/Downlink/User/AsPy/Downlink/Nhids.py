from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nhids:
	"""Nhids commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nhids", core, parent)

	def set(self, num_harq_ids: int, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:AS:DL:NHIDs \n
		Snippet: driver.source.bb.eutra.downlink.user.asPy.downlink.nhids.set(num_harq_ids = 1, userIx = repcap.UserIx.Default) \n
		Sets the number of HARQ process IDs. \n
			:param num_harq_ids: integer Range: 1 to 15
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.decimal_value_to_str(num_harq_ids)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:AS:DL:NHIDs {param}')

	def get(self, userIx=repcap.UserIx.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:AS:DL:NHIDs \n
		Snippet: value: int = driver.source.bb.eutra.downlink.user.asPy.downlink.nhids.get(userIx = repcap.UserIx.Default) \n
		Sets the number of HARQ process IDs. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: num_harq_ids: integer Range: 1 to 15"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:AS:DL:NHIDs?')
		return Conversions.str_to_int(response)
