from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RbOffset:
	"""RbOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbOffset", core, parent)

	def set(self, rb_offset: int, userEquipment=repcap.UserEquipment.Default, subframeNull=repcap.SubframeNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:PRACh:SUBF<CH0>:RBOFfset \n
		Snippet: driver.source.bb.eutra.uplink.ue.prach.subf.rbOffset.set(rb_offset = 1, userEquipment = repcap.UserEquipment.Default, subframeNull = repcap.SubframeNull.Default) \n
		Queries the starting RB, as set with the command [:SOURce<hw>]:BB:EUTRa:UL:PRACh:FOFFset. \n
			:param rb_offset: integer Range: 0 to 109
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
		"""
		param = Conversions.decimal_value_to_str(rb_offset)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:PRACh:SUBF{subframeNull_cmd_val}:RBOFfset {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default, subframeNull=repcap.SubframeNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:PRACh:SUBF<CH0>:RBOFfset \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.prach.subf.rbOffset.get(userEquipment = repcap.UserEquipment.Default, subframeNull = repcap.SubframeNull.Default) \n
		Queries the starting RB, as set with the command [:SOURce<hw>]:BB:EUTRa:UL:PRACh:FOFFset. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:return: rb_offset: integer Range: 0 to 109"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:PRACh:SUBF{subframeNull_cmd_val}:RBOFfset?')
		return Conversions.str_to_int(response)
