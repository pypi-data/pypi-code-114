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
	def get_bandwidth(self) -> enums.CodingChannelBandwidth:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:CHANnel:[BANDwidth] \n
		Snippet: value: enums.CodingChannelBandwidth = driver.source.bb.isdbt.channel.get_bandwidth() \n
		Selects the channel bandwidth. \n
			:return: channel_bw: BW_8| BW_6| BW_7
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ISDBt:CHANnel:BANDwidth?')
		return Conversions.str_to_scalar_enum(response, enums.CodingChannelBandwidth)

	def set_bandwidth(self, channel_bw: enums.CodingChannelBandwidth) -> None:
		"""SCPI: [SOURce<HW>]:BB:ISDBt:CHANnel:[BANDwidth] \n
		Snippet: driver.source.bb.isdbt.channel.set_bandwidth(channel_bw = enums.CodingChannelBandwidth.BW_6) \n
		Selects the channel bandwidth. \n
			:param channel_bw: BW_8| BW_6| BW_7
		"""
		param = Conversions.enum_scalar_to_str(channel_bw, enums.CodingChannelBandwidth)
		self._core.io.write(f'SOURce<HwInstance>:BB:ISDBt:CHANnel:BANDwidth {param}')
