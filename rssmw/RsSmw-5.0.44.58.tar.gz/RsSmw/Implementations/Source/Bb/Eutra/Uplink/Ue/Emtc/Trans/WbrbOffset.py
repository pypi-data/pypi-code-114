from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class WbrbOffset:
	"""WbrbOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wbrbOffset", core, parent)

	def set(self, wideband_rb_offset: enums.EutraEmtcVrbOffs, userEquipment=repcap.UserEquipment.Default, transmission=repcap.Transmission.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:EMTC:TRANs<CH>:WBRBoffset \n
		Snippet: driver.source.bb.eutra.uplink.ue.emtc.trans.wbrbOffset.set(wideband_rb_offset = enums.EutraEmtcVrbOffs.OS0, userEquipment = repcap.UserEquipment.Default, transmission = repcap.Transmission.Default) \n
		Shifts the selected number of resource blocks within the wideband. \n
			:param wideband_rb_offset: OS0| OS3| OS6| OS9| OS12| OS15| OS18| OS21
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param transmission: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trans')
		"""
		param = Conversions.enum_scalar_to_str(wideband_rb_offset, enums.EutraEmtcVrbOffs)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		transmission_cmd_val = self._cmd_group.get_repcap_cmd_value(transmission, repcap.Transmission)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:EMTC:TRANs{transmission_cmd_val}:WBRBoffset {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default, transmission=repcap.Transmission.Default) -> enums.EutraEmtcVrbOffs:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:EMTC:TRANs<CH>:WBRBoffset \n
		Snippet: value: enums.EutraEmtcVrbOffs = driver.source.bb.eutra.uplink.ue.emtc.trans.wbrbOffset.get(userEquipment = repcap.UserEquipment.Default, transmission = repcap.Transmission.Default) \n
		Shifts the selected number of resource blocks within the wideband. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param transmission: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trans')
			:return: wideband_rb_offset: OS0| OS3| OS6| OS9| OS12| OS15| OS18| OS21"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		transmission_cmd_val = self._cmd_group.get_repcap_cmd_value(transmission, repcap.Transmission)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:EMTC:TRANs{transmission_cmd_val}:WBRBoffset?')
		return Conversions.str_to_scalar_enum(response, enums.EutraEmtcVrbOffs)
