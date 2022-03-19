from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SsfPeriod:
	"""SsfPeriod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ssfPeriod", core, parent)

	def set(self, start_sf_period: enums.IdEutraEmtcPrachStartingSfPeriod, ceLevel=repcap.CeLevel.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:EMTC:CELV<CH0>:SSFPeriod \n
		Snippet: driver.source.bb.eutra.uplink.prach.emtc.celv.ssfPeriod.set(start_sf_period = enums.IdEutraEmtcPrachStartingSfPeriod._128, ceLevel = repcap.CeLevel.Default) \n
		Sets the starting subframe periodicity. \n
			:param start_sf_period: NONE| 4| 2| 8| 16| 32| 64| 128| 256
			:param ceLevel: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Celv')
		"""
		param = Conversions.enum_scalar_to_str(start_sf_period, enums.IdEutraEmtcPrachStartingSfPeriod)
		ceLevel_cmd_val = self._cmd_group.get_repcap_cmd_value(ceLevel, repcap.CeLevel)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:EMTC:CELV{ceLevel_cmd_val}:SSFPeriod {param}')

	# noinspection PyTypeChecker
	def get(self, ceLevel=repcap.CeLevel.Default) -> enums.IdEutraEmtcPrachStartingSfPeriod:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:EMTC:CELV<CH0>:SSFPeriod \n
		Snippet: value: enums.IdEutraEmtcPrachStartingSfPeriod = driver.source.bb.eutra.uplink.prach.emtc.celv.ssfPeriod.get(ceLevel = repcap.CeLevel.Default) \n
		Sets the starting subframe periodicity. \n
			:param ceLevel: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Celv')
			:return: start_sf_period: NONE| 4| 2| 8| 16| 32| 64| 128| 256"""
		ceLevel_cmd_val = self._cmd_group.get_repcap_cmd_value(ceLevel, repcap.CeLevel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:EMTC:CELV{ceLevel_cmd_val}:SSFPeriod?')
		return Conversions.str_to_scalar_enum(response, enums.IdEutraEmtcPrachStartingSfPeriod)
