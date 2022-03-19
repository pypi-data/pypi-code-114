from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nssf:
	"""Nssf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nssf", core, parent)

	def set(self, search_space_sw_fl: int, userNull=repcap.UserNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:DSCH:NSSF \n
		Snippet: driver.source.bb.nr5G.ubwp.user.dsch.nssf.set(search_space_sw_fl = 1, userNull = repcap.UserNull.Default) \n
		Defines the number of the 'Search Space Switching Flags' fields in DCI format 2_0. \n
			:param search_space_sw_fl: integer Range: 0 to 4
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
		"""
		param = Conversions.decimal_value_to_str(search_space_sw_fl)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:DSCH:NSSF {param}')

	def get(self, userNull=repcap.UserNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:DSCH:NSSF \n
		Snippet: value: int = driver.source.bb.nr5G.ubwp.user.dsch.nssf.get(userNull = repcap.UserNull.Default) \n
		Defines the number of the 'Search Space Switching Flags' fields in DCI format 2_0. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:return: search_space_sw_fl: No help available"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:DSCH:NSSF?')
		return Conversions.str_to_int(response)
