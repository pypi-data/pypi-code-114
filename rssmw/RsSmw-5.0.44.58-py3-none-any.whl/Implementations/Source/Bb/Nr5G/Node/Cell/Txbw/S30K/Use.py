from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Use:
	"""Use commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("use", core, parent)

	def set(self, scs_use: bool, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:TXBW:S30K:USE \n
		Snippet: driver.source.bb.nr5G.node.cell.txbw.s30K.use.set(scs_use = False, cellNull = repcap.CellNull.Nr0) \n
		Enables an SCS in the particular cell. \n
			:param scs_use: 1| ON| 0| OFF
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.bool_to_str(scs_use)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:TXBW:S30K:USE {param}')

	def get(self, cellNull=repcap.CellNull.Nr0) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:TXBW:S30K:USE \n
		Snippet: value: bool = driver.source.bb.nr5G.node.cell.txbw.s30K.use.get(cellNull = repcap.CellNull.Nr0) \n
		Enables an SCS in the particular cell. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: scs_use: 1| ON| 0| OFF"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:TXBW:S30K:USE?')
		return Conversions.str_to_bool(response)
