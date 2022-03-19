from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mretransmissions:
	"""Mretransmissions commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mretransmissions", core, parent)

	def set(self, mretransmission: int, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPCCh:E:FRC:HARQ:SIMulation:MRETransmissions \n
		Snippet: driver.source.bb.w3Gpp.mstation.hsupa.dpcch.e.frc.harq.simulation.mretransmissions.set(mretransmission = 1, mobileStation = repcap.MobileStation.Default) \n
		Sets the maximum number of retransmissions. After the expiration of this value, the next packet is send, regardless of
		the received feedback. \n
			:param mretransmission: integer Range: 0 to 20
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.decimal_value_to_str(mretransmission)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPCCh:E:FRC:HARQ:SIMulation:MRETransmissions {param}')

	def get(self, mobileStation=repcap.MobileStation.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPCCh:E:FRC:HARQ:SIMulation:MRETransmissions \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.hsupa.dpcch.e.frc.harq.simulation.mretransmissions.get(mobileStation = repcap.MobileStation.Default) \n
		Sets the maximum number of retransmissions. After the expiration of this value, the next packet is send, regardless of
		the received feedback. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: mretransmission: integer Range: 0 to 20"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPCCh:E:FRC:HARQ:SIMulation:MRETransmissions?')
		return Conversions.str_to_int(response)
