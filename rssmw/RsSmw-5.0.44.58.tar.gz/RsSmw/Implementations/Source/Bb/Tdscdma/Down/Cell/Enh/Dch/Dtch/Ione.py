from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ione:
	"""Ione commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ione", core, parent)

	def set(self, ione: bool, cell=repcap.Cell.Default, channel=repcap.Channel.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:DTCH<CH>:IONE \n
		Snippet: driver.source.bb.tdscdma.down.cell.enh.dch.dtch.ione.set(ione = False, cell = repcap.Cell.Default, channel = repcap.Channel.Default) \n
		Activates or deactivates the channel coding interleaver state 1 and 2 off all the transport channels. Interleaver state 1
		and 2 can only be set for all the TCHs together. Activation does not change the symbol rate. \n
			:param ione: 1| ON| 0| OFF
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Dtch')
		"""
		param = Conversions.bool_to_str(ione)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:DTCH{channel_cmd_val}:IONE {param}')

	def get(self, cell=repcap.Cell.Default, channel=repcap.Channel.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:DTCH<CH>:IONE \n
		Snippet: value: bool = driver.source.bb.tdscdma.down.cell.enh.dch.dtch.ione.get(cell = repcap.Cell.Default, channel = repcap.Channel.Default) \n
		Activates or deactivates the channel coding interleaver state 1 and 2 off all the transport channels. Interleaver state 1
		and 2 can only be set for all the TCHs together. Activation does not change the symbol rate. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Dtch')
			:return: ione: No help available"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:DTCH{channel_cmd_val}:IONE?')
		return Conversions.str_to_bool(response)
