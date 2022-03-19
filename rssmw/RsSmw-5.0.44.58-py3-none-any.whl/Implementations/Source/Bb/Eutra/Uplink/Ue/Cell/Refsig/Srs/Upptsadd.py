from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Upptsadd:
	"""Upptsadd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("upptsadd", core, parent)

	def set(self, srs_up_pts_add: enums.EutraNumUpPts, userEquipment=repcap.UserEquipment.Default, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:[CELL<CCIDX>]:REFSig:SRS:UPPTsadd \n
		Snippet: driver.source.bb.eutra.uplink.ue.cell.refsig.srs.upptsadd.set(srs_up_pts_add = enums.EutraNumUpPts._0, userEquipment = repcap.UserEquipment.Default, cellNull = repcap.CellNull.Default) \n
		In TDD mode, sets the parameter srs-UpPtsAdd and defines the number of additional SC-FDMA symbols in UpPTS. \n
			:param srs_up_pts_add: 0| 2| 4
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(srs_up_pts_add, enums.EutraNumUpPts)
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:CELL{cellNull_cmd_val}:REFSig:SRS:UPPTsadd {param}')

	# noinspection PyTypeChecker
	def get(self, userEquipment=repcap.UserEquipment.Default, cellNull=repcap.CellNull.Default) -> enums.EutraNumUpPts:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:UE<ST>:[CELL<CCIDX>]:REFSig:SRS:UPPTsadd \n
		Snippet: value: enums.EutraNumUpPts = driver.source.bb.eutra.uplink.ue.cell.refsig.srs.upptsadd.get(userEquipment = repcap.UserEquipment.Default, cellNull = repcap.CellNull.Default) \n
		In TDD mode, sets the parameter srs-UpPtsAdd and defines the number of additional SC-FDMA symbols in UpPTS. \n
			:param userEquipment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ue')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: srs_up_pts_add: 0| 2| 4"""
		userEquipment_cmd_val = self._cmd_group.get_repcap_cmd_value(userEquipment, repcap.UserEquipment)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:UE{userEquipment_cmd_val}:CELL{cellNull_cmd_val}:REFSig:SRS:UPPTsadd?')
		return Conversions.str_to_scalar_enum(response, enums.EutraNumUpPts)
