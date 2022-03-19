from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScsMode:
	"""ScsMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scsMode", core, parent)

	# noinspection PyTypeChecker
	def get(self, cell=repcap.Cell.Default) -> enums.AutoUser:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:BCH:SCSMode \n
		Snippet: value: enums.AutoUser = driver.source.bb.tdscdma.down.cell.enh.bch.scsMode.get(cell = repcap.Cell.Default) \n
		Queries the spreading code predetermined in the standard. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: scs_mode: AUTO"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:BCH:SCSMode?')
		return Conversions.str_to_scalar_enum(response, enums.AutoUser)
