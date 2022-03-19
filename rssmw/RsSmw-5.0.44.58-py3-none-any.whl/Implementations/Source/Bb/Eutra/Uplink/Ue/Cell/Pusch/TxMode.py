from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TxMode:
	"""TxMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("txMode", core, parent)

	def set(self, tx_mode: enums.PuschTxMode, userEquipment=repcap.UserEquipment.Default, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:[CELL<CCIDX>]:PUSCh:TXMode \n
		Snippet: driver.source.bb.eutra.uplink.ue.cell.pusch.txMode.set(tx_mode = enums.PuschTxMode.M1, userEquipment = repcap.UserEquipment.Default, cellNull = repcap.CellNull.Default) \n
		For LTE-A UEs, sets the PUSCH transmission mode according to . eMTC UEs support PUSCH transmission mode M1 only. \n
			:param tx_mode: M1| M2 M1 Spatial multiplexing not possible M2 Spatial multiplexing possible
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(tx_mode, enums.PuschTxMode)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:CELL{cellNull_cmd_val}:PUSCh:TXMode {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default, cellNull=repcap.CellNull.Default) -> enums.PuschTxMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:[CELL<CCIDX>]:PUSCh:TXMode \n
		Snippet: value: enums.PuschTxMode = driver.source.bb.eutra.uplink.ue.cell.pusch.txMode.get(userEquipment = repcap.UserEquipment.Default, cellNull = repcap.CellNull.Default) \n
		For LTE-A UEs, sets the PUSCH transmission mode according to . eMTC UEs support PUSCH transmission mode M1 only. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: tx_mode: M1| M2 M1 Spatial multiplexing not possible M2 Spatial multiplexing possible"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:CELL{cellNull_cmd_val}:PUSCh:TXMode?')
		return Conversions.str_to_scalar_enum(response, enums.PuschTxMode)
