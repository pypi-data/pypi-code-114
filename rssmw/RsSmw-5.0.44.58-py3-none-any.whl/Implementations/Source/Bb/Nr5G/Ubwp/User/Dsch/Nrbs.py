from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nrbs:
	"""Nrbs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nrbs", core, parent)

	def set(self, num_rb_set_ind: int, userNull=repcap.UserNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:DSCH:NRBS \n
		Snippet: driver.source.bb.nr5G.ubwp.user.dsch.nrbs.set(num_rb_set_ind = 1, userNull = repcap.UserNull.Default) \n
		Defines the number of the 'Available RB Set Indicators' fields in DCI format 2_0. \n
			:param num_rb_set_ind: integer Range: 0 to 16
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
		"""
		param = Conversions.decimal_value_to_str(num_rb_set_ind)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:DSCH:NRBS {param}')

	def get(self, userNull=repcap.UserNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:DSCH:NRBS \n
		Snippet: value: int = driver.source.bb.nr5G.ubwp.user.dsch.nrbs.get(userNull = repcap.UserNull.Default) \n
		Defines the number of the 'Available RB Set Indicators' fields in DCI format 2_0. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:return: num_rb_set_ind: No help available"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:DSCH:NRBS?')
		return Conversions.str_to_int(response)
