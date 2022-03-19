from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nktc:
	"""Nktc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nktc", core, parent)

	def set(self, tran_comb_num_ktc: enums.NumbersD, userEquipment=repcap.UserEquipment.Default, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:[CELL<CCIDX>]:REFSig:SRS:NKTC \n
		Snippet: driver.source.bb.eutra.uplink.ue.cell.refsig.srs.nktc.set(tran_comb_num_ktc = enums.NumbersD._2, userEquipment = repcap.UserEquipment.Default, cellNull = repcap.CellNull.Default) \n
		In TDD mode, sets the UE-specific parameter number of combs (transmissionCombNum) . \n
			:param tran_comb_num_ktc: 2| 4
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(tran_comb_num_ktc, enums.NumbersD)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:CELL{cellNull_cmd_val}:REFSig:SRS:NKTC {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default, cellNull=repcap.CellNull.Default) -> enums.NumbersD:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:[CELL<CCIDX>]:REFSig:SRS:NKTC \n
		Snippet: value: enums.NumbersD = driver.source.bb.eutra.uplink.ue.cell.refsig.srs.nktc.get(userEquipment = repcap.UserEquipment.Default, cellNull = repcap.CellNull.Default) \n
		In TDD mode, sets the UE-specific parameter number of combs (transmissionCombNum) . \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: tran_comb_num_ktc: 2| 4"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:CELL{cellNull_cmd_val}:REFSig:SRS:NKTC?')
		return Conversions.str_to_scalar_enum(response, enums.NumbersD)
