from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cdin:
	"""Cdin commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cdin", core, parent)

	def set(self, cot_duration_ind: int, userNull=repcap.UserNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:DSCH:CDIN \n
		Snippet: driver.source.bb.nr5G.ubwp.user.dsch.cdin.set(cot_duration_ind = 1, userNull = repcap.UserNull.Default) \n
		Defines the number of the 'COT Duration Indicators' fields in DCI format 2_0. \n
			:param cot_duration_ind: integer Range: 0 to 16
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
		"""
		param = Conversions.decimal_value_to_str(cot_duration_ind)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:DSCH:CDIN {param}')

	def get(self, userNull=repcap.UserNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:DSCH:CDIN \n
		Snippet: value: int = driver.source.bb.nr5G.ubwp.user.dsch.cdin.get(userNull = repcap.UserNull.Default) \n
		Defines the number of the 'COT Duration Indicators' fields in DCI format 2_0. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:return: cot_duration_ind: No help available"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:DSCH:CDIN?')
		return Conversions.str_to_int(response)
