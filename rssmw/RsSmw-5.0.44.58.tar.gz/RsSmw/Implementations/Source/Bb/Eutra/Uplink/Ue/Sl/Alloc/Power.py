from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def set(self, power: float, userEquipment=repcap.UserEquipment.Default, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:ALLoc<CH0>:POWer \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.alloc.power.set(power = 1.0, userEquipment = repcap.UserEquipment.Default, allocationNull = repcap.AllocationNull.Default) \n
		Sets the power of the selected channel. \n
			:param power: float Range: -80 to 10
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(power)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:ALLoc{allocationNull_cmd_val}:POWer {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default, allocationNull=repcap.AllocationNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:ALLoc<CH0>:POWer \n
		Snippet: value: float = driver.source.bb.eutra.uplink.ue.sl.alloc.power.get(userEquipment = repcap.UserEquipment.Default, allocationNull = repcap.AllocationNull.Default) \n
		Sets the power of the selected channel. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: power: float Range: -80 to 10"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:ALLoc{allocationNull_cmd_val}:POWer?')
		return Conversions.str_to_float(response)
