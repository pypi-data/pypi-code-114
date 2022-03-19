from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CrcSize:
	"""CrcSize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("crcSize", core, parent)

	# noinspection PyTypeChecker
	def get(self, cell=repcap.Cell.Default, channel=repcap.Channel.Default) -> enums.TchCrc:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:BCH:DTCH<CH>:CRCSize \n
		Snippet: value: enums.TchCrc = driver.source.bb.tdscdma.down.cell.enh.bch.dtch.crcSize.get(cell = repcap.Cell.Default, channel = repcap.Channel.Default) \n
		The command queries the type (length) of the CRC. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:param channel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Dtch')
			:return: crc_size: NONE| 8| 12| 16| 24"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:BCH:DTCH{channel_cmd_val}:CRCSize?')
		return Conversions.str_to_scalar_enum(response, enums.TchCrc)
