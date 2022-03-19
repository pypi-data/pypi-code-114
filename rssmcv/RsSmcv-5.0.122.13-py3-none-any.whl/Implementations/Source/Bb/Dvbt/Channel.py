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
	def get_bandwidth(self) -> enums.DvbtCodingChannelBandwidth:
		"""SCPI: [SOURce<HW>]:BB:DVBT:CHANnel:[BANDwidth] \n
		Snippet: value: enums.DvbtCodingChannelBandwidth = driver.source.bb.dvbt.channel.get_bandwidth() \n
		Selects the channel bandwidth. \n
			:return: channel_bw: BW_Var| BW_8| BW_7| BW_5| BW_6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBT:CHANnel:BANDwidth?')
		return Conversions.str_to_scalar_enum(response, enums.DvbtCodingChannelBandwidth)

	def set_bandwidth(self, channel_bw: enums.DvbtCodingChannelBandwidth) -> None:
		"""SCPI: [SOURce<HW>]:BB:DVBT:CHANnel:[BANDwidth] \n
		Snippet: driver.source.bb.dvbt.channel.set_bandwidth(channel_bw = enums.DvbtCodingChannelBandwidth.BW_5) \n
		Selects the channel bandwidth. \n
			:param channel_bw: BW_Var| BW_8| BW_7| BW_5| BW_6
		"""
		param = Conversions.enum_scalar_to_str(channel_bw, enums.DvbtCodingChannelBandwidth)
		self._core.io.write(f'SOURce<HwInstance>:BB:DVBT:CHANnel:BANDwidth {param}')
