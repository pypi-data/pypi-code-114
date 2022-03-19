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

	def get(self, userEquipment=repcap.UserEquipment.Default, subframeNull=repcap.SubframeNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:UE<ST>:PRACh:SUBF<CH0>:RBOFfset \n
		Snippet: value: int = driver.source.bb.oneweb.uplink.ue.prach.subf.rbOffset.get(userEquipment = repcap.UserEquipment.Default, subframeNull = repcap.SubframeNull.Default) \n
		Queries the starting RB, as set with the command [:SOURce<hw>]:BB:ONEWeb:UL:UE<st>:PRACh:SUBF<ch0>:RBOFfset?. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:return: rb_offset: integer Range: 0 to 109"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:UL:UE{userEquipment_cmd_val}:PRACh:SUBF{subframeNull_cmd_val}:RBOFfset?')
		return Conversions.str_to_int(response)
