from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, filename: str, baseband=repcap.Baseband.Default, attenuationList=repcap.AttenuationList.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:USER:[BB<ST>]:AOTime<CH>:FILE:[SELect] \n
		Snippet: driver.source.bb.esequencer.user.bb.aoTime.file.select.set(filename = '1', baseband = repcap.Baseband.Default, attenuationList = repcap.AttenuationList.Default) \n
		Selects an existing attenuation list file. \n
			:param filename: string
			:param baseband: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bb')
			:param attenuationList: optional repeated capability selector. Default value: Nr1 (settable in the interface 'AoTime')
		"""
		param = Conversions.value_to_quoted_str(filename)
		baseband_cmd_val = self._cmd_group.get_repcap_cmd_value(baseband, repcap.Baseband)
		attenuationList_cmd_val = self._cmd_group.get_repcap_cmd_value(attenuationList, repcap.AttenuationList)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:USER:BB{baseband_cmd_val}:AOTime{attenuationList_cmd_val}:FILE:SELect {param}')

	def get(self, baseband=repcap.Baseband.Default, attenuationList=repcap.AttenuationList.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:USER:[BB<ST>]:AOTime<CH>:FILE:[SELect] \n
		Snippet: value: str = driver.source.bb.esequencer.user.bb.aoTime.file.select.get(baseband = repcap.Baseband.Default, attenuationList = repcap.AttenuationList.Default) \n
		Selects an existing attenuation list file. \n
			:param baseband: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bb')
			:param attenuationList: optional repeated capability selector. Default value: Nr1 (settable in the interface 'AoTime')
			:return: filename: string"""
		baseband_cmd_val = self._cmd_group.get_repcap_cmd_value(baseband, repcap.Baseband)
		attenuationList_cmd_val = self._cmd_group.get_repcap_cmd_value(attenuationList, repcap.AttenuationList)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:USER:BB{baseband_cmd_val}:AOTime{attenuationList_cmd_val}:FILE:SELect?')
		return trim_str_response(response)
