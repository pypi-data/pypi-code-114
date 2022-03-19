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

	# noinspection PyTypeChecker
	def get(self, cell=repcap.Cell.Default, channel=repcap.Channel.Default) -> enums.TdscdmaEnhTchTti:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:BCH:DTCH<CH>:TTINterval \n
		Snippet: value: enums.TdscdmaEnhTchTti = driver.source.bb.tdscdma.down.cell.enh.bch.dtch.ttInterval.get(cell = repcap.Cell.Default, channel = repcap.Channel.Default) \n
		Queries the number of frames into which a TCH is divided. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Dtch')
			:return: tt_interval: 5MS| 10MS| 20MS| 40MS| 80MS"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:BCH:DTCH{channel_cmd_val}:TTINterval?')
		return Conversions.str_to_scalar_enum(response, enums.TdscdmaEnhTchTti)
