from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import enums
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.HsUpaHsimMode, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPCCh:E:FRC:HARQ:SIMulation:MODE \n
		Snippet: driver.source.bb.w3Gpp.mstation.hsupa.dpcch.e.frc.harq.simulation.mode.set(mode = enums.HsUpaHsimMode.HFEedback, mobileStation = repcap.MobileStation.Default) \n
		Selects the HARQ simulation mode. \n
			:param mode: VHARq | HFEedback VHARq Simulates basestation feedback. HFEedback Allows to control the transmission of the HSUPA fixed reference channels dynamically.
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.HsUpaHsimMode)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPCCh:E:FRC:HARQ:SIMulation:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.HsUpaHsimMode:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPCCh:E:FRC:HARQ:SIMulation:MODE \n
		Snippet: value: enums.HsUpaHsimMode = driver.source.bb.w3Gpp.mstation.hsupa.dpcch.e.frc.harq.simulation.mode.get(mobileStation = repcap.MobileStation.Default) \n
		Selects the HARQ simulation mode. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: mode: VHARq | HFEedback VHARq Simulates basestation feedback. HFEedback Allows to control the transmission of the HSUPA fixed reference channels dynamically."""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPCCh:E:FRC:HARQ:SIMulation:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.HsUpaHsimMode)
