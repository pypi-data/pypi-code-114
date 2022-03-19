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

	def set(self, scs_mode: enums.AutoUser, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:SCSMode \n
		Snippet: driver.source.bb.tdscdma.down.cell.enh.dch.scsMode.set(scs_mode = enums.AutoUser.AUTO, cell = repcap.Cell.Default) \n
		Sets the spreading code selection mode for the used transport channels. \n
			:param scs_mode: AUTO| USER
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(scs_mode, enums.AutoUser)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:SCSMode {param}')

	# noinspection PyTypeChecker
	def get(self, cell=repcap.Cell.Default) -> enums.AutoUser:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:ENH:DCH:SCSMode \n
		Snippet: value: enums.AutoUser = driver.source.bb.tdscdma.down.cell.enh.dch.scsMode.get(cell = repcap.Cell.Default) \n
		Sets the spreading code selection mode for the used transport channels. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: scs_mode: AUTO| USER"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:ENH:DCH:SCSMode?')
		return Conversions.str_to_scalar_enum(response, enums.AutoUser)
