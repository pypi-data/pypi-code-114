from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import enums
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Adefinition:
	"""Adefinition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("adefinition", core, parent)

	def set(self, adefinition: enums.LowHigh, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPCCh:E:FRC:HARQ:SIMulation:ADEFinition \n
		Snippet: driver.source.bb.w3Gpp.mstation.hsupa.dpcch.e.frc.harq.simulation.adefinition.set(adefinition = enums.LowHigh.HIGH, mobileStation = repcap.MobileStation.Default) \n
		Selects whether a high level (TTL) is interpreted as an ACK or a low level. \n
			:param adefinition: HIGH| LOW
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(adefinition, enums.LowHigh)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPCCh:E:FRC:HARQ:SIMulation:ADEFinition {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.LowHigh:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPCCh:E:FRC:HARQ:SIMulation:ADEFinition \n
		Snippet: value: enums.LowHigh = driver.source.bb.w3Gpp.mstation.hsupa.dpcch.e.frc.harq.simulation.adefinition.get(mobileStation = repcap.MobileStation.Default) \n
		Selects whether a high level (TTL) is interpreted as an ACK or a low level. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: adefinition: HIGH| LOW"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPCCh:E:FRC:HARQ:SIMulation:ADEFinition?')
		return Conversions.str_to_scalar_enum(response, enums.LowHigh)
