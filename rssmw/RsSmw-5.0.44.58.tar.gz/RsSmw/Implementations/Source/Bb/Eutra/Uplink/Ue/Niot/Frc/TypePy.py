from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, frc_id: enums.FrcTypeAll, userEquipment=repcap.UserEquipment.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:NIOT:FRC:TYPE \n
		Snippet: driver.source.bb.eutra.uplink.ue.niot.frc.typePy.set(frc_id = enums.FrcTypeAll.A141, userEquipment = repcap.UserEquipment.Default) \n
		Selects the FRC. \n
			:param frc_id: A141| A142| A143| A151| A144| A152| A161| A162| A163| A164| A165| A241| A242| A243| A244| A245| A246| A247
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
		"""
		param = Conversions.enum_scalar_to_str(frc_id, enums.FrcTypeAll)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:NIOT:FRC:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default) -> enums.FrcTypeAll:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:NIOT:FRC:TYPE \n
		Snippet: value: enums.FrcTypeAll = driver.source.bb.eutra.uplink.ue.niot.frc.typePy.get(userEquipment = repcap.UserEquipment.Default) \n
		Selects the FRC. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:return: frc_id: A141| A142| A143| A151| A144| A152| A161| A162| A163| A164| A165| A241| A242| A243| A244| A245| A246| A247"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:NIOT:FRC:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.FrcTypeAll)
