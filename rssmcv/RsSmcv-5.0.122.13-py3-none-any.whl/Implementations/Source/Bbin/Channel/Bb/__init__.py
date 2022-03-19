from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bb:
	"""Bb commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bb", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, bbin_iq_hs_ch_bb: enums.BbDigInpBb, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BBIN:CHANnel<CH0>:BB \n
		Snippet: driver.source.bbin.channel.bb.set(bbin_iq_hs_ch_bb = enums.BbDigInpBb.A, channelNull = repcap.ChannelNull.Default) \n
		No command help available \n
			:param bbin_iq_hs_ch_bb: No help available
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
		"""
		param = Conversions.enum_scalar_to_str(bbin_iq_hs_ch_bb, enums.BbDigInpBb)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BBIN:CHANnel{channelNull_cmd_val}:BB {param}')

	# noinspection PyTypeChecker
	def get(self, channelNull=repcap.ChannelNull.Default) -> enums.BbDigInpBb:
		"""SCPI: [SOURce<HW>]:BBIN:CHANnel<CH0>:BB \n
		Snippet: value: enums.BbDigInpBb = driver.source.bbin.channel.bb.get(channelNull = repcap.ChannelNull.Default) \n
		No command help available \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Channel')
			:return: bbin_iq_hs_ch_bb: No help available"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BBIN:CHANnel{channelNull_cmd_val}:BB?')
		return Conversions.str_to_scalar_enum(response, enums.BbDigInpBb)

	def clone(self) -> 'Bb':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Bb(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
