from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Channel:
	"""Channel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("channel", core, parent)

	def set(self, channel: enums.HsUpaFrcMode, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPCCh:E:FRC:CHANnel \n
		Snippet: driver.source.bb.w3Gpp.mstation.hsupa.dpcch.e.frc.channel.set(channel = enums.HsUpaFrcMode._1, mobileStation = repcap.MobileStation.Default) \n
		The command sets the FRC according to TS 25.141 Annex A.10. Selection of FRC#8 is enabled only for instruments equipped
		with option SMW-K83. \n
			:param channel: USER| 1| 2| 3| 4| 5| 6| 7| 8
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(channel, enums.HsUpaFrcMode)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPCCh:E:FRC:CHANnel {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.HsUpaFrcMode:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPCCh:E:FRC:CHANnel \n
		Snippet: value: enums.HsUpaFrcMode = driver.source.bb.w3Gpp.mstation.hsupa.dpcch.e.frc.channel.get(mobileStation = repcap.MobileStation.Default) \n
		The command sets the FRC according to TS 25.141 Annex A.10. Selection of FRC#8 is enabled only for instruments equipped
		with option SMW-K83. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: channel: USER| 1| 2| 3| 4| 5| 6| 7| 8"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPCCh:E:FRC:CHANnel?')
		return Conversions.str_to_scalar_enum(response, enums.HsUpaFrcMode)
