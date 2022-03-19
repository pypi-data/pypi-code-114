from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.Cdma2KmsMode, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation<ST>:MODE \n
		Snippet: driver.source.bb.c2K.mstation.mode.set(mode = enums.Cdma2KmsMode.ACCess, mobileStation = repcap.MobileStation.Default) \n
		The command selects operating mode for the mobile station. The channel-specific parameters are set with commands
		SOUR:BB:C2K:MST<n>:CHANnel<n>:...n. \n
			:param mode: TRAFfic| ACCess| EACCess| CCONtrol TRAFfic The mobile station generates a single traffic channel A traffic channel consists of up to eight sub channels depending on the selected radio configuration (R-FCH, R-SCCH, R-SCH, R-DCCH) . This mode corresponds to the standard mode of a mobile station during voice and data transmission. ACCess The mobile station generates an access channel (R-ACH) . This channel is needed to set up the connection between the mobile station and the base station. EACCess The mobile station generates an enhanced access channel (R-ACH) and a pilot channel (R-PICH) . CCONtrol The mobile station generates a common control channel (R-ACH) and a pilot channel (R-PICH) .
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.Cdma2KmsMode)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:MSTation{mobileStation_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.Cdma2KmsMode:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation<ST>:MODE \n
		Snippet: value: enums.Cdma2KmsMode = driver.source.bb.c2K.mstation.mode.get(mobileStation = repcap.MobileStation.Default) \n
		The command selects operating mode for the mobile station. The channel-specific parameters are set with commands
		SOUR:BB:C2K:MST<n>:CHANnel<n>:...n. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: mode: TRAFfic| ACCess| EACCess| CCONtrol TRAFfic The mobile station generates a single traffic channel A traffic channel consists of up to eight sub channels depending on the selected radio configuration (R-FCH, R-SCCH, R-SCH, R-DCCH) . This mode corresponds to the standard mode of a mobile station during voice and data transmission. ACCess The mobile station generates an access channel (R-ACH) . This channel is needed to set up the connection between the mobile station and the base station. EACCess The mobile station generates an enhanced access channel (R-ACH) and a pilot channel (R-PICH) . CCONtrol The mobile station generates a common control channel (R-ACH) and a pilot channel (R-PICH) ."""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:MSTation{mobileStation_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.Cdma2KmsMode)
