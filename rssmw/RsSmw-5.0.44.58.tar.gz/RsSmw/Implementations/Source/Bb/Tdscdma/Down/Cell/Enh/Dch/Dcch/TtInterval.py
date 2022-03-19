from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TtInterval:
	"""TtInterval commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ttInterval", core, parent)

	def set(self, tt_interval: enums.TdscdmaEnhTchTti, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:DCCH:TTINterval \n
		Snippet: driver.source.bb.tdscdma.down.cell.enh.dch.dcch.ttInterval.set(tt_interval = enums.TdscdmaEnhTchTti._10MS, cell = repcap.Cell.Default) \n
		Sets the number of frames into which a TCH is divided. This setting also defines the interleaver depth. \n
			:param tt_interval: 5MS| 10MS| 20MS| 40MS
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(tt_interval, enums.TdscdmaEnhTchTti)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:DCCH:TTINterval {param}')

	# noinspection PyTypeChecker
	def get(self, cell=repcap.Cell.Default) -> enums.TdscdmaEnhTchTti:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:DCCH:TTINterval \n
		Snippet: value: enums.TdscdmaEnhTchTti = driver.source.bb.tdscdma.down.cell.enh.dch.dcch.ttInterval.get(cell = repcap.Cell.Default) \n
		Sets the number of frames into which a TCH is divided. This setting also defines the interleaver depth. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: tt_interval: 5MS| 10MS| 20MS| 40MS"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:DCCH:TTINterval?')
		return Conversions.str_to_scalar_enum(response, enums.TdscdmaEnhTchTti)
