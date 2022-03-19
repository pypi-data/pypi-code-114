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

	def set(self, rb_offset: int, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RDATa:RBOFfset \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.rdata.rbOffset.set(rb_offset = 1, userEquipment = repcap.UserEquipment.Default) \n
		Shifts the band in the frequency domain by the selected number of resource blocks (RB) . \n
			:param rb_offset: integer Range: 0 to 98
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.decimal_value_to_str(rb_offset)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RDATa:RBOFfset {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RDATa:RBOFfset \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.sl.rdata.rbOffset.get(userEquipment = repcap.UserEquipment.Default) \n
		Shifts the band in the frequency domain by the selected number of resource blocks (RB) . \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: rb_offset: integer Range: 0 to 98"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RDATa:RBOFfset?')
		return Conversions.str_to_int(response)
