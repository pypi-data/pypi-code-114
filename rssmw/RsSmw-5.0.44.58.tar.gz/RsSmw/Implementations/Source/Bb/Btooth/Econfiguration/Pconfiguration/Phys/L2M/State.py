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

	def set(self, state: bool, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:PHYS:L2M<CH0>:STATe \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.phys.l2M.state.set(state = False, channelNull = repcap.ChannelNull.Default) \n
		Specifies the physical layers for which the Peripheral has a minimum number of used channels requirement. Information is
		signaled via LL_MIN_USED_CHANNELS_IND.
			INTRO_CMD_HELP: You can enable one or more PHYs: \n
			- L1M for LE uncoded 1 Msymbol/s PHY.
			- L2M for LE uncoded 2 Msymbol/s PHY.
			- LCOD for LE coded 1 Msymbol/s PHY. \n
			:param state: 1| ON| 0| OFF
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'L2M')
		"""
		param = Conversions.bool_to_str(state)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:PHYS:L2M{channelNull_cmd_val}:STATe {param}')

	def get(self, channelNull=repcap.ChannelNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:PHYS:L2M<CH0>:STATe \n
		Snippet: value: bool = driver.source.bb.btooth.econfiguration.pconfiguration.phys.l2M.state.get(channelNull = repcap.ChannelNull.Default) \n
		Specifies the physical layers for which the Peripheral has a minimum number of used channels requirement. Information is
		signaled via LL_MIN_USED_CHANNELS_IND.
			INTRO_CMD_HELP: You can enable one or more PHYs: \n
			- L1M for LE uncoded 1 Msymbol/s PHY.
			- L2M for LE uncoded 2 Msymbol/s PHY.
			- LCOD for LE coded 1 Msymbol/s PHY. \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'L2M')
			:return: state: 1| ON| 0| OFF"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:PHYS:L2M{channelNull_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
