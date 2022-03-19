from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Foffset:
	"""Foffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("foffset", core, parent)

	def set(self, frequency_offset: int, ceLevel=repcap.CeLevel.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:EMTC:CELV<CH0>:FOFFset \n
		Snippet: driver.source.bb.eutra.uplink.prach.emtc.celv.foffset.set(frequency_offset = 1, ceLevel = repcap.CeLevel.Default) \n
		Sets a frequency offset in terms of resource blocks. \n
			:param frequency_offset: integer Range: 0 to 94
			:param ceLevel: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Celv')
		"""
		param = Conversions.decimal_value_to_str(frequency_offset)
		ceLevel_cmd_val = self._cmd_group.get_repcap_cmd_value(ceLevel, repcap.CeLevel)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:EMTC:CELV{ceLevel_cmd_val}:FOFFset {param}')

	def get(self, ceLevel=repcap.CeLevel.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:PRACh:EMTC:CELV<CH0>:FOFFset \n
		Snippet: value: int = driver.source.bb.eutra.uplink.prach.emtc.celv.foffset.get(ceLevel = repcap.CeLevel.Default) \n
		Sets a frequency offset in terms of resource blocks. \n
			:param ceLevel: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Celv')
			:return: frequency_offset: integer Range: 0 to 94"""
		ceLevel_cmd_val = self._cmd_group.get_repcap_cmd_value(ceLevel, repcap.CeLevel)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:PRACh:EMTC:CELV{ceLevel_cmd_val}:FOFFset?')
		return Conversions.str_to_int(response)
