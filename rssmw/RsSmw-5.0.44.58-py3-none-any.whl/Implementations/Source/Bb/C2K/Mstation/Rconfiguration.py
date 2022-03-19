from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rconfiguration:
	"""Rconfiguration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rconfiguration", core, parent)

	def set(self, rconfiguration: enums.Cdma2KradioConf, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation<ST>:RCONfiguration \n
		Snippet: driver.source.bb.c2K.mstation.rconfiguration.set(rconfiguration = enums.Cdma2KradioConf._1, mobileStation = repcap.MobileStation.Default) \n
		The command selects the radio configuration for the traffic channel. The settings of the channel table parameters are
		specific for the selected radio configuration. A separate set of settings of all channel table parameters for each radio
		configuration is provided. If the radio configuration is changed, the set of channel table values belonging to this RC is
		automatically activated. \n
			:param rconfiguration: 1| 2| 3| 4
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(rconfiguration, enums.Cdma2KradioConf)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:MSTation{mobileStation_cmd_val}:RCONfiguration {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.Cdma2KradioConf:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation<ST>:RCONfiguration \n
		Snippet: value: enums.Cdma2KradioConf = driver.source.bb.c2K.mstation.rconfiguration.get(mobileStation = repcap.MobileStation.Default) \n
		The command selects the radio configuration for the traffic channel. The settings of the channel table parameters are
		specific for the selected radio configuration. A separate set of settings of all channel table parameters for each radio
		configuration is provided. If the radio configuration is changed, the set of channel table values belonging to this RC is
		automatically activated. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: rconfiguration: 1| 2| 3| 4"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:MSTation{mobileStation_cmd_val}:RCONfiguration?')
		return Conversions.str_to_scalar_enum(response, enums.Cdma2KradioConf)
