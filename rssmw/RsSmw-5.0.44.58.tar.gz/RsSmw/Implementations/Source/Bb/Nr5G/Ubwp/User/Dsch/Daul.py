from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Daul:
	"""Daul commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("daul", core, parent)

	def set(self, ul_total_dai_inclu: bool, userNull=repcap.UserNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:DSCH:DAUL \n
		Snippet: driver.source.bb.nr5G.ubwp.user.dsch.daul.set(ul_total_dai_inclu = False, userNull = repcap.UserNull.Default) \n
		Configures the higher layer parameter ul-TotalDAI-Included as defined in 3GPP 38.331. \n
			:param ul_total_dai_inclu: 1| ON| 0| OFF
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
		"""
		param = Conversions.bool_to_str(ul_total_dai_inclu)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:DSCH:DAUL {param}')

	def get(self, userNull=repcap.UserNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:DSCH:DAUL \n
		Snippet: value: bool = driver.source.bb.nr5G.ubwp.user.dsch.daul.get(userNull = repcap.UserNull.Default) \n
		Configures the higher layer parameter ul-TotalDAI-Included as defined in 3GPP 38.331. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:return: ul_total_dai_inclu: No help available"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:DSCH:DAUL?')
		return Conversions.str_to_bool(response)
