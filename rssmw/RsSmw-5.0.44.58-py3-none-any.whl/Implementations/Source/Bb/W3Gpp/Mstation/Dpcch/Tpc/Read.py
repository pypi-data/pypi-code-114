from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Read:
	"""Read commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("read", core, parent)

	def set(self, read: enums.TpcReadMode, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:TPC:READ \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.tpc.read.set(read = enums.TpcReadMode.CONTinuous, mobileStation = repcap.MobileStation.Default) \n
		The command sets the read out mode for the bit pattern of the TPC field of the DPCCH. The bit pattern is selected with
		the command SOUR:BB:W3GPp:MST:DPCC:TPC:DATA:PATT. \n
			:param read: CONTinuous| S0A| S1A| S01A| S10A CONTinuous The bit pattern is used cyclically. S0A The bit pattern is used once, then the TPC sequence continues with 0 bits. S1A The bit pattern is used once, then the TPC sequence continues with 1 bit. S01A The bit pattern is used once and then the TPC sequence is continued with 0 bits and 1 bit alternately (in multiples, depending on by the symbol rate, for example, 00001111) . S10A The bit pattern is used once and then the TPC sequence is continued with 1 bit and 0 bits alternately (in multiples, depending on by the symbol rate, for example, 11110000) .
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(read, enums.TpcReadMode)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:TPC:READ {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.TpcReadMode:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:TPC:READ \n
		Snippet: value: enums.TpcReadMode = driver.source.bb.w3Gpp.mstation.dpcch.tpc.read.get(mobileStation = repcap.MobileStation.Default) \n
		The command sets the read out mode for the bit pattern of the TPC field of the DPCCH. The bit pattern is selected with
		the command SOUR:BB:W3GPp:MST:DPCC:TPC:DATA:PATT. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: read: CONTinuous| S0A| S1A| S01A| S10A CONTinuous The bit pattern is used cyclically. S0A The bit pattern is used once, then the TPC sequence continues with 0 bits. S1A The bit pattern is used once, then the TPC sequence continues with 1 bit. S01A The bit pattern is used once and then the TPC sequence is continued with 0 bits and 1 bit alternately (in multiples, depending on by the symbol rate, for example, 00001111) . S10A The bit pattern is used once and then the TPC sequence is continued with 1 bit and 0 bits alternately (in multiples, depending on by the symbol rate, for example, 11110000) ."""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:TPC:READ?')
		return Conversions.str_to_scalar_enum(response, enums.TpcReadMode)
