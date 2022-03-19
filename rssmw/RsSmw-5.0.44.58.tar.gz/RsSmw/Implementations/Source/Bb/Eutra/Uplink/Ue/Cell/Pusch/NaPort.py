from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NaPort:
	"""NaPort commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("naPort", core, parent)

	def set(self, num_aps: enums.NumberOfPorts, userEquipment=repcap.UserEquipment.Default, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:[CELL<CCIDX>]:PUSCh:NAPort \n
		Snippet: driver.source.bb.eutra.uplink.ue.cell.pusch.naPort.set(num_aps = enums.NumberOfPorts.AP1, userEquipment = repcap.UserEquipment.Default, cellNull = repcap.CellNull.Default) \n
		Sets the number of antenna ports for PUSCH transmission.
		Use the command [:SOURce<hw>]:BB:EUTRa:UL[:CELL<ccidx>][:SUBF<st0>]:ALLoc<ch0>:PUSCh:PRECoding:NAPused to query the
		number of used antenna ports. \n
			:param num_aps: AP1 | AP2 | AP4
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(num_aps, enums.NumberOfPorts)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:CELL{cellNull_cmd_val}:PUSCh:NAPort {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default, cellNull=repcap.CellNull.Default) -> enums.NumberOfPorts:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:[CELL<CCIDX>]:PUSCh:NAPort \n
		Snippet: value: enums.NumberOfPorts = driver.source.bb.eutra.uplink.ue.cell.pusch.naPort.get(userEquipment = repcap.UserEquipment.Default, cellNull = repcap.CellNull.Default) \n
		Sets the number of antenna ports for PUSCH transmission.
		Use the command [:SOURce<hw>]:BB:EUTRa:UL[:CELL<ccidx>][:SUBF<st0>]:ALLoc<ch0>:PUSCh:PRECoding:NAPused to query the
		number of used antenna ports. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: num_aps: AP1 | AP2 | AP4"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:CELL{cellNull_cmd_val}:PUSCh:NAPort?')
		return Conversions.str_to_scalar_enum(response, enums.NumberOfPorts)
