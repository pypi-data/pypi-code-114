from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, ssch_cha_coding: bool, userNull=repcap.UserNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:SSCH:CCODing:STATe \n
		Snippet: driver.source.bb.nr5G.ubwp.user.ssch.ccoding.state.set(ssch_cha_coding = False, userNull = repcap.UserNull.Default) \n
		No command help available \n
			:param ssch_cha_coding: No help available
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
		"""
		param = Conversions.bool_to_str(ssch_cha_coding)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:SSCH:CCODing:STATe {param}')

	def get(self, userNull=repcap.UserNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:SSCH:CCODing:STATe \n
		Snippet: value: bool = driver.source.bb.nr5G.ubwp.user.ssch.ccoding.state.get(userNull = repcap.UserNull.Default) \n
		No command help available \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:return: ssch_cha_coding: No help available"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:SSCH:CCODing:STATe?')
		return Conversions.str_to_bool(response)
