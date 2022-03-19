from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.ChanCodMode, userEquipment=repcap.UserEquipment.Default, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:[CELL<CCIDX>]:PUSCh:CCODing:MODE \n
		Snippet: driver.source.bb.eutra.uplink.ue.cell.pusch.ccoding.mode.set(mode = enums.ChanCodMode.COMBined, userEquipment = repcap.UserEquipment.Default, cellNull = repcap.CellNull.Default) \n
		Defines the information transmitted on the PUSCH. \n
			:param mode: COMBined| ULSChonly| UCIonly COMBined Control information and data are multiplexed into the PUSCH. ULSChonly Only data is transmitted on PUSCH. UCIonly Only uplink control information is transmitted on PUSCH.
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ChanCodMode)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:CELL{cellNull_cmd_val}:PUSCh:CCODing:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default, cellNull=repcap.CellNull.Default) -> enums.ChanCodMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:[CELL<CCIDX>]:PUSCh:CCODing:MODE \n
		Snippet: value: enums.ChanCodMode = driver.source.bb.eutra.uplink.ue.cell.pusch.ccoding.mode.get(userEquipment = repcap.UserEquipment.Default, cellNull = repcap.CellNull.Default) \n
		Defines the information transmitted on the PUSCH. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: mode: COMBined| ULSChonly| UCIonly COMBined Control information and data are multiplexed into the PUSCH. ULSChonly Only data is transmitted on PUSCH. UCIonly Only uplink control information is transmitted on PUSCH."""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:CELL{cellNull_cmd_val}:PUSCh:CCODing:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ChanCodMode)
