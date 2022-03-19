from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NnPrep:
	"""NnPrep commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nnPrep", core, parent)

	def set(self, no_npusch_rep: enums.EutraUlNoNpuschRepNbiotAll, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:NIOT:FRC:NNPRep \n
		Snippet: driver.source.bb.eutra.uplink.ue.niot.frc.nnPrep.set(no_npusch_rep = enums.EutraUlNoNpuschRepNbiotAll._1, userEquipment = repcap.UserEquipment.Default) \n
		Queries the number of NPUSCH repetitions. \n
			:param no_npusch_rep: 1| 2| 16| 64
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.enum_scalar_to_str(no_npusch_rep, enums.EutraUlNoNpuschRepNbiotAll)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:NIOT:FRC:NNPRep {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default) -> enums.EutraUlNoNpuschRepNbiotAll:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:NIOT:FRC:NNPRep \n
		Snippet: value: enums.EutraUlNoNpuschRepNbiotAll = driver.source.bb.eutra.uplink.ue.niot.frc.nnPrep.get(userEquipment = repcap.UserEquipment.Default) \n
		Queries the number of NPUSCH repetitions. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: no_npusch_rep: 1| 2| 16| 64"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:NIOT:FRC:NNPRep?')
		return Conversions.str_to_scalar_enum(response, enums.EutraUlNoNpuschRepNbiotAll)
