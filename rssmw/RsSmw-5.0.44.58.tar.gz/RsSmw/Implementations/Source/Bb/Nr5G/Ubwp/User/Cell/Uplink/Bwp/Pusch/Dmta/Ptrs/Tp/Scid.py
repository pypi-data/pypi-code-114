from ..............Internal.Core import Core
from ..............Internal.CommandsGroup import CommandsGroup
from ..............Internal import Conversions
from .............. import enums
from .............. import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scid:
	"""Scid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scid", core, parent)

	def set(self, tp_ptrs_scram_id: enums.NrsIdAll, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:UL:BWP<DIR0>:PUSCh:DMTA:PTRS:TP:SCID \n
		Snippet: driver.source.bb.nr5G.ubwp.user.cell.uplink.bwp.pusch.dmta.ptrs.tp.scid.set(tp_ptrs_scram_id = enums.NrsIdAll.CID, userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default) \n
		Sets whether the PTRS Scrambling ID value used for PTRS sequence generation is configured by the 'NPusch ID' (higher
		layer) or by the cell ID. \n
			:param tp_ptrs_scram_id: CID| PUID CID Sets the cell ID as the scrambling ID for PTRS sequence generation. PUID Sets the 'NPusch ID' as the scrambling ID for PTRS sequence generation.
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
		"""
		param = Conversions.enum_scalar_to_str(tp_ptrs_scram_id, enums.NrsIdAll)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:UL:BWP{bwPartNull_cmd_val}:PUSCh:DMTA:PTRS:TP:SCID {param}')

	# noinspection PyTypeChecker
	def get(self, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default) -> enums.NrsIdAll:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:UL:BWP<DIR0>:PUSCh:DMTA:PTRS:TP:SCID \n
		Snippet: value: enums.NrsIdAll = driver.source.bb.nr5G.ubwp.user.cell.uplink.bwp.pusch.dmta.ptrs.tp.scid.get(userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default) \n
		Sets whether the PTRS Scrambling ID value used for PTRS sequence generation is configured by the 'NPusch ID' (higher
		layer) or by the cell ID. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
			:return: tp_ptrs_scram_id: CID| PUID CID Sets the cell ID as the scrambling ID for PTRS sequence generation. PUID Sets the 'NPusch ID' as the scrambling ID for PTRS sequence generation."""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:UL:BWP{bwPartNull_cmd_val}:PUSCh:DMTA:PTRS:TP:SCID?')
		return Conversions.str_to_scalar_enum(response, enums.NrsIdAll)
