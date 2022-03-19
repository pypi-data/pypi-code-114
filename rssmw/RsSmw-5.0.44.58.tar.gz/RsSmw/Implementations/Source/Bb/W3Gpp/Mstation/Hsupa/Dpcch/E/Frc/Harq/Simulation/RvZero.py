from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RvZero:
	"""RvZero commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rvZero", core, parent)

	def set(self, rv_zero: bool, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPCCh:E:FRC:HARQ:SIMulation:RVZero \n
		Snippet: driver.source.bb.w3Gpp.mstation.hsupa.dpcch.e.frc.harq.simulation.rvZero.set(rv_zero = False, mobileStation = repcap.MobileStation.Default) \n
		If activated, the same redundancy version is sent, that is, the redundancy version is not adjusted for the next
		retransmission in case of a received NACK. \n
			:param rv_zero: ON| OFF
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.bool_to_str(rv_zero)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPCCh:E:FRC:HARQ:SIMulation:RVZero {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPCCh:E:FRC:HARQ:SIMulation:RVZero \n
		Snippet: value: bool = driver.source.bb.w3Gpp.mstation.hsupa.dpcch.e.frc.harq.simulation.rvZero.get(mobileStation = repcap.MobileStation.Default) \n
		If activated, the same redundancy version is sent, that is, the redundancy version is not adjusted for the next
		retransmission in case of a received NACK. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: rv_zero: ON| OFF"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPCCh:E:FRC:HARQ:SIMulation:RVZero?')
		return Conversions.str_to_bool(response)
