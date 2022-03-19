from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nrepetitions:
	"""Nrepetitions commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nrepetitions", core, parent)

	def set(self, num_repetitions: int, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RDISc:NREPetitions \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.rdisc.nrepetitions.set(num_repetitions = 1, userEquipment = repcap.UserEquipment.Default) \n
		Sets the number of PSDCH repetitions. \n
			:param num_repetitions: integer Range: 1 to 50
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.decimal_value_to_str(num_repetitions)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RDISc:NREPetitions {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RDISc:NREPetitions \n
		Snippet: value: int = driver.source.bb.eutra.uplink.ue.sl.rdisc.nrepetitions.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the number of PSDCH repetitions. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: num_repetitions: integer Range: 1 to 50"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RDISc:NREPetitions?')
		return Conversions.str_to_int(response)
