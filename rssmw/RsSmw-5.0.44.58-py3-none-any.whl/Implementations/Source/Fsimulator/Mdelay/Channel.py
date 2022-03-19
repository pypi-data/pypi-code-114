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
	def get_mode(self) -> enums.FadMpRopChanMode:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:CHANnel:MODE \n
		Snippet: value: enums.FadMpRopChanMode = driver.source.fsimulator.mdelay.channel.get_mode() \n
		Determines whether only one or several moving channels are simulated. \n
			:return: mode: ONE| ALL
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MDELay:CHANnel:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FadMpRopChanMode)

	def set_mode(self, mode: enums.FadMpRopChanMode) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MDELay:CHANnel:MODE \n
		Snippet: driver.source.fsimulator.mdelay.channel.set_mode(mode = enums.FadMpRopChanMode.ALL) \n
		Determines whether only one or several moving channels are simulated. \n
			:param mode: ONE| ALL
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FadMpRopChanMode)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MDELay:CHANnel:MODE {param}')
