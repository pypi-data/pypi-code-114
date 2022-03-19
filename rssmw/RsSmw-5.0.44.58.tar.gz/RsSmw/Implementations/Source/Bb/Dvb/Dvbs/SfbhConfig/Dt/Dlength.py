from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dlength:
	"""Dlength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dlength", core, parent)

	def set(self, dwell_length: int, channelNull=repcap.ChannelNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFBHconfig:DT<CH0>:DLENgth \n
		Snippet: driver.source.bb.dvb.dvbs.sfbhConfig.dt.dlength.set(dwell_length = 1, channelNull = repcap.ChannelNull.Default) \n
		No command help available \n
			:param dwell_length: No help available
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Dt')
		"""
		param = Conversions.decimal_value_to_str(dwell_length)
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVB:DVBS:SFBHconfig:DT{channelNull_cmd_val}:DLENgth {param}')

	def get(self, channelNull=repcap.ChannelNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:DVB:DVBS:SFBHconfig:DT<CH0>:DLENgth \n
		Snippet: value: int = driver.source.bb.dvb.dvbs.sfbhConfig.dt.dlength.get(channelNull = repcap.ChannelNull.Default) \n
		No command help available \n
			:param channelNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Dt')
			:return: dwell_length: No help available"""
		channelNull_cmd_val = self._cmd_group.get_repcap_cmd_value(channelNull, repcap.ChannelNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DVB:DVBS:SFBHconfig:DT{channelNull_cmd_val}:DLENgth?')
		return Conversions.str_to_int(response)
