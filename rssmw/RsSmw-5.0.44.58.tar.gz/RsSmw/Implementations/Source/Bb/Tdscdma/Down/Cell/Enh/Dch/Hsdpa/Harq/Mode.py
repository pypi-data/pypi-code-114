from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.EnhHsHarqMode, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:HSDPA:HARQ:MODE \n
		Snippet: driver.source.bb.tdscdma.down.cell.enh.dch.hsdpa.harq.mode.set(mode = enums.EnhHsHarqMode.CACK, cell = repcap.Cell.Default) \n
		Sets the HARQ simulation mode. \n
			:param mode: CACK| CNACk CACK New data is used for each new TTI. This mode is used to simulate maximum throughput transmission. CNACk Enables NACK simulation, i.e. depending on the sequence selected with command BB:TDSC:DOWN:CELL1:ENH:DCH:HSDPA:RVS packets are retransmitted. This mode is used for testing with varying redundancy version.
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.EnhHsHarqMode)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:HSDPA:HARQ:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, cell=repcap.Cell.Default) -> enums.EnhHsHarqMode:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:HSDPA:HARQ:MODE \n
		Snippet: value: enums.EnhHsHarqMode = driver.source.bb.tdscdma.down.cell.enh.dch.hsdpa.harq.mode.get(cell = repcap.Cell.Default) \n
		Sets the HARQ simulation mode. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: mode: CACK| CNACk CACK New data is used for each new TTI. This mode is used to simulate maximum throughput transmission. CNACk Enables NACK simulation, i.e. depending on the sequence selected with command BB:TDSC:DOWN:CELL1:ENH:DCH:HSDPA:RVS packets are retransmitted. This mode is used for testing with varying redundancy version."""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:HSDPA:HARQ:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.EnhHsHarqMode)
