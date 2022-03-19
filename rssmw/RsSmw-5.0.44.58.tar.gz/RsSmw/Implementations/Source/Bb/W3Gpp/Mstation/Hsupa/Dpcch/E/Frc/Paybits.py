from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Paybits:
	"""Paybits commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("paybits", core, parent)

	def get(self, mobileStation=repcap.MobileStation.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPCCh:E:FRC:PAYBits \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.hsupa.dpcch.e.frc.paybits.get(mobileStation = repcap.MobileStation.Default) \n
		The command queries the payload of the information bit. This value determines the number of transport layer bits sent in
		each HARQ process. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: paybits: integer"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPCCh:E:FRC:PAYBits?')
		return Conversions.str_to_int(response)
