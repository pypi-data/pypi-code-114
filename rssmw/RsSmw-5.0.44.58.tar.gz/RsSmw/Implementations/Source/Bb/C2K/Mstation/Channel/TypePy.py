from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default, channel=repcap.Channel.Default) -> enums.Cdma2KchanTypeUp:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation<ST>:CHANnel<CH>:TYPE \n
		Snippet: value: enums.Cdma2KchanTypeUp = driver.source.bb.c2K.mstation.channel.typePy.get(mobileStation = repcap.MobileStation.Default, channel = repcap.Channel.Default) \n
		The command queries the channel type. The channel type depends on the selected operating mode and, for the sub channels
		of the traffic channel, from the selected radio configuration. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Channel')
			:return: type_py: R-PICH| R-ACH| R-EACH| R-CCCH| R-DCCH| R-FCH| R-SCCH| R-SCH2| R-SCH1 R-ACH Access Channel. R-EACH Enhanced Access Channel R-CCCH Common Control Channel R-PICH Pilot Channel. R-DCCH Dedicated Control Channel R-FCH Fundamental Channel R-SCHx Supplemental Channel 1 | 2 R-SCCH Supplemental Control Channel"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:MSTation{mobileStation_cmd_val}:CHANnel{channel_cmd_val}:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.Cdma2KchanTypeUp)
