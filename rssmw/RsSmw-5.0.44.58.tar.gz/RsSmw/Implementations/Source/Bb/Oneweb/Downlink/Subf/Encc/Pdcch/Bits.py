from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bits:
	"""Bits commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bits", core, parent)

	def get(self, subframeNull=repcap.SubframeNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:[SUBF<ST0>]:ENCC:PDCCh:BITS \n
		Snippet: value: int = driver.source.bb.oneweb.downlink.subf.encc.pdcch.bits.get(subframeNull = repcap.SubframeNull.Default) \n
		Queries the number of bits allocated for PDCCH. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:return: phys_bits: integer Range: 0 to 1E5"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:DL:SUBF{subframeNull_cmd_val}:ENCC:PDCCh:BITS?')
		return Conversions.str_to_int(response)
