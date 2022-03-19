from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Srelease:
	"""Srelease commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("srelease", core, parent)

	def set(self, usr_sps_rel_sub_frame: int, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:USER<CH>:SPS:SRELease \n
		Snippet: driver.source.bb.oneweb.downlink.user.sps.srelease.set(usr_sps_rel_sub_frame = 1, userIx = repcap.UserIx.Default) \n
		No command help available \n
			:param usr_sps_rel_sub_frame: No help available
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.decimal_value_to_str(usr_sps_rel_sub_frame)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:USER{userIx_cmd_val}:SPS:SRELease {param}')

	def get(self, userIx=repcap.UserIx.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:USER<CH>:SPS:SRELease \n
		Snippet: value: int = driver.source.bb.oneweb.downlink.user.sps.srelease.get(userIx = repcap.UserIx.Default) \n
		No command help available \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: usr_sps_rel_sub_frame: No help available"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:DL:USER{userIx_cmd_val}:SPS:SRELease?')
		return Conversions.str_to_int(response)
