from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pow:
	"""Pow commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pow", core, parent)

	def set(self, csi_rs_pow: float, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:CSIS:[CELL<CH0>]:POW \n
		Snippet: driver.source.bb.v5G.downlink.csis.cell.pow.set(csi_rs_pow = 1.0, cellNull = repcap.CellNull.Default) \n
		Boosts the CSI-RS power compared to the cell-specific reference signals. \n
			:param csi_rs_pow: float Range: -8 to 15
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(csi_rs_pow)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:CSIS:CELL{cellNull_cmd_val}:POW {param}')

	def get(self, cellNull=repcap.CellNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:CSIS:[CELL<CH0>]:POW \n
		Snippet: value: float = driver.source.bb.v5G.downlink.csis.cell.pow.get(cellNull = repcap.CellNull.Default) \n
		Boosts the CSI-RS power compared to the cell-specific reference signals. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: csi_rs_pow: float Range: -8 to 15"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:V5G:DL:CSIS:CELL{cellNull_cmd_val}:POW?')
		return Conversions.str_to_float(response)
