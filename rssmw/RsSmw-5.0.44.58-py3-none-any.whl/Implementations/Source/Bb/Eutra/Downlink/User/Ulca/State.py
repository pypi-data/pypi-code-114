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

	def set(self, cu_ul_ca_state: bool, userIx=repcap.UserIx.Default, ulCarriersNull=repcap.UlCarriersNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:ULCA<ST0>:STATe \n
		Snippet: driver.source.bb.eutra.downlink.user.ulca.state.set(cu_ul_ca_state = False, userIx = repcap.UserIx.Default, ulCarriersNull = repcap.UlCarriersNull.Default) \n
		Sets the state of the associated UL carriers, if carrier aggregation is enabled. \n
			:param cu_ul_ca_state: 1| ON| 0| OFF
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param ulCarriersNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Ulca')
		"""
		param = Conversions.bool_to_str(cu_ul_ca_state)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		ulCarriersNull_cmd_val = self._cmd_group.get_repcap_cmd_value(ulCarriersNull, repcap.UlCarriersNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:ULCA{ulCarriersNull_cmd_val}:STATe {param}')

	def get(self, userIx=repcap.UserIx.Default, ulCarriersNull=repcap.UlCarriersNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:ULCA<ST0>:STATe \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.user.ulca.state.get(userIx = repcap.UserIx.Default, ulCarriersNull = repcap.UlCarriersNull.Default) \n
		Sets the state of the associated UL carriers, if carrier aggregation is enabled. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param ulCarriersNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Ulca')
			:return: cu_ul_ca_state: 1| ON| 0| OFF"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		ulCarriersNull_cmd_val = self._cmd_group.get_repcap_cmd_value(ulCarriersNull, repcap.UlCarriersNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:ULCA{ulCarriersNull_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
