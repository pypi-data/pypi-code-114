from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Zpi:
	"""Zpi commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("zpi", core, parent)

	def set(self, sf_config: int, cellNull=repcap.CellNull.Default, csiRefSignal=repcap.CsiRefSignal.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DRS:CELL<CH0>:CSIRs<ST>:ZPI \n
		Snippet: driver.source.bb.eutra.downlink.drs.cell.csirs.zpi.set(sf_config = 1, cellNull = repcap.CellNull.Default, csiRefSignal = repcap.CsiRefSignal.Default) \n
		Sets the parameter ICSI-RS. \n
			:param sf_config: integer Range: 0 to 154
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param csiRefSignal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Csirs')
		"""
		param = Conversions.decimal_value_to_str(sf_config)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		csiRefSignal_cmd_val = self._cmd_group.get_repcap_cmd_value(csiRefSignal, repcap.CsiRefSignal)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:DRS:CELL{cellNull_cmd_val}:CSIRs{csiRefSignal_cmd_val}:ZPI {param}')

	def get(self, cellNull=repcap.CellNull.Default, csiRefSignal=repcap.CsiRefSignal.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DRS:CELL<CH0>:CSIRs<ST>:ZPI \n
		Snippet: value: int = driver.source.bb.eutra.downlink.drs.cell.csirs.zpi.get(cellNull = repcap.CellNull.Default, csiRefSignal = repcap.CsiRefSignal.Default) \n
		Sets the parameter ICSI-RS. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param csiRefSignal: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Csirs')
			:return: sf_config: integer Range: 0 to 154"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		csiRefSignal_cmd_val = self._cmd_group.get_repcap_cmd_value(csiRefSignal, repcap.CsiRefSignal)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:DRS:CELL{cellNull_cmd_val}:CSIRs{csiRefSignal_cmd_val}:ZPI?')
		return Conversions.str_to_int(response)
