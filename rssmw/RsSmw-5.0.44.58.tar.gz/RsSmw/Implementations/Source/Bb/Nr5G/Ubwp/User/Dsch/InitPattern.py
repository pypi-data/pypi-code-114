from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InitPattern:
	"""InitPattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("initPattern", core, parent)

	def set(self, pattern_init: int, userNull=repcap.UserNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:DSCH:INITpattern \n
		Snippet: driver.source.bb.nr5G.ubwp.user.dsch.initPattern.set(pattern_init = 1, userNull = repcap.UserNull.Default) \n
		Sets an initialization value for the second m-sequence in the PN sequence. \n
			:param pattern_init: float Range: 1 to 0x7fffff
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
		"""
		param = Conversions.decimal_value_to_str(pattern_init)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:DSCH:INITpattern {param}')

	def get(self, userNull=repcap.UserNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:DSCH:INITpattern \n
		Snippet: value: int = driver.source.bb.nr5G.ubwp.user.dsch.initPattern.get(userNull = repcap.UserNull.Default) \n
		Sets an initialization value for the second m-sequence in the PN sequence. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:return: pattern_init: float Range: 1 to 0x7fffff"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:DSCH:INITpattern?')
		return Conversions.str_to_int(response)
