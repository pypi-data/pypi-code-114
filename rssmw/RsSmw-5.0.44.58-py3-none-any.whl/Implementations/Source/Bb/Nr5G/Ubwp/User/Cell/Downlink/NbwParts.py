from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NbwParts:
	"""NbwParts commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nbwParts", core, parent)

	def set(self, user_dl_bwp: int, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:DL:NBWParts \n
		Snippet: driver.source.bb.nr5G.ubwp.user.cell.downlink.nbwParts.set(user_dl_bwp = 1, userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default) \n
		Sets the number of downlink bandwidth parts (BWP) . \n
			:param user_dl_bwp: integer Range: 0 to 4
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.decimal_value_to_str(user_dl_bwp)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:DL:NBWParts {param}')

	def get(self, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:DL:NBWParts \n
		Snippet: value: int = driver.source.bb.nr5G.ubwp.user.cell.downlink.nbwParts.get(userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default) \n
		Sets the number of downlink bandwidth parts (BWP) . \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: user_dl_bwp: integer Range: 0 to 4"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:DL:NBWParts?')
		return Conversions.str_to_int(response)
