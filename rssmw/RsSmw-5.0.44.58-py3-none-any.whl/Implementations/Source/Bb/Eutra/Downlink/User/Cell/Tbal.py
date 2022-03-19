from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tbal:
	"""Tbal commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tbal", core, parent)

	def set(self, tbs_alt_index: enums.EutraMcsTable, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:CELL<ST0>:TBAL \n
		Snippet: driver.source.bb.eutra.downlink.user.cell.tbal.set(tbs_alt_index = enums.EutraMcsTable._0, userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default) \n
		Sets the which of the transport block size (TBS) tables defined in is used. \n
			:param tbs_alt_index: 0| OFF| T1| 1| ON| T2| T3| T4 0|OFF|T1 ='TBS Alt. Index = 0' 1|ON|T2 = 'TBS Alt. Index = 1' T3 = 'TBS Alt. Index = 2' T3 = 'TBS Alt. Index = 3'
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(tbs_alt_index, enums.EutraMcsTable)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:CELL{cellNull_cmd_val}:TBAL {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default) -> enums.EutraMcsTable:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:CELL<ST0>:TBAL \n
		Snippet: value: enums.EutraMcsTable = driver.source.bb.eutra.downlink.user.cell.tbal.get(userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default) \n
		Sets the which of the transport block size (TBS) tables defined in is used. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: tbs_alt_index: 0| OFF| T1| 1| ON| T2| T3| T4 0|OFF|T1 ='TBS Alt. Index = 0' 1|ON|T2 = 'TBS Alt. Index = 1' T3 = 'TBS Alt. Index = 2' T3 = 'TBS Alt. Index = 3'"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:CELL{cellNull_cmd_val}:TBAL?')
		return Conversions.str_to_scalar_enum(response, enums.EutraMcsTable)
