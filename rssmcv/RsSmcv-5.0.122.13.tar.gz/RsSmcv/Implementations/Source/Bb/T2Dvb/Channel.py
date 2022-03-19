from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Channel:
	"""Channel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("channel", core, parent)

	# noinspection PyTypeChecker
	def get_bandwidth(self) -> enums.Dvbt2FramingChannelBandwidth:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:CHANnel:[BANDwidth] \n
		Snippet: value: enums.Dvbt2FramingChannelBandwidth = driver.source.bb.t2Dvb.channel.get_bandwidth() \n
		Selects the channel bandwidth. \n
			:return: channel_bw: BW_2| BW_5| BW_6| BW_7| BW_8
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:CHANnel:BANDwidth?')
		return Conversions.str_to_scalar_enum(response, enums.Dvbt2FramingChannelBandwidth)

	def set_bandwidth(self, channel_bw: enums.Dvbt2FramingChannelBandwidth) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:CHANnel:[BANDwidth] \n
		Snippet: driver.source.bb.t2Dvb.channel.set_bandwidth(channel_bw = enums.Dvbt2FramingChannelBandwidth.BW_2) \n
		Selects the channel bandwidth. \n
			:param channel_bw: BW_2| BW_5| BW_6| BW_7| BW_8
		"""
		param = Conversions.enum_scalar_to_str(channel_bw, enums.Dvbt2FramingChannelBandwidth)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:CHANnel:BANDwidth {param}')
