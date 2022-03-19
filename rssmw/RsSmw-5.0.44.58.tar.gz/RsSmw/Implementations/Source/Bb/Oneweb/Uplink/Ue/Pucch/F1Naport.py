from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class F1Naport:
	"""F1Naport commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("f1Naport", core, parent)

	def set(self, num_aps: enums.PucchNumAp, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:UE<ST>:PUCCh:F1Naport \n
		Snippet: driver.source.bb.oneweb.uplink.ue.pucch.f1Naport.set(num_aps = enums.PucchNumAp.AP1, userEquipment = repcap.UserEquipment.Default) \n
		No command help available \n
			:param num_aps: No help available
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.enum_scalar_to_str(num_aps, enums.PucchNumAp)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:UL:UE{userEquipment_cmd_val}:PUCCh:F1Naport {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default) -> enums.PucchNumAp:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:UL:UE<ST>:PUCCh:F1Naport \n
		Snippet: value: enums.PucchNumAp = driver.source.bb.oneweb.uplink.ue.pucch.f1Naport.get(userEquipment = repcap.UserEquipment.Default) \n
		No command help available \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: num_aps: No help available"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:UL:UE{userEquipment_cmd_val}:PUCCh:F1Naport?')
		return Conversions.str_to_scalar_enum(response, enums.PucchNumAp)
