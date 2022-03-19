from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Imagin:
	"""Imagin commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("imagin", core, parent)

	def set(self, ant_mod_inv_mat_imag: float, row=repcap.Row.Default, column=repcap.Column.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:ANTenna:INVerse:MATRix:ROW<ST>:COLumn<CH>:IMAGin \n
		Snippet: driver.source.fsimulator.mimo.antenna.inverse.matrix.row.column.imagin.set(ant_mod_inv_mat_imag = 1.0, row = repcap.Row.Default, column = repcap.Column.Default) \n
		Sets the complex elements of the inverse channel matrix. \n
			:param ant_mod_inv_mat_imag: float Range: -1 to 1
			:param row: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Row')
			:param column: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Column')
		"""
		param = Conversions.decimal_value_to_str(ant_mod_inv_mat_imag)
		row_cmd_val = self._cmd_group.get_repcap_cmd_value(row, repcap.Row)
		column_cmd_val = self._cmd_group.get_repcap_cmd_value(column, repcap.Column)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:ANTenna:INVerse:MATRix:ROW{row_cmd_val}:COLumn{column_cmd_val}:IMAGin {param}')

	def get(self, row=repcap.Row.Default, column=repcap.Column.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:ANTenna:INVerse:MATRix:ROW<ST>:COLumn<CH>:IMAGin \n
		Snippet: value: float = driver.source.fsimulator.mimo.antenna.inverse.matrix.row.column.imagin.get(row = repcap.Row.Default, column = repcap.Column.Default) \n
		Sets the complex elements of the inverse channel matrix. \n
			:param row: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Row')
			:param column: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Column')
			:return: ant_mod_inv_mat_imag: float Range: -1 to 1"""
		row_cmd_val = self._cmd_group.get_repcap_cmd_value(row, repcap.Row)
		column_cmd_val = self._cmd_group.get_repcap_cmd_value(column, repcap.Column)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:MIMO:ANTenna:INVerse:MATRix:ROW{row_cmd_val}:COLumn{column_cmd_val}:IMAGin?')
		return Conversions.str_to_float(response)
