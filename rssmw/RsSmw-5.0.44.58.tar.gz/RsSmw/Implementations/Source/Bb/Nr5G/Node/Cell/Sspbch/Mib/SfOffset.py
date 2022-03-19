from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SfOffset:
	"""SfOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sfOffset", core, parent)

	def get(self, cellNull=repcap.CellNull.Nr0, ssPbchNull=repcap.SsPbchNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:SSPBch<ST0>:MIB:SFOFfset \n
		Snippet: value: int = driver.source.bb.nr5G.node.cell.sspbch.mib.sfOffset.get(cellNull = repcap.CellNull.Nr0, ssPbchNull = repcap.SsPbchNull.Default) \n
		By default, the counting of the SFN (system frame number) starts with 0. Use this parameter to set a different start SFN
		value. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:param ssPbchNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Sspbch')
			:return: ssp_bch_sf_start_of: integer Range: 0 to 1023"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		ssPbchNull_cmd_val = self._cmd_group.get_repcap_cmd_value(ssPbchNull, repcap.SsPbchNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:SSPBch{ssPbchNull_cmd_val}:MIB:SFOFfset?')
		return Conversions.str_to_int(response)
