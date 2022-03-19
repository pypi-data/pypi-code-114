from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import enums
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Layer:
	"""Layer commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("layer", core, parent)

	def set(self, layer: enums.EnhBitErr, mobileStation=repcap.MobileStation.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPCCh:E:FRC:DERRor:BIT:LAYer \n
		Snippet: driver.source.bb.w3Gpp.mstation.hsupa.dpcch.e.frc.derror.bit.layer.set(layer = enums.EnhBitErr.PHYSical, mobileStation = repcap.MobileStation.Default) \n
		The command sets the layer in the coding process at which bit errors are inserted. \n
			:param layer: TRANsport| PHYSical
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
		"""
		param = Conversions.enum_scalar_to_str(layer, enums.EnhBitErr)
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPCCh:E:FRC:DERRor:BIT:LAYer {param}')

	# noinspection PyTypeChecker
	def get(self, mobileStation=repcap.MobileStation.Default) -> enums.EnhBitErr:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation<ST>:[HSUPa]:DPCCh:E:FRC:DERRor:BIT:LAYer \n
		Snippet: value: enums.EnhBitErr = driver.source.bb.w3Gpp.mstation.hsupa.dpcch.e.frc.derror.bit.layer.get(mobileStation = repcap.MobileStation.Default) \n
		The command sets the layer in the coding process at which bit errors are inserted. \n
			:param mobileStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mstation')
			:return: layer: TRANsport| PHYSical"""
		mobileStation_cmd_val = self._cmd_group.get_repcap_cmd_value(mobileStation, repcap.MobileStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:MSTation{mobileStation_cmd_val}:HSUPa:DPCCh:E:FRC:DERRor:BIT:LAYer?')
		return Conversions.str_to_scalar_enum(response, enums.EnhBitErr)
