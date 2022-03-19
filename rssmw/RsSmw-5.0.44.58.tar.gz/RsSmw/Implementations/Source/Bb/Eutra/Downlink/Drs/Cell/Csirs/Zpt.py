from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Zpt:
	"""Zpt commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("zpt", core, parent)

	def get(self, cellNull=repcap.CellNull.Default, csiRefSignal=repcap.CsiRefSignal.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DRS:CELL<CH0>:CSIRs<ST>:ZPT \n
		Snippet: value: int = driver.source.bb.eutra.downlink.drs.cell.csirs.zpt.get(cellNull = repcap.CellNull.Default, csiRefSignal = repcap.CsiRefSignal.Default) \n
		Queries the subframe configuration period TCSI-RS value. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param csiRefSignal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Csirs')
			:return: periodicity: integer Range: 5 to 80"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		csiRefSignal_cmd_val = self._cmd_group.get_repcap_cmd_value(csiRefSignal, repcap.CsiRefSignal)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:DRS:CELL{cellNull_cmd_val}:CSIRs{csiRefSignal_cmd_val}:ZPT?')
		return Conversions.str_to_int(response)
