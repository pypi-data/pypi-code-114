from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rbid:
	"""Rbid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbid", core, parent)

	def set(self, rb_index: int, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:PRACh:NIOT:RBID \n
		Snippet: driver.source.bb.eutra.uplink.ue.prach.niot.rbid.set(rb_index = 1, userEquipment = repcap.UserEquipment.Default) \n
		Sets the resource block in that the NPRACH is allocated. \n
			:param rb_index: integer Range: 0 to 100
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.decimal_value_to_str(rb_index)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:PRACh:NIOT:RBID {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:PRACh:NIOT:RBID \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.prach.niot.rbid.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the resource block in that the NPRACH is allocated. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: rb_index: integer Range: 0 to 100"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:PRACh:NIOT:RBID?')
		return Conversions.str_to_int(response)
