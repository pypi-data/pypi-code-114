from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.TpcMode, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:TPC:MODE \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.tpc.mode.set(mode = enums.TpcMode.D2B, mobileStation = repcap.MobileStation.Default) \n
		Selects the TPC (Transmit Power Control) mode.
		The command sets the slot format ([:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:SFORmat) in conjunction with the set TFCI
		status ([:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:TFCI:STATe) and the FBI Mode
		([:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:FBI:MODE) to the associated values. \n
			:param mode: D2B| D4B D2B A TPC field with a length of 2 bits is used. D4B (enabled only for instruments equipped with R&S SMW-K83) A TPC field with a length of 4 bits is used. A 4 bits long TPC field can be selected, only for Slot Format 4 and disabled FBI and TFCI fields.
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.TpcMode)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:TPC:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.TpcMode:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:TPC:MODE \n
		Snippet: value: enums.TpcMode = driver.source.bb.w3Gpp.mstation.dpcch.tpc.mode.get(mobileStation = repcap.MobileStation.Default) \n
		Selects the TPC (Transmit Power Control) mode.
		The command sets the slot format ([:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:SFORmat) in conjunction with the set TFCI
		status ([:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:TFCI:STATe) and the FBI Mode
		([:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:FBI:MODE) to the associated values. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: mode: D2B| D4B D2B A TPC field with a length of 2 bits is used. D4B (enabled only for instruments equipped with R&S SMW-K83) A TPC field with a length of 4 bits is used. A 4 bits long TPC field can be selected, only for Slot Format 4 and disabled FBI and TFCI fields."""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:TPC:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.TpcMode)
