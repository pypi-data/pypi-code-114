from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, baseband=repcap.Baseband.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:USER:[BB<ST>]:HOTime:STATe \n
		Snippet: driver.source.bb.esequencer.user.bb.hoTime.state.set(state = False, baseband = repcap.Baseband.Default) \n
		Enables the selected frequency hopping list to be included in the signal generation. Select a frequency hopping list file
		first, see [:SOURce<hw>]:BB:ESEQuencer:USER[:BB<st>]:HOTime:FILE[:SELect]. \n
			:param state: 1| ON| 0| OFF
			:param baseband: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bb')
		"""
		param = Conversions.bool_to_str(state)
		baseband_cmd_val = self._cmd_group.get_repcap_cmd_value(baseband, repcap.Baseband)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:USER:BB{baseband_cmd_val}:HOTime:STATe {param}')

	def get(self, baseband=repcap.Baseband.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:USER:[BB<ST>]:HOTime:STATe \n
		Snippet: value: bool = driver.source.bb.esequencer.user.bb.hoTime.state.get(baseband = repcap.Baseband.Default) \n
		Enables the selected frequency hopping list to be included in the signal generation. Select a frequency hopping list file
		first, see [:SOURce<hw>]:BB:ESEQuencer:USER[:BB<st>]:HOTime:FILE[:SELect]. \n
			:param baseband: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bb')
			:return: state: 1| ON| 0| OFF"""
		baseband_cmd_val = self._cmd_group.get_repcap_cmd_value(baseband, repcap.Baseband)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:USER:BB{baseband_cmd_val}:HOTime:STATe?')
		return Conversions.str_to_bool(response)
