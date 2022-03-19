from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Npdsch:
	"""Npdsch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("npdsch", core, parent)

	def set(self, npsdch: int, userEquipment=repcap.UserEquipment.Default, allocationNull=repcap.AllocationNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:ALLoc<CH0>:NPDSch \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.alloc.npdsch.set(npsdch = 1, userEquipment = repcap.UserEquipment.Default, allocationNull = repcap.AllocationNull.Default) \n
			INTRO_CMD_HELP: In discovery mode and depending on the discovery type, sets one of the parameters: \n
			- n_PSDCH applies for discovery type 1
			- n' - for discovery type 2B. \n
			:param npsdch: integer Range: 0 to 2100
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(npsdch)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:ALLoc{allocationNull_cmd_val}:NPDSch {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default, allocationNull=repcap.AllocationNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:ALLoc<CH0>:NPDSch \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.sl.alloc.npdsch.get(userEquipment = repcap.UserEquipment.Default, allocationNull = repcap.AllocationNull.Default) \n
			INTRO_CMD_HELP: In discovery mode and depending on the discovery type, sets one of the parameters: \n
			- n_PSDCH applies for discovery type 1
			- n' - for discovery type 2B. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param allocationNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: npsdch: integer Range: 0 to 2100"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		allocationNull_cmd_val = self._cmd_group.get_repcap_cmd_value(allocationNull, repcap.AllocationNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:ALLoc{allocationNull_cmd_val}:NPDSch?')
		return Conversions.str_to_int(response)
