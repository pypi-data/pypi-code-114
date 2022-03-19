from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	def set(self, modulation: enums.HsUpaMod, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPCCh:E:FRC:MODulation \n
		Snippet: driver.source.bb.w3Gpp.mstation.hsupa.dpcch.e.frc.modulation.set(modulation = enums.HsUpaMod.BPSK, mobileStation = repcap.MobileStation.Default) \n
		Sets the modulation used for the selected FRC. Two modulation schemes are defined: BPSK for FRC 1 - 7 and 4PAM (4
		Pulse-Amplitude Modulation) for FRC 8. \n
			:param modulation: BPSK| PAM4
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(modulation, enums.HsUpaMod)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPCCh:E:FRC:MODulation {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.HsUpaMod:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPCCh:E:FRC:MODulation \n
		Snippet: value: enums.HsUpaMod = driver.source.bb.w3Gpp.mstation.hsupa.dpcch.e.frc.modulation.get(mobileStation = repcap.MobileStation.Default) \n
		Sets the modulation used for the selected FRC. Two modulation schemes are defined: BPSK for FRC 1 - 7 and 4PAM (4
		Pulse-Amplitude Modulation) for FRC 8. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: modulation: BPSK| PAM4"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPCCh:E:FRC:MODulation?')
		return Conversions.str_to_scalar_enum(response, enums.HsUpaMod)
