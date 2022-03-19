from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hopping:
	"""Hopping commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hopping", core, parent)

	def set(self, hopping: bool, ceLevel=repcap.CeLevel.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:EMTC:CELV<CH0>:HOPPing \n
		Snippet: driver.source.bb.eutra.uplink.prach.emtc.celv.hopping.set(hopping = False, ceLevel = repcap.CeLevel.Default) \n
		Enables frequency hopping. \n
			:param hopping: 1| ON| 0| OFF
			:param ceLevel: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Celv')
		"""
		param = Conversions.bool_to_str(hopping)
		ceLevel_cmd_val = self._cmd_group.get_repcap_cmd_value(ceLevel, repcap.CeLevel)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:EMTC:CELV{ceLevel_cmd_val}:HOPPing {param}')

	def get(self, ceLevel=repcap.CeLevel.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:EMTC:CELV<CH0>:HOPPing \n
		Snippet: value: bool = driver.source.bb.eutra.uplink.prach.emtc.celv.hopping.get(ceLevel = repcap.CeLevel.Default) \n
		Enables frequency hopping. \n
			:param ceLevel: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Celv')
			:return: hopping: 1| ON| 0| OFF"""
		ceLevel_cmd_val = self._cmd_group.get_repcap_cmd_value(ceLevel, repcap.CeLevel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:EMTC:CELV{ceLevel_cmd_val}:HOPPing?')
		return Conversions.str_to_bool(response)
