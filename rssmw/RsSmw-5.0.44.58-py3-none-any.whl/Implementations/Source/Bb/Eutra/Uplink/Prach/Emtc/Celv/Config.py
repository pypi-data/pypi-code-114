from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Config:
	"""Config commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("config", core, parent)

	def set(self, config: int, ceLevel=repcap.CeLevel.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:EMTC:CELV<CH0>:CONFig \n
		Snippet: driver.source.bb.eutra.uplink.prach.emtc.celv.config.set(config = 1, ceLevel = repcap.CeLevel.Default) \n
		Selects the PRACH configuration index. \n
			:param config: integer Range: 0 to 63
			:param ceLevel: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Celv')
		"""
		param = Conversions.decimal_value_to_str(config)
		ceLevel_cmd_val = self._cmd_group.get_repcap_cmd_value(ceLevel, repcap.CeLevel)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:EMTC:CELV{ceLevel_cmd_val}:CONFig {param}')

	def get(self, ceLevel=repcap.CeLevel.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:EMTC:CELV<CH0>:CONFig \n
		Snippet: value: int = driver.source.bb.eutra.uplink.prach.emtc.celv.config.get(ceLevel = repcap.CeLevel.Default) \n
		Selects the PRACH configuration index. \n
			:param ceLevel: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Celv')
			:return: config: integer Range: 0 to 63"""
		ceLevel_cmd_val = self._cmd_group.get_repcap_cmd_value(ceLevel, repcap.CeLevel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:EMTC:CELV{ceLevel_cmd_val}:CONFig?')
		return Conversions.str_to_int(response)
