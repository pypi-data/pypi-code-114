from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Read:
	"""Read commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("read", core, parent)

	def set(self, read: enums.TpcReadMode, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation<ST>:TPC:READ \n
		Snippet: driver.source.bb.c2K.mstation.tpc.read.set(read = enums.TpcReadMode.CONTinuous, mobileStation = repcap.MobileStation.Default) \n
		The command sets the read out mode for the bit pattern of the power control bits. The bit pattern is defined with the
		commands BB:C2K:MST<n>:TPC.... \n
			:param read: CONTinuous| S0A| S1A| S01A| S10A CONTinuous The bit pattern is used cyclically. S0A The bit pattern is used once, then the power control bit sequence continues with 0 bits. S1A The bit pattern is used once, then the power control bit sequence continues with 1 bit. S01A The bit pattern is used once and then the power control bit sequence is continued with 0 bits and 1 bit alternately. S10A The bit pattern is used once and then the power control bit sequence is continued with 1 bit and 0 bits alternately.
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(read, enums.TpcReadMode)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:C2K:MSTation{mobileStation_cmd_val}:TPC:READ {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.TpcReadMode:
		"""SCPI: [SOURce<HW>]:BB:C2K:MSTation<ST>:TPC:READ \n
		Snippet: value: enums.TpcReadMode = driver.source.bb.c2K.mstation.tpc.read.get(mobileStation = repcap.MobileStation.Default) \n
		The command sets the read out mode for the bit pattern of the power control bits. The bit pattern is defined with the
		commands BB:C2K:MST<n>:TPC.... \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: read: CONTinuous| S0A| S1A| S01A| S10A CONTinuous The bit pattern is used cyclically. S0A The bit pattern is used once, then the power control bit sequence continues with 0 bits. S1A The bit pattern is used once, then the power control bit sequence continues with 1 bit. S01A The bit pattern is used once and then the power control bit sequence is continued with 0 bits and 1 bit alternately. S10A The bit pattern is used once and then the power control bit sequence is continued with 1 bit and 0 bits alternately."""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:C2K:MSTation{mobileStation_cmd_val}:TPC:READ?')
		return Conversions.str_to_scalar_enum(response, enums.TpcReadMode)
