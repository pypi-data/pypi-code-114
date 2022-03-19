from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CycShift:
	"""CycShift commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cycShift", core, parent)

	def set(self, cyclic_shift: int, userEquipment=repcap.UserEquipment.Default, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:ALLoc<CH0>:CYCShift \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.alloc.cycShift.set(cyclic_shift = 1, userEquipment = repcap.UserEquipment.Default, allocationNull = repcap.AllocationNull.Default) \n
		Sets the cyclic shift used by the generation of the DRS (discovery reference signal) sequence. \n
			:param cyclic_shift: integer Value range depens on the sidelink mode. In communication mode, cyclic shift of 0 is used. In V2X communication mode, the value for PSCCH is one of the following {0, 3, 6, 9}. Range: 0 to 9
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(cyclic_shift)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:ALLoc{allocationNull_cmd_val}:CYCShift {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default, allocationNull=repcap.AllocationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:ALLoc<CH0>:CYCShift \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.sl.alloc.cycShift.get(userEquipment = repcap.UserEquipment.Default, allocationNull = repcap.AllocationNull.Default) \n
		Sets the cyclic shift used by the generation of the DRS (discovery reference signal) sequence. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: cyclic_shift: integer Value range depens on the sidelink mode. In communication mode, cyclic shift of 0 is used. In V2X communication mode, the value for PSCCH is one of the following {0, 3, 6, 9}. Range: 0 to 9"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:ALLoc{allocationNull_cmd_val}:CYCShift?')
		return Conversions.str_to_int(response)
