from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scgw:
	"""Scgw commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scgw", core, parent)

	def set(self, cell_groups_within: int, userNull=repcap.UserNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:DSCH:SCGW \n
		Snippet: driver.source.bb.nr5G.ubwp.user.dsch.scgw.set(cell_groups_within = 1, userNull = repcap.UserNull.Default) \n
		Sets the parameter 'Number of SCell Groups Within Active Time'. \n
			:param cell_groups_within: integer Range: 0 to 5
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
		"""
		param = Conversions.decimal_value_to_str(cell_groups_within)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:DSCH:SCGW {param}')

	def get(self, userNull=repcap.UserNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:DSCH:SCGW \n
		Snippet: value: int = driver.source.bb.nr5G.ubwp.user.dsch.scgw.get(userNull = repcap.UserNull.Default) \n
		Sets the parameter 'Number of SCell Groups Within Active Time'. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:return: cell_groups_within: No help available"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:DSCH:SCGW?')
		return Conversions.str_to_int(response)
