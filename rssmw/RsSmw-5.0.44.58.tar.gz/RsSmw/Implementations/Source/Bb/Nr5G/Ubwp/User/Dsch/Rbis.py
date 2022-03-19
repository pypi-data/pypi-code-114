from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rbis:
	"""Rbis commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbis", core, parent)

	def set(self, indicator_size: int, userNull=repcap.UserNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:DSCH:RBIS \n
		Snippet: driver.source.bb.nr5G.ubwp.user.dsch.rbis.set(indicator_size = 1, userNull = repcap.UserNull.Default) \n
		Defines the size of the 'Available RB Set Indicator' field in DCI format 2_0. \n
			:param indicator_size: integer Range: 1 to 5
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
		"""
		param = Conversions.decimal_value_to_str(indicator_size)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:DSCH:RBIS {param}')

	def get(self, userNull=repcap.UserNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:DSCH:RBIS \n
		Snippet: value: int = driver.source.bb.nr5G.ubwp.user.dsch.rbis.get(userNull = repcap.UserNull.Default) \n
		Defines the size of the 'Available RB Set Indicator' field in DCI format 2_0. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:return: indicator_size: integer Range: 1 to 5"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:DSCH:RBIS?')
		return Conversions.str_to_int(response)
