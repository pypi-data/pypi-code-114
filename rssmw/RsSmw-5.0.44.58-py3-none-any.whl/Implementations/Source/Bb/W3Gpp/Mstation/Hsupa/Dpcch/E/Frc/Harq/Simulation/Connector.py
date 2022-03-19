from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import enums
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Connector:
	"""Connector commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("connector", core, parent)

	def set(self, connector: enums.FeedbackConnector, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPCCh:E:FRC:HARQ:SIMulation:CONNector \n
		Snippet: driver.source.bb.w3Gpp.mstation.hsupa.dpcch.e.frc.harq.simulation.connector.set(connector = enums.FeedbackConnector.GLOBal, mobileStation = repcap.MobileStation.Default) \n
		Determines the input connector at that the instrument expects the feedback signal. \n
			:param connector: LOCal| GLOBal
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(connector, enums.FeedbackConnector)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPCCh:E:FRC:HARQ:SIMulation:CONNector {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.FeedbackConnector:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPCCh:E:FRC:HARQ:SIMulation:CONNector \n
		Snippet: value: enums.FeedbackConnector = driver.source.bb.w3Gpp.mstation.hsupa.dpcch.e.frc.harq.simulation.connector.get(mobileStation = repcap.MobileStation.Default) \n
		Determines the input connector at that the instrument expects the feedback signal. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: connector: LOCal| GLOBal"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPCCh:E:FRC:HARQ:SIMulation:CONNector?')
		return Conversions.str_to_scalar_enum(response, enums.FeedbackConnector)
