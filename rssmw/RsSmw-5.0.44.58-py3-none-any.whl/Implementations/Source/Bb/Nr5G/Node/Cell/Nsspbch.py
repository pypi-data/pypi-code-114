from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nsspbch:
	"""Nsspbch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nsspbch", core, parent)

	def set(self, nu_of_pbch_pattern: int, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:NSSPbch \n
		Snippet: driver.source.bb.nr5G.node.cell.nsspbch.set(nu_of_pbch_pattern = 1, cellNull = repcap.CellNull.Nr0) \n
		Sets the number of SS/PBCH patterns to be configured. \n
			:param nu_of_pbch_pattern: integer Range: 0 to 4
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.decimal_value_to_str(nu_of_pbch_pattern)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:NSSPbch {param}')

	def get(self, cellNull=repcap.CellNull.Nr0) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:NSSPbch \n
		Snippet: value: int = driver.source.bb.nr5G.node.cell.nsspbch.get(cellNull = repcap.CellNull.Nr0) \n
		Sets the number of SS/PBCH patterns to be configured. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: nu_of_pbch_pattern: integer Range: 0 to 4"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:NSSPbch?')
		return Conversions.str_to_int(response)
