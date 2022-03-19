from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class F5Naport:
	"""F5Naport commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("f5Naport", core, parent)

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default) -> enums.PucchNumAp:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:PUCCh:F5Naport \n
		Snippet: value: enums.PucchNumAp = driver.source.bb.eutra.uplink.ue.pucch.f5Naport.get(userEquipment = repcap.UserEquipment.Default) \n
		For LTE-A UEs, sets the number of antenna ports used for every PUCCH format transmission. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: pucch_f_5_num_aps: No help available"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:PUCCh:F5Naport?')
		return Conversions.str_to_scalar_enum(response, enums.PucchNumAp)
