from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Misuse:
	"""Misuse commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("misuse", core, parent)

	def set(self, misuse: bool, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:TPC:MISuse \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.tpc.misuse.set(misuse = False, mobileStation = repcap.MobileStation.Default) \n
		The command activates 'mis-' use of the TPC field (Transmit Power Control) for controlling the channel power of the user
		equipment. The bit pattern (see commands :SOURce:BB:W3GPp:MSTation:DPCCh:TPC:DATA...) of the TPC field of the DPCCH is
		used to control the channel power. A '1' leads to an increase of channel powers, a '0' to a reduction of channel powers.
		Channel power is limited to the range 0 dB to -60 dB. The step width for the change is defined by the command
		[:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:TPC:PSTep. Note: 'Mis-'using the TPC field is available for UE2, UE3,UE4 only. \n
			:param misuse: ON| OFF
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.bool_to_str(misuse)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:TPC:MISuse {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:TPC:MISuse \n
		Snippet: value: bool = driver.source.bb.w3Gpp.mstation.dpcch.tpc.misuse.get(mobileStation = repcap.MobileStation.Default) \n
		The command activates 'mis-' use of the TPC field (Transmit Power Control) for controlling the channel power of the user
		equipment. The bit pattern (see commands :SOURce:BB:W3GPp:MSTation:DPCCh:TPC:DATA...) of the TPC field of the DPCCH is
		used to control the channel power. A '1' leads to an increase of channel powers, a '0' to a reduction of channel powers.
		Channel power is limited to the range 0 dB to -60 dB. The step width for the change is defined by the command
		[:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:TPC:PSTep. Note: 'Mis-'using the TPC field is available for UE2, UE3,UE4 only. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: misuse: ON| OFF"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:TPC:MISuse?')
		return Conversions.str_to_bool(response)
