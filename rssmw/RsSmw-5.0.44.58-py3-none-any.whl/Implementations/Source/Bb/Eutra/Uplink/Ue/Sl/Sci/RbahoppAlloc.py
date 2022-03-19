from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RbahoppAlloc:
	"""RbahoppAlloc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbahoppAlloc", core, parent)

	def set(self, rband_hopp_alloc: int, userEquipment=repcap.UserEquipment.Default, indexNull=repcap.IndexNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:SCI<CH0>:RBAHoppalloc \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.sci.rbahoppAlloc.set(rband_hopp_alloc = 1, userEquipment = repcap.UserEquipment.Default, indexNull = repcap.IndexNull.Default) \n
		Sets the DCI field resource block (RBA) and hopping resource allocation. This field identifies which resource blocks,
		within the subframes indicated by the time resource pattern ITRP, are used for PSSCH transmission. \n
			:param rband_hopp_alloc: integer Range: 0 to 8191
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Sci')
		"""
		param = Conversions.decimal_value_to_str(rband_hopp_alloc)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:SCI{indexNull_cmd_val}:RBAHoppalloc {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default, indexNull=repcap.IndexNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:SCI<CH0>:RBAHoppalloc \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.sl.sci.rbahoppAlloc.get(userEquipment = repcap.UserEquipment.Default, indexNull = repcap.IndexNull.Default) \n
		Sets the DCI field resource block (RBA) and hopping resource allocation. This field identifies which resource blocks,
		within the subframes indicated by the time resource pattern ITRP, are used for PSSCH transmission. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Sci')
			:return: rband_hopp_alloc: integer Range: 0 to 8191"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:SCI{indexNull_cmd_val}:RBAHoppalloc?')
		return Conversions.str_to_int(response)
