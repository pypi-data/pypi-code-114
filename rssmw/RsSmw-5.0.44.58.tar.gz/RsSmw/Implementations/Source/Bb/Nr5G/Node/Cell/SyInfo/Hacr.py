from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hacr:
	"""Hacr commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hacr", core, parent)

	def set(self, codebook_r_16: enums.AllHarqAckCbr16, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:SYINfo:HACR \n
		Snippet: driver.source.bb.nr5G.node.cell.syInfo.hacr.set(codebook_r_16 = enums.AllHarqAckCbr16.EDYN, cellNull = repcap.CellNull.Nr0) \n
		Defines the state of the higher layer parameter pdsch-HARQ-ACK-Codebook-r16. \n
			:param codebook_r_16: NCON| EDYN NCON Does not apply the release 16 codebook (not configured) . NCON Applies the release 16 codebook (enhanced dynamic) .
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.enum_scalar_to_str(codebook_r_16, enums.AllHarqAckCbr16)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:SYINfo:HACR {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Nr0) -> enums.AllHarqAckCbr16:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:SYINfo:HACR \n
		Snippet: value: enums.AllHarqAckCbr16 = driver.source.bb.nr5G.node.cell.syInfo.hacr.get(cellNull = repcap.CellNull.Nr0) \n
		Defines the state of the higher layer parameter pdsch-HARQ-ACK-Codebook-r16. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: codebook_r_16: NCON| EDYN NCON Does not apply the release 16 codebook (not configured) . NCON Applies the release 16 codebook (enhanced dynamic) ."""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:SYINfo:HACR?')
		return Conversions.str_to_scalar_enum(response, enums.AllHarqAckCbr16)
