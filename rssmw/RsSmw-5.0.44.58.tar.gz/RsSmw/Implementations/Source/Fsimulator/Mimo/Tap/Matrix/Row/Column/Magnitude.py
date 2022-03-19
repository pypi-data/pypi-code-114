from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Magnitude:
	"""Magnitude commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("magnitude", core, parent)

	def set(self, magnitude: float, mimoTap=repcap.MimoTap.Default, row=repcap.Row.Default, column=repcap.Column.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:TAP<CH>:MATRix:ROW<DI>:COLumn<ST>:MAGNitude \n
		Snippet: driver.source.fsimulator.mimo.tap.matrix.row.column.magnitude.set(magnitude = 1.0, mimoTap = repcap.MimoTap.Default, row = repcap.Row.Default, column = repcap.Column.Default) \n
		Determines the value for the real/magnitude part of the correlation. \n
			:param magnitude: float Range: 0 to 1
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
			:param row: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Row')
			:param column: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Column')
		"""
		param = Conversions.decimal_value_to_str(magnitude)
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		row_cmd_val = self._cmd_group.get_repcap_cmd_value(row, repcap.Row)
		column_cmd_val = self._cmd_group.get_repcap_cmd_value(column, repcap.Column)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:TAP{mimoTap_cmd_val}:MATRix:ROW{row_cmd_val}:COLumn{column_cmd_val}:MAGNitude {param}')

	def get(self, mimoTap=repcap.MimoTap.Default, row=repcap.Row.Default, column=repcap.Column.Default) -> float:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:TAP<CH>:MATRix:ROW<DI>:COLumn<ST>:MAGNitude \n
		Snippet: value: float = driver.source.fsimulator.mimo.tap.matrix.row.column.magnitude.get(mimoTap = repcap.MimoTap.Default, row = repcap.Row.Default, column = repcap.Column.Default) \n
		Determines the value for the real/magnitude part of the correlation. \n
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')
			:param row: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Row')
			:param column: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Column')
			:return: magnitude: float Range: 0 to 1"""
		mimoTap_cmd_val = self._cmd_group.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		row_cmd_val = self._cmd_group.get_repcap_cmd_value(row, repcap.Row)
		column_cmd_val = self._cmd_group.get_repcap_cmd_value(column, repcap.Column)
		response = self._core.io.query_str(f'SOURce<HwInstance>:FSIMulator:MIMO:TAP{mimoTap_cmd_val}:MATRix:ROW{row_cmd_val}:COLumn{column_cmd_val}:MAGNitude?')
		return Conversions.str_to_float(response)
