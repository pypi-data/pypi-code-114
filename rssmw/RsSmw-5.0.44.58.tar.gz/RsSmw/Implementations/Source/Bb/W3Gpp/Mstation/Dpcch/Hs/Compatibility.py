from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Compatibility:
	"""Compatibility commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("compatibility", core, parent)

	def set(self, compatibility: enums.HsCompatMode, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:COMPatibility \n
		Snippet: driver.source.bb.w3Gpp.mstation.dpcch.hs.compatibility.set(compatibility = enums.HsCompatMode.REL7, mobileStation = repcap.MobileStation.Default) \n
		The concept of the graphical user interface for the configuration of HS-DPCCH has been adapted to support simultaneous
		DC-HSDPA and MIMO operation, as required in 3GPP Release 9 onwards. This command enables the configuration of the
		HS-DPCCH settings provided for backwards compatibility (REL7) . \n
			:param compatibility: REL7| REL8 | REL8RT
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(compatibility, enums.HsCompatMode)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:COMPatibility {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.HsCompatMode:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:DPCCh:HS:COMPatibility \n
		Snippet: value: enums.HsCompatMode = driver.source.bb.w3Gpp.mstation.dpcch.hs.compatibility.get(mobileStation = repcap.MobileStation.Default) \n
		The concept of the graphical user interface for the configuration of HS-DPCCH has been adapted to support simultaneous
		DC-HSDPA and MIMO operation, as required in 3GPP Release 9 onwards. This command enables the configuration of the
		HS-DPCCH settings provided for backwards compatibility (REL7) . \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: compatibility: REL7| REL8 | REL8RT"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:DPCCh:HS:COMPatibility?')
		return Conversions.str_to_scalar_enum(response, enums.HsCompatMode)
