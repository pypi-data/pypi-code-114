from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mcs:
	"""Mcs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcs", core, parent)

	def set(self, mcs_table: enums.EutraMcsTable, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:CELL<ST0>:MCS \n
		Snippet: driver.source.bb.eutra.downlink.user.cell.mcs.set(mcs_table = enums.EutraMcsTable._0, userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default) \n
		Defines which of the tables defined in is used to specify the used modulation and coding scheme. \n
			:param mcs_table: 0| OFF| T1| 1| ON| T2| T3| T4 0|OFF|T1 Table 7.1.7.1-1 1|ON|T2 Table 7.1.7.1-1A T3 Table 7.1.7.1-1B T4 Table 7.1.7.1-1C
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(mcs_table, enums.EutraMcsTable)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:CELL{cellNull_cmd_val}:MCS {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default, cellNull=repcap.CellNull.Default) -> enums.EutraMcsTable:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:CELL<ST0>:MCS \n
		Snippet: value: enums.EutraMcsTable = driver.source.bb.eutra.downlink.user.cell.mcs.get(userIx = repcap.UserIx.Default, cellNull = repcap.CellNull.Default) \n
		Defines which of the tables defined in is used to specify the used modulation and coding scheme. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: mcs_table: 0| OFF| T1| 1| ON| T2| T3| T4 0|OFF|T1 Table 7.1.7.1-1 1|ON|T2 Table 7.1.7.1-1A T3 Table 7.1.7.1-1B T4 Table 7.1.7.1-1C"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:CELL{cellNull_cmd_val}:MCS?')
		return Conversions.str_to_scalar_enum(response, enums.EutraMcsTable)
