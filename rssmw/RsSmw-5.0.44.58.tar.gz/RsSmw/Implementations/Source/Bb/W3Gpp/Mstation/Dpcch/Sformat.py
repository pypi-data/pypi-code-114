from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sformat:
	"""Sformat commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sformat", core, parent)

	def set(self, sformat: int, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:SFORmat \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.sformat.set(sformat = 1, mobileStation = repcap.MobileStation.Default) \n
		The command sets the slot format for the DPCCH. The slot format defines the structure of the DPCCH slots and the control
		fields. Slot Format # 4 is available only for instruments equipped with R&S SMW-K83. Slot formats 0 to 4 are available
		for the DPCCH channel as defined in the 3GPP Release 7 specification TS 25.211. Note: The former slot formats 4 and 5
		according to 3GPP Release 4 specification TS 25.211 are not supported any more. The command sets the FBI mode
		([:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:FBI:MODE) ,
		the TFCI status ([:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:TFCI:STATe) and the TPC Mode
		([:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:TPC:MODE) to the associated values. \n
			:param sformat: integer Range: 0 to 4
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(sformat)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:SFORmat {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:SFORmat \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.dpcch.sformat.get(mobileStation = repcap.MobileStation.Default) \n
		The command sets the slot format for the DPCCH. The slot format defines the structure of the DPCCH slots and the control
		fields. Slot Format # 4 is available only for instruments equipped with R&S SMW-K83. Slot formats 0 to 4 are available
		for the DPCCH channel as defined in the 3GPP Release 7 specification TS 25.211. Note: The former slot formats 4 and 5
		according to 3GPP Release 4 specification TS 25.211 are not supported any more. The command sets the FBI mode
		([:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:FBI:MODE) ,
		the TFCI status ([:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:TFCI:STATe) and the TPC Mode
		([:SOURce<hw>]:BB:W3GPp:MSTation<st>:DPCCh:TPC:MODE) to the associated values. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: sformat: integer Range: 0 to 4"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:SFORmat?')
		return Conversions.str_to_int(response)
