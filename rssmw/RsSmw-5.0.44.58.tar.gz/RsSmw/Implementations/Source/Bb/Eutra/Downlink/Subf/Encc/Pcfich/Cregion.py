from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cregion:
	"""Cregion commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cregion", core, parent)

	def set(self, control_region: int, subframeNull=repcap.SubframeNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PCFich:CREGion \n
		Snippet: driver.source.bb.eutra.downlink.subf.encc.pcfich.cregion.set(control_region = 1, subframeNull = repcap.SubframeNull.Default) \n
		Sets the number of OFDM Symbols to be used for PDCCH. \n
			:param control_region: integer Range: 1 to 4
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
		"""
		param = Conversions.decimal_value_to_str(control_region)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PCFich:CREGion {param}')

	def get(self, subframeNull=repcap.SubframeNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PCFich:CREGion \n
		Snippet: value: int = driver.source.bb.eutra.downlink.subf.encc.pcfich.cregion.get(subframeNull = repcap.SubframeNull.Default) \n
		Sets the number of OFDM Symbols to be used for PDCCH. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:return: control_region: integer Range: 1 to 4"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PCFich:CREGion?')
		return Conversions.str_to_int(response)
