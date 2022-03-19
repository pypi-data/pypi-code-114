from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nsubbands:
	"""Nsubbands commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nsubbands", core, parent)

	def set(self, num_subbands: enums.NumbersB, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RDATa:NSUBbands \n
		Snippet: driver.source.bb.eutra.uplink.ue.sl.rdata.nsubbands.set(num_subbands = enums.NumbersB._1, userEquipment = repcap.UserEquipment.Default) \n
		Sets the number of subbands. \n
			:param num_subbands: 1| 2| 4
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.enum_scalar_to_str(num_subbands, enums.NumbersB)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RDATa:NSUBbands {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default) -> enums.NumbersB:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:SL:RDATa:NSUBbands \n
		Snippet: value: enums.NumbersB = driver.source.bb.eutra.uplink.ue.sl.rdata.nsubbands.get(userEquipment = repcap.UserEquipment.Default) \n
		Sets the number of subbands. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: num_subbands: 1| 2| 4"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:SL:RDATa:NSUBbands?')
		return Conversions.str_to_scalar_enum(response, enums.NumbersB)
