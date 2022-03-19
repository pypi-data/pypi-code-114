from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SrbSubchan:
	"""SrbSubchan commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("srbSubchan", core, parent)

	def set(self, start_rb_subchan: int, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:V2X:SRBSubchan \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.v2X.srbSubchan.set(start_rb_subchan = 1, userEquipment = repcap.UserEquipment.Default) \n
		Sets the first RB in the subchannel. \n
			:param start_rb_subchan: integer Range: 0 to 99
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.decimal_value_to_str(start_rb_subchan)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:V2X:SRBSubchan {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:V2X:SRBSubchan \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.sl.v2X.srbSubchan.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the first RB in the subchannel. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: start_rb_subchan: integer Range: 0 to 99"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:V2X:SRBSubchan?')
		return Conversions.str_to_int(response)
