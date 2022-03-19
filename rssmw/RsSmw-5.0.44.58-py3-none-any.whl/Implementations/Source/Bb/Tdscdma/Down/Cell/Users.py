from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Users:
	"""Users commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("users", core, parent)

	def set(self, users: enums.TdscdmaTotalUsers, cell=repcap.Cell.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:USERs \n
		Snippet: driver.source.bb.tdscdma.down.cell.users.set(users = enums.TdscdmaTotalUsers._10, cell = repcap.Cell.Default) \n
		Sets the total number of users of the cell. \n
			:param users: 2| 4| 6| 8| 10| 12| 14| 16
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(users, enums.TdscdmaTotalUsers)
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:USERs {param}')

	# noinspection PyTypeChecker
	def get(self, cell=repcap.Cell.Default) -> enums.TdscdmaTotalUsers:
		"""SCPI: [SOURce<HW>]:BB:TDSCdma:DOWN:CELL<ST>:USERs \n
		Snippet: value: enums.TdscdmaTotalUsers = driver.source.bb.tdscdma.down.cell.users.get(cell = repcap.Cell.Default) \n
		Sets the total number of users of the cell. \n
			:param cell: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cell')
			:return: users: 2| 4| 6| 8| 10| 12| 14| 16"""
		cell_cmd_val = self._cmd_group.get_repcap_cmd_value(cell, repcap.Cell)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:TDSCdma:DOWN:CELL{cell_cmd_val}:USERs?')
		return Conversions.str_to_scalar_enum(response, enums.TdscdmaTotalUsers)
