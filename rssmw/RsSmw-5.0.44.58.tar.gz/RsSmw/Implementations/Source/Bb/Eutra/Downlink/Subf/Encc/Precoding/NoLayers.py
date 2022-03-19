from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NoLayers:
	"""NoLayers commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("noLayers", core, parent)

	def get(self, subframeNull=repcap.SubframeNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:[SUBF<ST0>]:ENCC:PRECoding:NOLayers \n
		Snippet: value: int = driver.source.bb.eutra.downlink.subf.encc.precoding.noLayers.get(subframeNull = repcap.SubframeNull.Default) \n
		Queries the number of layers for PDCCH. This value is fixed to 1 for PDCCH. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:return: layer_count: integer Range: 1 to 2"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:SUBF{subframeNull_cmd_val}:ENCC:PRECoding:NOLayers?')
		return Conversions.str_to_int(response)
