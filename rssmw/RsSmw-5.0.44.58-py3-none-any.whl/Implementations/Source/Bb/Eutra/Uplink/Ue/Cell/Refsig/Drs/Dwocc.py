from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dwocc:
	"""Dwocc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dwocc", core, parent)

	def set(self, dmrs_with_occ: bool, userEquipment=repcap.UserEquipment.Default, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:[CELL<CCIDX>]:REFSig:DRS:DWOCc \n
		Snippet: driver.source.bb.eutra.uplink.ue.cell.refsig.drs.dwocc.set(dmrs_with_occ = False, userEquipment = repcap.UserEquipment.Default, cellNull = repcap.CellNull.Default) \n
		For Release 10 UEs, activate demodulation reference signal (DMRS) with an orthogonal cover code (OCC) for one antenna
		port. \n
			:param dmrs_with_occ: 1| ON| 0| OFF
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.bool_to_str(dmrs_with_occ)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:CELL{cellNull_cmd_val}:REFSig:DRS:DWOCc {param}')

	def get(self, userEquipment=repcap.UserEquipment.Default, cellNull=repcap.CellNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:[CELL<CCIDX>]:REFSig:DRS:DWOCc \n
		Snippet: value: bool = driver.source.bb.eutra.uplink.ue.cell.refsig.drs.dwocc.get(userEquipment = repcap.UserEquipment.Default, cellNull = repcap.CellNull.Default) \n
		For Release 10 UEs, activate demodulation reference signal (DMRS) with an orthogonal cover code (OCC) for one antenna
		port. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: dmrs_with_occ: 1| ON| 0| OFF"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:CELL{cellNull_cmd_val}:REFSig:DRS:DWOCc?')
		return Conversions.str_to_bool(response)
