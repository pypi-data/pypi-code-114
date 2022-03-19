from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, tphys: bool, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:TPHYs:L2M<CH0>:STATe \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.tphys.l2M.state.set(tphys = False, channelNull = repcap.ChannelNull.Default) \n
		Specifies preferred physical layers in Rx (..:RPHYs:..) or Tx (..:TPHYs:..) direction. Information is signaled via
		LL_PHY_REQ and LL_PHY_RSP. You can enable one or more PHYs: L1M for LE uncoded 1 Msymbol/s PHY, L2M for LE uncoded 2
		Msymbol/s PHY, and LCOD for LE coded 1 Msymbol/s PHY. \n
			:param tphys: 1| ON| 0| OFF
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'L2M')
		"""
		param = Conversions.bool_to_str(tphys)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:TPHYs:L2M{channelNull_cmd_val}:STATe {param}')

	def get(self, channelNull=repcap.ChannelNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:TPHYs:L2M<CH0>:STATe \n
		Snippet: value: bool = driver.source.bb.btooth.econfiguration.pconfiguration.tphys.l2M.state.get(channelNull = repcap.ChannelNull.Default) \n
		Specifies preferred physical layers in Rx (..:RPHYs:..) or Tx (..:TPHYs:..) direction. Information is signaled via
		LL_PHY_REQ and LL_PHY_RSP. You can enable one or more PHYs: L1M for LE uncoded 1 Msymbol/s PHY, L2M for LE uncoded 2
		Msymbol/s PHY, and LCOD for LE coded 1 Msymbol/s PHY. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'L2M')
			:return: tphys: 1| ON| 0| OFF"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:TPHYs:L2M{channelNull_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
