from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eprotection:
	"""Eprotection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eprotection", core, parent)

	# noinspection PyTypeChecker
	def get(self, cell=repcap.Cell.Default, channel=repcap.Channel.Default) -> enums.EnhTchErr:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:BCH:DTCH<CH>:EPRotection \n
		Snippet: value: enums.EnhTchErr = driver.source.bb.tdscdma.down.cell.enh.bch.dtch.eprotection.get(cell = repcap.Cell.Default, channel = repcap.Channel.Default) \n
		Queries the error protection. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Dtch')
			:return: eprotection: NONE| TURBo3| CON2| CON3"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:BCH:DTCH{channel_cmd_val}:EPRotection?')
		return Conversions.str_to_scalar_enum(response, enums.EnhTchErr)
